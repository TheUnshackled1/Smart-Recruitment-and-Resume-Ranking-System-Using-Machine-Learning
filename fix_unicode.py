import sys
with open('generate_test_cv.py', 'r', encoding='utf-8') as f:
    content = f.read()
replacements = [
    ('\u2190', '<--'),
    ('\u2014', '--'),
    ('\u2013', '-'),
    ('\u2019', "'"),
    ('\u2018', "'"),
    ('\u2022', '-'),
    ('\u00e2\u20ac\u201c', '-'),
]
for old, new in replacements:
    content = content.replace(old, new)
with open('generate_test_cv.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done - unicode chars replaced')
