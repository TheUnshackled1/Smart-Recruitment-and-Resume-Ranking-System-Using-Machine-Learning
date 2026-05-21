import warnings
try:
    import textract  # optional: only for .doc/.docx resumes
except ImportError:
    textract = None
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import pathlib
from json import load, dumps
from operator import getitem
from collections import OrderedDict
from .text_process import normalize

import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
import mysite.configurations as regex
from datetime import date

from collections import defaultdict
from datetime import datetime
from dateutil import relativedelta
from typing import *


warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')


def getFilePath(loc):
    temp = str(loc)
    temp = temp.replace('\\', '/')
    return temp


def getFileName(filename):
    return filename.rsplit('\\')[1]


def readResultInJson(jobfile='job1'):
    filepath = 'result/'
    with open(filepath + jobfile + '.json', 'r') as openfile:
        # Reading from json file
        result = load(openfile)
    return result


def writeResultInJson(data, jobfile='job1'):
    filepath = 'result/'
    json_str = dumps(data, indent=4)
    with open(filepath + jobfile + '.json', 'w+', encoding='utf-8') as f:
        f.write(json_str)
        f.close()


def getNumberOfMonths(datepair) -> int:
    """
    Helper function to extract total months of experience from a resume
    :param date1: Starting date
    :param date2: Ending date
    :return: months of experience from date1 to date2
        """

    # if years
    date2_parsed = False
    if datepair.get("fh", None) is not None:
        gap = datepair["fh"]
    else:
        gap = ""
    try:
        present_vocab = ("present", "date", "now")
        if "syear" in datepair:
            date1 = datepair["fyear"]
            date2 = datepair["syear"]

            if date2.lower() in present_vocab:
                date2 = datetime.now()
                date2_parsed = True

            try:
                if not date2_parsed:
                    date2 = datetime.strptime(str(date2), "%Y")
                date1 = datetime.strptime(str(date1), "%Y")
            except:
                pass
        elif "smonth_num" in datepair:
            date1 = datepair["fmonth_num"]
            date2 = datepair["smonth_num"]

            if date2.lower() in present_vocab:
                date2 = datetime.now()
                date2_parsed = True

            for stype in ("%m" + gap + "%Y", "%m" + gap + "%y"):
                try:
                    if not date2_parsed:
                        date2 = datetime.strptime(str(date2), stype)
                    date1 = datetime.strptime(str(date1), stype)
                    break
                except:
                    pass
        else:
            date1 = datepair["fmonth"]
            date2 = datepair["smonth"]

            if date2.lower() in present_vocab:
                date2 = datetime.now()
                date2_parsed = True

            for stype in (
                "%b" + gap + "%Y",
                "%b" + gap + "%y",
                "%B" + gap + "%Y",
                "%B" + gap + "%y",
            ):
                try:
                    if not date2_parsed:
                        date2 = datetime.strptime(str(date2), stype)
                    date1 = datetime.strptime(str(date1), stype)
                    break
                except:
                    pass

        months_of_experience = relativedelta.relativedelta(date2, date1)
        months_of_experience = (
            months_of_experience.years * 12 + months_of_experience.months
        )
        return months_of_experience
    except Exception as e:
        return 0


def getTotalExperience(experience_list) -> int:
    """
    Wrapper function to extract total months of experience from a resume
    :param experience_list: list of experience text extracted
    :return: total months of experience
    """
    exp_ = []
    for line in experience_list:
        line = line.lower().strip()
        # have to split search since regex OR does not capture on a first-come-first-serve basis
        experience = re.search(
            r"(?P<fyear>\d{4})\s*(\s|-|to)\s*(?P<syear>\d{4}|present|date|now)",
            line,
            re.I,
        )
        if experience:
            d = experience.groupdict()
            exp_.append(d)
            continue

        experience = re.search(
            r"(?P<fmonth>\w+(?P<fh>.)\d+)\s*(\s|-|to)\s*(?P<smonth>\w+(?P<sh>.)\d+|present|date|now)",
            line,
            re.I,
        )
        if experience:
            d = experience.groupdict()
            exp_.append(d)
            continue

        experience = re.search(
            r"(?P<fmonth_num>\d+(?P<fh>.)\d+)\s*(\s|-|to)\s*(?P<smonth_num>\d+(?P<sh>.)\d+|present|date|now)",
            line,
            re.I,
        )
        if experience:
            d = experience.groupdict()
            exp_.append(d)
            continue
    experience_num_list = [getNumberOfMonths(i) for i in exp_]
    total_experience_in_months = sum(experience_num_list)
    return total_experience_in_months


"""
Utility Function that calculates experience in the resume text
params: resume_text type:string
returns: experience type:int
"""
def calculate_experience(resume_text):
  def get_month_index(month):
    month_dict = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
    return month_dict[month.lower()]

  try:
    start_month = -1
    start_year = -1
    end_month = -1
    end_year = -1
    regular_expression = re.compile(regex.date_range, re.IGNORECASE)
    regex_result = re.search(regular_expression, resume_text)
    while regex_result:
      date_range = regex_result.group()
      year_regex = re.compile(regex.year)
      year_result = re.search(year_regex, date_range)
      if (start_year == -1) or (int(year_result.group()) <= start_year):
        start_year = int(year_result.group())
        month_regex = re.compile(regex.months_short, re.IGNORECASE)
        month_result = re.search(month_regex, date_range)
        if month_result:
          current_month = get_month_index(month_result.group())
          if (start_month == -1) or (current_month < start_month):
            start_month = current_month
      if date_range.lower().find('present') != -1:
        end_month = date.today().month # current month
        end_year = date.today().year # current year
      else:
        year_result = re.search(year_regex, date_range[year_result.end():])
        if (end_year == -1) or (int(year_result.group()) >= end_year):
          end_year = int(year_result.group())
          month_regex = re.compile(regex.months_short, re.IGNORECASE)
          month_result = re.search(month_regex, date_range)
          if month_result:
            current_month = get_month_index(month_result.group())
            if (end_month == -1) or (current_month > end_month):
              end_month = current_month
      resume_text = resume_text[regex_result.end():]
      regex_result = re.search(regular_expression, resume_text)

    return end_year - start_year  # Use the obtained month attribute
  except Exception as exception_instance:
    # logging.error('Issue calculating experience: '+str(exception_instance))
    print('Issue calculating experience: '+str(exception_instance))
    return None


def get_experience_year(job_expr):
    job_expr = str.split(job_expr, ' ')[0]
    if '-' in job_expr:
        expr = job_expr.split('-')
        return int(expr[0])*12, int(expr[1])*12
    return int(job_expr)*12, -1


# for 2nd method
def getTotalExperienceFormatted(exp_list, job_expr) -> bool:

    min_yr_in_month, max_yr_in_month = get_experience_year(job_expr)
    print(min_yr_in_month, max_yr_in_month)
    print(exp_list)
    months = getTotalExperience(exp_list)

    if max_yr_in_month != -1:
        if (months >= min_yr_in_month) and (months <= max_yr_in_month):
            return True
    else:
        if months >= min_yr_in_month:
            return True
    return False


def findWorkAndEducation(text, name) -> Dict[str, List[str]]:
    categories = {"Work": ["(Work|WORK)", "(Experience(s?)|EXPERIENCE(S?))", "(History|HISTORY)"]}
    inv_data = {v[0][1]: (v[0][0], k) for k, v in categories.items()}
    line_count = 0
    exp_list = defaultdict(list)
    name = name.lower()

    current_line = None
    is_dot = False
    is_space = True
    continuation_sent = []
    first_line = None
    unique_char_regex = "[^\sA-Za-z0-9\.\/\(\)\,\-\|]+"

    for line in text.split("\n"):
        line = re.sub(r"\s+", " ", line).strip()
        match = re.search(r"^.*:", line)
        if match:
            line = line[match.end():].strip()

        # get first non-space line for filtering since
        # sometimes it might be a page header
        if line and first_line is None:
            first_line = line

        # update line_countfirst since there are `continue`s below
        line_count += 1
        if (line_count - 1) in inv_data:
            current_line = inv_data[line_count - 1][1]
        # contains a full-blown state-machine for filtering stuff
        elif current_line == "Work":
            if line:
                # if name is inside, skip
                if name == line:
                    continue
                # if like first line of resume, skip
                if line == first_line:
                    continue
                # check if it's not a list with some unique character as list bullet
                has_dot = re.findall(unique_char_regex, line[:5])
                # if last paragraph is a list item
                if is_dot:
                    # if this paragraph is not a list item and the previous line is a space
                    if not has_dot and is_space:
                        if line[0].isupper() or re.findall(r"^\d+\.", line[:5]):
                            exp_list[current_line].append(line)
                            is_dot = False

                else:
                    if not has_dot and (
                        line[0].isupper() or re.findall(r"^\d+\.", line[:5])
                    ):
                        exp_list[current_line].append(line)
                        is_dot = False
                if has_dot:
                    is_dot = True
                is_space = False
            else:
                is_space = True
        elif current_line == "Education":
            if line:
                # if not like first line
                if line == first_line:
                    continue
                line = re.sub(unique_char_regex, '', line[:5]) + line[5:]
                if len(line) < 12:
                    continuation_sent.append(line)
                else:
                    if continuation_sent:
                        continuation_sent.append(line)
                        line = " ".join(continuation_sent)
                        continuation_sent = []
                    exp_list[current_line].append(line)

    return exp_list


def check_basicRequirement(resumes_data, job_data):
    # print(job_experience)
    Ordered_list_Resume = []
    Resumes = []
    Temp_pdf = ''
    # print(int(job_data.experience.split(' ')[0].split('-')[0]))
    # print(len(resumes_data))
    # filter resumes based on the gender
    resumes_data = resumes_data.filter(experience__gte=float(job_data.experience.split(' ')[0].split('-')[0]))
    print(len(resumes_data))
    if job_data.gender == 'Male':
        resumes_data = resumes_data.filter(gender='Male')
    elif job_data.gender == 'Female':
        resumes_data = resumes_data.filter(gender='Female')

    # resumes file path
    filepath = 'media/'
    resumes = [str(item.cv) for item in resumes_data]
    print("resumes: ", resumes)
    resumes_new = [item.split(':')[0] for item in resumes]
    resumes_new = [item for item in resumes_new if item != '']

    LIST_OF_FILES = resumes_new

    print("Total Files to Parse\t", len(LIST_OF_FILES))
    print("####### PARSING ########")
    # Ordered_list_Resume stays index-aligned with Resumes: append a name only
    # when its text is successfully extracted.
    for indx, file in enumerate(LIST_OF_FILES):
        print(indx, file)
        if not pathlib.Path(filepath + file).is_file():
            continue

        ext = pathlib.Path(file).suffix.lower().lstrip('.')

        if ext == "pdf":
            try:
                with open(filepath + file, 'rb') as pdf_file:
                    read_pdf = PyPDF2.PdfReader(pdf_file, strict=False)
                    Temp_pdf = ''
                    for page in read_pdf.pages:
                        page_content = page.extract_text() or ''
                        page_content = page_content.replace('\n', ' ').replace('\f', '')
                        Temp_pdf += page_content
                    Temp_pdf = re.sub(r'\s+', ' ', Temp_pdf).strip()
                    if not Temp_pdf:
                        print("  " + file + ": no extractable text, skipped")
                        continue
                    Resumes.append(Temp_pdf)            # one entry per resume
                    Ordered_list_Resume.append(file)    # aligned name
            except Exception as e:
                print(e)

        elif ext in ("doc", "docx"):
            if textract is None:
                print("  " + file + ": .doc/.docx skipped (textract not installed)")
                continue
            try:
                a = textract.process(filepath + file)
                a = a.replace(b'\n', b' ').replace(b'\r', b' ')
                Resumes.append(str(a))
                Ordered_list_Resume.append(file)
            except Exception as e:
                print(e)

    print("Done Parsing.")
    return Resumes, Ordered_list_Resume


def get_rank(result_dict=None):

    if result_dict == None:
        return {}

    # KNN-score = cosine distance: lower = better match -> sort ASC, rank 1 = lowest
    new_result_dict = OrderedDict(sorted(result_dict.items(), key=lambda item: getitem(item[1], 'score'), reverse=False))
    new_updated_result_dict = {}
    indx = 0
    for _, item in new_result_dict.items():
        item['rank'] = indx + 1
        new_updated_result_dict[indx] = item
        indx += 1
    return new_updated_result_dict


def show_rank(result_dict=None, jobfileName='job1', top_k=20):
    if (result_dict == None):
        filepath = 'result/' + jobfileName + '.json'
        result_dict = readResultInJson(filepath)
    print("\nResult:")
    for _, result in result_dict.items():
        print(f"Rank: {result['rank']}\t KNN-score:{round(result['score'], 5)} (cosine distance, lower=better) \tName:{result['name']}")


# start parsing
# result
def res(resumes_data, job_data):
    result_arr = dict()
    print("Resumes: ", resumes_data.values('cv'))

    # checking basic requirements
    Resumes, Ordered_list_Resume = check_basicRequirement(resumes_data, job_data)

    if not Ordered_list_Resume or not Resumes:
        return result_arr

    # build + normalize the job description text
    job_desc = job_data.details + '\n' + job_data.responsibilities + '\n' + job_data.experience + '\n'
    job_desc = re.sub(r' +', ' ', job_desc.replace('\n', '').replace('\r', ''))
    try:
        job_text = ' '.join(normalize(word_tokenize(str(job_desc))))
    except Exception:
        job_text = ''
    print("\nNormalized Job Description:\n", job_text)

    if not job_text.strip():
        print("Job description has no usable keywords; nothing to rank.")
        return result_arr

    # normalize each resume, keep names index-aligned
    resume_texts = []
    resume_names = []
    for text, name in zip(Resumes, Ordered_list_Resume):
        try:
            norm = ' '.join(normalize(word_tokenize(str(text))))
        except Exception:
            norm = ''
        resume_texts.append(norm)
        resume_names.append(name)

    # ONE TF-IDF model over job + all resumes (shared vocab + real IDF),
    # then cosine similarity of each resume to the job description.
    corpus = [job_text] + resume_texts
    vectorizer = TfidfVectorizer(stop_words='english')
    try:
        tfidf = vectorizer.fit_transform(corpus)
    except ValueError:
        print("Empty vocabulary after normalization; nothing to rank.")
        return result_arr

    # KNN (K-Nearest Neighbour) document similarity: distance of each resume
    # to the job description using cosine metric -> KNN-score (lower = better).
    job_vec = tfidf[0]
    resume_matrix = tfidf[1:]
    neigh = NearestNeighbors(n_neighbors=1, metric='cosine')
    neigh.fit(job_vec)  # single reference point = job description
    distances = neigh.kneighbors(resume_matrix)[0][:, 0]

    result_arr = {indx: {'name': name, 'score': float(distances[indx])}
                  for indx, name in enumerate(resume_names)}

    result_arr = get_rank(result_arr)
    show_rank(result_arr)

    # return resultant shortlist
    return result_arr
