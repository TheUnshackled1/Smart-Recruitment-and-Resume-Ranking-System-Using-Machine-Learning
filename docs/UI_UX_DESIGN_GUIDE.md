# UI/UX Design Guide — Smart Recruitment System

**Professional + Innovative Aesthetic**
**Navy (#001F3F) + Teal (#00D9FF) Design System**
**Based on UI/UX Pro Max Principles**

---

## Table of Contents

1. [Design System Overview](#design-system-overview)
2. [Priority-Based Rules](#priority-based-rules)
3. [Component Library](#component-library)
4. [Color & Typography](#color--typography)
5. [Stack Guidelines](#stack-guidelines)
6. [Common Patterns](#common-patterns)
7. [Anti-Patterns](#anti-patterns)
8. [Pre-Delivery Checklist](#pre-delivery-checklist)
9. [Search Reference](#search-reference)
10. [Implementation Guide](#implementation-guide)

---

## Design System Overview

### Design System Identity

| Aspect | Value | Purpose |
|--------|-------|---------|
| **Aesthetic** | Professional + Innovative | Trustworthy + Forward-thinking |
| **Primary Color** | Navy #001F3F | Authority, stability, trust |
| **Accent Color** | Teal #00D9FF | Innovation, energy, action |
| **Display Font** | Poppins | Bold, geometric, modern |
| **Body Font** | Inter | Clean, readable, technical |
| **Motion Speed** | 0.3s ease-out (base) | Responsive, professional |

### Design Tokens

All values are CSS variables in `design-system.css` for easy customization.

```css
/* Colors */
--color-navy: #001F3F
--color-dark-navy: #000F1F
--color-teal: #00D9FF
--color-light-teal: #B3F1FF
--color-dark-text: #2C3E50
--color-medium-text: #55606B
--color-light-text: #7F8C8D
--color-white: #FFFFFF
--color-light-grey: #ECF0F1
--color-lighter-grey: #F8F9FA
--color-border: #E0E0E0

/* Typography */
--font-display: 'Poppins', sans-serif
--font-body: 'Inter', sans-serif
--text-h1: 2.5rem
--text-h2: 2rem
--text-h3: 1.5rem
--text-body: 1rem
--text-small: 0.875rem

/* Spacing (8-step system) */
--spacing-xs: 0.5rem
--spacing-sm: 1rem
--spacing-md: 1.5rem
--spacing-lg: 2rem
--spacing-xl: 3rem
--spacing-2xl: 4rem
--spacing-3xl: 6rem

/* Motion */
--transition-fast: 0.2s ease-out
--transition-base: 0.3s ease-out
--transition-slow: 0.5s ease-out

/* Shadows */
--shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.08)
--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.12)
--shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.15)
--shadow-xl: 0 12px 40px rgba(0, 0, 0, 0.2)
```

---

## Priority-Based Rules

### 1. Accessibility (CRITICAL)

Minimum requirements for accessible recruitment platform.

#### Color Contrast ✅

| Context | Ratio | Requirement | Check |
|---------|-------|-------------|-------|
| **Body text on white** | 7.5:1 | WCAG AAA | Dark text (#2C3E50) on white |
| **Button text** | 5.5:1 | WCAG AAA | Teal bg + Navy text or Navy bg + Teal text |
| **Muted text** | 4.5:1 | WCAG AA | Light grey (#7F8C8D) minimum for secondary text |
| **Form labels** | 7:1 | WCAG AAA | Navy text (#001F3F) on light backgrounds |

**Implementation:**
```html
<!-- ✅ GOOD: 7.5:1 contrast -->
<p class="text-dark-text">Body text on white</p>

<!-- ❌ BAD: Insufficient contrast -->
<p class="text-light-text">Muted text (only 4.5:1)</p>
```

#### Focus States 🎯

All interactive elements must have visible focus rings.

```css
/* Form controls */
.form-control:focus {
  border-color: var(--color-teal);
  box-shadow: 0 0 0 3px rgba(0, 217, 255, 0.1);
  outline: none;
}

/* Buttons */
.btn:focus {
  outline: 2px solid var(--color-teal);
  outline-offset: 2px;
}

/* Links */
a:focus {
  outline: 2px solid var(--color-navy);
  outline-offset: 2px;
}
```

#### Form Accessibility 📝

```html
<!-- ✅ GOOD: Proper label association -->
<label for="job-title">Job Title</label>
<input id="job-title" type="text" class="form-control" />

<!-- ✅ GOOD: Aria-label for icon-only buttons -->
<button class="btn" aria-label="Search jobs">
  <span class="icon-search"></span>
</button>

<!-- ✅ GOOD: Error messages linked to input -->
<input id="email" aria-describedby="email-error" />
<span id="email-error" class="text-danger">Invalid email</span>

<!-- ❌ BAD: Missing label -->
<input type="text" placeholder="Job Title" />

<!-- ❌ BAD: No aria-label on icon button -->
<button class="btn"><span class="icon-search"></span></button>
```

#### Keyboard Navigation ⌨️

- Tab order follows visual order (left-to-right, top-to-bottom)
- Skip to main content link available
- All functionality accessible via keyboard
- No keyboard traps (elements can be tabbed out of)

```html
<!-- ✅ GOOD: Logical tab order -->
<header>
  <nav>
    <a href="#main">Skip to main content</a>
    <a href="/jobs">Browse Jobs</a>
    <a href="/login">Log In</a>
  </nav>
</header>

<main id="main">
  <input type="text" placeholder="Search..." />
  <button>Search</button>
</main>
```

#### Alt Text & ARIA 🖼️

```html
<!-- ✅ GOOD: Meaningful alt text -->
<img src="hero.jpg" alt="Professional working at recruitment platform" />

<!-- ✅ GOOD: Hidden decorative images -->
<img src="decoration.svg" alt="" aria-hidden="true" />

<!-- ✅ GOOD: ARIA labels for complex widgets -->
<div aria-label="Job filters" role="group">
  <input type="checkbox" /> Full-time
</div>

<!-- ❌ BAD: Vague alt text -->
<img src="logo.png" alt="image" />

<!-- ❌ BAD: No alt text -->
<img src="important-chart.png" />
```

---

### 2. Touch & Interaction (CRITICAL)

Optimize for cursor and touch interactions.

#### Touch Target Size 👆

All clickable elements must be minimum 44x44px (WCAG 2.5.5).

```css
/* ✅ GOOD: 44x44px minimum */
.btn {
  padding: 0.75rem 1.5rem;  /* Creates ~44px height */
  min-width: 44px;
  min-height: 44px;
}

.icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ❌ BAD: Too small */
.icon-button {
  width: 24px;  /* Too small for touch */
  height: 24px;
}
```

#### Cursor Pointer 🖱️

All interactive elements must show hand cursor.

```html
<!-- ✅ GOOD: Interactive element with cursor pointer -->
<div class="cursor-pointer hover-lift">
  <h3>Job Title</h3>
  <p>Company Name</p>
</div>

<!-- ✅ GOOD: Button inherits pointer -->
<button class="btn btn-primary">Apply Now</button>

<!-- ❌ BAD: Clickable div without cursor -->
<div onclick="handleClick()">
  Click me
</div>

<!-- ✅ FIX: Add cursor-pointer -->
<div class="cursor-pointer" onclick="handleClick()">
  Click me
</div>
```

#### Hover vs Tap 🎨

Use distinct interactions for desktop and mobile.

```css
/* ✅ GOOD: Hover effect on desktop (not on mobile) */
@media (hover: hover) {
  .card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
  }
}

/* ✅ GOOD: Active state on touch */
.card:active {
  opacity: 0.95;
}

/* ❌ BAD: Only hover, no feedback on touch */
.card:hover {
  background-color: var(--color-light-grey);
}
```

#### Loading States ⏳

Always disable button during async operations.

```html
<!-- ✅ GOOD: Disabled state during submission -->
<button id="apply-btn" class="btn btn-primary">Apply Now</button>

<script>
  document.getElementById('apply-btn').addEventListener('click', async () => {
    const btn = event.target;
    btn.disabled = true;
    btn.textContent = 'Applying...';

    try {
      await submitApplication();
      btn.textContent = 'Applied!';
    } catch (error) {
      btn.disabled = false;
      btn.textContent = 'Apply Now';
      showError(error.message);
    }
  });
</script>

<!-- ❌ BAD: No disabled state, multiple clicks possible -->
<button class="btn btn-primary" id="apply-btn">Apply Now</button>
```

#### Error Feedback 🚨

Clear error messages instantly near the problem.

```html
<!-- ✅ GOOD: Error at field level with clear message -->
<div class="form-group">
  <label for="email">Email Address</label>
  <input
    id="email"
    type="email"
    class="form-control border-danger"
    aria-describedby="email-error"
  />
  <span id="email-error" class="text-danger text-small mt-1">
    Please enter a valid email address
  </span>
</div>

<!-- ❌ BAD: Generic error message at top of form -->
<div class="alert alert-danger">Error submitting form</div>

<!-- ❌ BAD: No error feedback -->
<input type="email" />
```

---

### 3. Performance (HIGH)

Optimize animations and rendering.

#### Image Optimization 🖼️

```html
<!-- ✅ GOOD: WebP with JPG fallback -->
<picture>
  <source srcset="hero.webp" type="image/webp" />
  <img src="hero.jpg" alt="Hero background" />
</picture>

<!-- ✅ GOOD: Lazy loading with srcset -->
<img
  src="job-card-small.jpg"
  srcset="job-card-medium.jpg 768w, job-card-large.jpg 1024w"
  loading="lazy"
  alt="Job listing"
/>

<!-- ❌ BAD: Large unoptimized image -->
<img src="huge-uncompressed.png" alt="Hero" />

<!-- ❌ BAD: No srcset for responsive images -->
<img src="image.jpg" alt="Job" />
```

#### Reduced Motion 🎬

Always respect `prefers-reduced-motion` preference.

```css
/* ✅ GOOD: Respect user preference */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

/* Animation continues to work but instant for users who want it */
```

#### Content Jumping 📍

Reserve space for async-loaded content.

```html
<!-- ✅ GOOD: Reserved space for image -->
<div class="aspect-video">
  <img src="job-image.jpg" alt="Company office" loading="lazy" />
</div>

<!-- ✅ GOOD: Skeleton screen while loading -->
<div class="animate-pulse">
  <div class="h-4 bg-gray-200 rounded mb-2"></div>
  <div class="h-4 bg-gray-200 rounded w-5/6"></div>
</div>

<!-- ❌ BAD: Image loads, shifts layout -->
<img src="job-image.jpg" alt="Company office" />

<!-- ❌ BAD: No loading state, content appears suddenly -->
<div id="content"></div>
<script>
  fetch('/api/jobs')
    .then(r => r.json())
    .then(data => {
      document.getElementById('content').innerHTML = renderJobs(data);
    });
</script>
```

#### Animation Performance ⚡

Use GPU-accelerated transforms, not layout properties.

```css
/* ✅ GOOD: GPU-accelerated (fast) */
.card:hover {
  transform: translateY(-4px);  /* GPU accelerated */
  opacity: 0.95;                /* GPU accelerated */
}

/* ❌ BAD: Causes layout recalculation (slow) */
.card:hover {
  width: 105%;        /* Reflow */
  height: auto;       /* Reflow */
  padding: 20px;      /* Reflow */
  margin-bottom: 10px;/* Reflow */
}

/* Better: Just use transform */
.card:hover {
  transform: scale(1.02);  /* No reflow */
}
```

---

### 4. Layout & Responsive (HIGH)

Ensure proper scaling across devices.

#### Viewport Meta Tag ✅

```html
<!-- ✅ REQUIRED in base.html <head> -->
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />

<!-- ❌ WRONG: No viewport meta -->
<!-- Content won't scale on mobile -->
```

#### Readable Font Size 📖

Minimum 16px body text on mobile (no zoom required).

```html
<!-- ✅ GOOD: Readable on mobile -->
<p class="text-base">Job description</p>  <!-- 1rem = 16px -->

<!-- ❌ BAD: Too small on mobile -->
<p class="text-xs">Job description</p>  <!-- 0.75rem = 12px -->
```

#### No Horizontal Scroll 📱

Content must fit viewport width at all breakpoints.

```html
<!-- ✅ GOOD: Responsive containers -->
<div class="container mx-auto px-4">
  <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
    <!-- Content scales with viewport -->
  </div>
</div>

<!-- ❌ BAD: Fixed width larger than viewport -->
<div style="width: 1200px;">
  <!-- Causes horizontal scroll on mobile -->
</div>
```

#### Z-Index Management 🎯

Use defined scale to prevent stacking context conflicts.

```css
/* ✅ GOOD: Defined z-index scale */
:root {
  --z-dropdown: 100;      /* Dropdowns above content */
  --z-sticky: 500;        /* Sticky headers above dropdowns */
  --z-fixed: 1000;        /* Fixed nav above sticky */
  --z-modal: 1500;        /* Modals above everything */
  --z-tooltip: 1700;      /* Tooltips on top */
}

.dropdown { z-index: var(--z-dropdown); }
.sticky-header { z-index: var(--z-sticky); }
.fixed-nav { z-index: var(--z-fixed); }
.modal { z-index: var(--z-modal); }
.tooltip { z-index: var(--z-tooltip); }

/* ❌ BAD: Random z-index values */
.dropdown { z-index: 50; }
.modal { z-index: 100; }
.tooltip { z-index: 60; }  /* Tooltip below modal! */
```

---

### 5. Typography & Color (MEDIUM)

Professional and readable type system.

#### Line Height & Length 📝

- **Line height:** 1.5–1.75 for body text
- **Line length:** 65–75 characters per line (optimal reading)

```css
/* ✅ GOOD: Optimal typography */
.prose {
  line-height: 1.6;
  max-width: 65ch;  /* ~70 characters */
}

body {
  font-family: var(--font-body);
  font-size: 1rem;
  line-height: 1.6;
}

/* ❌ BAD: Hard to read */
.description {
  line-height: 1.2;  /* Too tight */
  max-width: 100%;   /* Too wide */
}
```

#### Font Pairing 🔤

**Display:** Poppins (bold, geometric, modern)
**Body:** Inter (clean, readable, technical)

```html
<!-- ✅ GOOD: Font hierarchy -->
<h1 class="font-display font-extrabold text-h1">
  Find Your Dream Job
</h1>

<p class="font-body font-normal text-body">
  Explore thousands of job opportunities with all the information you need.
</p>

<!-- ❌ BAD: Same font for heading and body -->
<h1>Find Your Dream Job</h1>
<p>Explore thousands of job opportunities...</p>
```

#### Color Semantics 🎨

| Meaning | Color | Use Case |
|---------|-------|----------|
| **Primary Action** | Teal #00D9FF | Main buttons, call-to-action |
| **Brand/Trust** | Navy #001F3F | Navigation, headers, primary text |
| **Success** | Green #27AE60 | Confirmations, applied, verified |
| **Warning** | Orange #F39C12 | Alerts, pending actions |
| **Danger/Error** | Red #E74C3C | Errors, critical actions |
| **Information** | Blue #3498DB | Tips, helpful information |

```html
<!-- ✅ GOOD: Semantic colors -->
<button class="btn btn-primary">Apply (Teal = Action)</button>
<button class="btn btn-secondary">Save (Navy = Secondary)</button>
<span class="badge badge-success">Applied (Green = Success)</span>
<span class="badge badge-warning">Pending (Orange = Warning)</span>

<!-- ❌ BAD: Using colors incorrectly -->
<button class="bg-green-500">Apply (Wrong - green for success, not action)</button>
<button class="bg-red-500">Save (Wrong - red for danger, not secondary)</button>
```

---

### 6. Animation (MEDIUM)

Smooth, purposeful motion.

#### Duration & Timing 🎬

| Interaction | Duration | Timing | Purpose |
|-------------|----------|--------|---------|
| **Micro-interaction** | 150–200ms | ease-out | Button hover, small shifts |
| **Standard transition** | 300ms | ease-out | Page transitions, modal open |
| **Large animation** | 500ms+ | ease-out | Page load reveals, complex sequences |

```css
/* ✅ GOOD: Appropriate timing */
.btn:hover {
  transition: all 0.2s ease-out;  /* Fast for immediate feedback */
}

.modal {
  animation: slideInUp 0.3s ease-out;  /* Standard for modal entrance */
}

.hero-title {
  animation: slideDown 0.6s ease-out;  /* Slower for dramatic reveal */
}

/* ❌ BAD: Too slow or inconsistent */
.btn:hover {
  transition: all 1s ease-in;  /* Way too slow for button hover */
}
```

#### Transform vs Layout 🚀

Always use `transform` and `opacity`, never animate layout properties.

```css
/* ✅ GOOD: GPU-accelerated */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(20px);  /* GPU accelerated */
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* ❌ BAD: Causes jank (layout reflow) */
@keyframes badSlide {
  from {
    bottom: -100px;      /* Reflow */
    position: relative;  /* Reflow */
  }
  to {
    bottom: 0;
  }
}
```

#### Loading States 🔄

Provide visual feedback during async operations.

```html
<!-- ✅ GOOD: Skeleton screen -->
<div class="animate-pulse">
  <div class="h-4 bg-gray-200 rounded mb-2"></div>
  <div class="h-4 bg-gray-200 rounded w-5/6"></div>
</div>

<!-- ✅ GOOD: Spinner for indeterminate loading -->
<div class="spinner"></div>

<!-- ✅ GOOD: Progress bar for determinate loading -->
<div class="progress">
  <div class="progress-bar" style="width: 65%"></div>
</div>

<!-- ❌ BAD: No loading state -->
<div id="content"></div>  <!-- Blank until data loads -->
```

---

### 7. Style Selection (MEDIUM)

Match style to product and audience.

#### Smart Recruitment Style 🎯

| Aspect | Choice | Reason |
|--------|--------|--------|
| **Primary Style** | Professional + Minimalist | Trust for recruiters, clarity for seekers |
| **Color Palette** | Navy + Teal | Corporate + Innovation |
| **Typography** | Poppins + Inter | Modern without being trendy |
| **Borders** | Soft, 4px navy left | Emphasis without harshness |
| **Shadows** | Subtle depth | Professional, not dramatic |
| **Spacing** | Generous | Breathing room, premium feel |

#### Consistency ✅

Use same style across all pages and components.

```html
<!-- ✅ GOOD: Consistent button style -->
<button class="btn btn-primary">Primary (Teal bg, Navy text)</button>
<button class="btn btn-primary">All buttons same style</button>
<button class="btn btn-primary">No variations</button>

<!-- ❌ BAD: Inconsistent button styles -->
<button class="btn btn-blue">Primary button</button>
<button class="btn bg-green-500 text-white">Another button</button>
<button style="background: #ff0000; color: white;">Yet another</button>
```

#### No Emoji Icons ⛔

Never use emoji as UI icons. Use SVG from icon libraries.

```html
<!-- ✅ GOOD: SVG icons (Heroicons, Lucide, etc.) -->
<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
</svg>

<!-- ❌ BAD: Emoji as icon -->
🔍 Search
📌 Pin
❌ Delete
⭐ Star
🎯 Target
```

Why? Emojis are:
- Inconsistent across browsers and devices
- Not accessible (no alt text support)
- Unprofessional for business apps
- Vary in size and appearance

---

### 8. Charts & Data (LOW)

Match chart type to data and audience.

#### Chart Type Selection 📊

| Data Type | Best Chart | Example |
|-----------|-----------|---------|
| **Trend over time** | Line / Area | Job postings per week |
| **Part-to-whole** | Pie / Doughnut | Application status breakdown |
| **Comparison** | Bar / Column | Salaries by role |
| **Distribution** | Histogram | Applications per day range |
| **Correlation** | Scatter | Experience vs salary |
| **Composition** | Stacked Bar | Applicants by source |
| **Ranking** | Horizontal Bar | Top 10 job categories |

#### Color in Charts 🎨

Use accessible color palettes for charts.

```javascript
// ✅ GOOD: Accessible chart colors
const chartColors = [
  '#001F3F',  // Navy (primary)
  '#00D9FF',  // Teal (accent)
  '#27AE60',  // Green (success)
  '#F39C12',  // Orange (warning)
  '#E74C3C',  // Red (danger)
];

// ❌ BAD: Hard to distinguish
const chartColors = [
  '#FF0000', '#00FF00', '#0000FF',  // Too bright/saturated
];

// ❌ BAD: Red-green only (colorblind issues)
const chartColors = [
  '#FF0000', '#00FF00',  // 8% of men can't distinguish
];
```

#### Data Tables 📋

Always provide table alternative for accessibility.

```html
<!-- ✅ GOOD: Proper table markup -->
<table role="table" aria-label="Job applications">
  <thead>
    <tr>
      <th scope="col">Job Title</th>
      <th scope="col">Applications</th>
      <th scope="col">Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Senior Developer</td>
      <td>45</td>
      <td>Open</td>
    </tr>
  </tbody>
</table>

<!-- ✅ GOOD: Responsive table for mobile -->
<div class="overflow-x-auto">
  <table class="w-full"><!-- Table content --></table>
</div>

<!-- ❌ BAD: Chart only, no table alternative -->
<canvas id="chart"></canvas>
<!-- No accessible data representation -->
```

---

## Component Library

### Buttons

```html
<!-- Primary Button (Teal) -->
<button class="btn btn-primary">
  <span class="icon-search mr-2"></span>Search Jobs
</button>

<!-- Secondary Button (Navy) -->
<button class="btn btn-secondary">
  Save Job
</button>

<!-- Danger Button (Red) -->
<button class="btn btn-danger">
  Delete Application
</button>

<!-- Disabled State -->
<button class="btn btn-primary" disabled>
  Applying...
</button>

<!-- Size Variants -->
<button class="btn btn-primary btn-lg">Large Button</button>
<button class="btn btn-primary btn-sm">Small Button</button>

<!-- Icon Button (44x44px) -->
<button class="btn btn-icon" aria-label="Search">
  <span class="icon-search"></span>
</button>
```

**CSS:**
```css
.btn {
  font-family: var(--font-display);
  font-weight: var(--weight-semibold);
  border-radius: var(--radius-md);
  padding: 0.75rem 1.5rem;
  font-size: var(--text-body);
  transition: all var(--transition-base);
  border: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 44px;
  min-width: 44px;
}

.btn-primary {
  background-color: var(--color-teal);
  color: var(--color-navy);
  border: 2px solid var(--color-teal);
}

.btn-primary:hover {
  background-color: var(--color-navy);
  color: var(--color-teal);
  border-color: var(--color-navy);
}

.btn-secondary {
  background-color: transparent;
  color: var(--color-navy);
  border: 2px solid var(--color-navy);
}

.btn-secondary:hover {
  background-color: var(--color-navy);
  color: var(--color-white);
}

.btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}
```

### Cards

```html
<!-- Job Card -->
<div class="card hover-lift">
  <div class="card-header">
    <h3 class="card-title">Senior Developer</h3>
    <span class="badge badge-primary">Full-time</span>
  </div>
  <div class="card-body">
    <p class="text-medium-text">TechCorp</p>
    <p class="text-light-text">San Francisco, CA</p>
    <p class="mt-3">Build innovative web applications...</p>
  </div>
  <div class="card-footer">
    <button class="btn btn-primary btn-sm">Apply Now</button>
  </div>
</div>
```

**CSS:**
```css
.card {
  border: none;
  border-left: 4px solid var(--color-navy);
  border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
  transition: all var(--transition-base);
  overflow: hidden;
  background-color: var(--color-white);
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-lg);
  border-left-color: var(--color-teal);
}

.card-header {
  background-color: var(--color-lighter-grey);
  border-bottom: 1px solid var(--color-border);
  padding: var(--spacing-lg);
  display: flex;
  justify-content: space-between;
  align-items: start;
}

.card-title {
  font-family: var(--font-display);
  font-weight: var(--weight-bold);
  color: var(--color-navy);
  margin: 0;
}

.card-body {
  padding: var(--spacing-lg);
}

.card-footer {
  padding: var(--spacing-lg);
  background-color: var(--color-lighter-grey);
  border-top: 1px solid var(--color-border);
}
```

### Forms

```html
<!-- Form Group -->
<div class="form-group">
  <label for="job-title" class="form-label">Job Title</label>
  <input
    id="job-title"
    type="text"
    class="form-control"
    placeholder="e.g., Senior Developer"
    aria-describedby="job-title-help"
  />
  <small id="job-title-help" class="form-text text-light-text">
    Enter the job title you're searching for
  </small>
</div>

<!-- Textarea -->
<div class="form-group">
  <label for="description" class="form-label">Description</label>
  <textarea
    id="description"
    class="form-control"
    rows="4"
    placeholder="Job description..."
  ></textarea>
</div>

<!-- Select -->
<div class="form-group">
  <label for="employment" class="form-label">Employment Type</label>
  <select id="employment" class="form-control">
    <option value="">Select employment type</option>
    <option value="full-time">Full-time</option>
    <option value="part-time">Part-time</option>
    <option value="contract">Contract</option>
  </select>
</div>

<!-- Form with Error -->
<div class="form-group">
  <label for="email" class="form-label">Email Address</label>
  <input
    id="email"
    type="email"
    class="form-control border-danger"
    aria-describedby="email-error"
  />
  <span id="email-error" class="form-error text-danger text-small mt-1">
    Please enter a valid email address
  </span>
</div>
```

**CSS:**
```css
.form-group {
  margin-bottom: var(--spacing-lg);
}

.form-label {
  display: block;
  font-weight: var(--weight-semibold);
  color: var(--color-dark-text);
  margin-bottom: var(--spacing-sm);
  font-size: var(--text-body);
}

.form-control {
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 0.75rem 1rem;
  font-family: var(--font-body);
  font-size: var(--text-body);
  color: var(--color-dark-text);
  transition: all var(--transition-base);
  width: 100%;
  background-color: var(--color-white);
}

.form-control::placeholder {
  color: var(--color-light-text);
}

.form-control:focus {
  border-color: var(--color-teal);
  box-shadow: 0 0 0 3px rgba(0, 217, 255, 0.1);
  outline: none;
}

.form-control.border-danger {
  border-color: var(--color-danger);
}

.form-text {
  display: block;
  margin-top: 0.25rem;
  color: var(--color-light-text);
  font-size: var(--text-small);
}

.form-error {
  color: var(--color-danger);
  display: block;
  margin-top: 0.25rem;
}
```

### Navigation

```html
<!-- Navbar -->
<header class="site-navbar">
  <div class="container-fluid">
    <div class="navbar-content">
      <!-- Logo -->
      <div class="navbar-logo">
        <a href="/" class="logo-text">Smart Recruitment</a>
      </div>

      <!-- Navigation -->
      <nav class="navbar-nav">
        <a href="/jobs" class="nav-link">Browse Jobs</a>
        <a href="/companies" class="nav-link">Companies</a>
        <a href="/about" class="nav-link">About</a>
      </nav>

      <!-- Auth Links -->
      <div class="navbar-auth">
        <a href="/login" class="nav-link">Log In</a>
        <button class="btn btn-primary">Sign Up</button>
      </div>
    </div>
  </div>
</header>
```

**CSS:**
```css
.site-navbar {
  background: linear-gradient(180deg, var(--color-navy), var(--color-dark-navy));
  padding: var(--spacing-md) 0;
  position: sticky;
  top: 0;
  z-index: var(--z-fixed);
}

.navbar-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--spacing-lg);
}

.navbar-logo a {
  font-size: 1.5rem;
  font-weight: 800;
  color: var(--color-white);
  font-family: var(--font-display);
  letter-spacing: 0.05em;
}

.navbar-nav {
  display: flex;
  gap: var(--spacing-lg);
}

.nav-link {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: color var(--transition-base);
  cursor: pointer;
}

.nav-link:hover,
.nav-link:focus {
  color: var(--color-teal);
  outline: 2px solid var(--color-teal);
  outline-offset: 2px;
}

.navbar-auth {
  display: flex;
  gap: var(--spacing-md);
  align-items: center;
}
```

### Badges

```html
<!-- Primary Badge -->
<span class="badge badge-primary">Full-time</span>

<!-- Secondary Badge -->
<span class="badge badge-secondary">Recommended</span>

<!-- Success Badge -->
<span class="badge badge-success">Applied</span>

<!-- Warning Badge -->
<span class="badge badge-warning">Closing Soon</span>

<!-- Danger Badge -->
<span class="badge badge-danger">Expired</span>
```

**CSS:**
```css
.badge {
  font-family: var(--font-display);
  font-weight: var(--weight-semibold);
  border-radius: var(--radius-full);
  padding: 0.35rem 0.75rem;
  font-size: var(--text-small);
  display: inline-block;
}

.badge-primary {
  background-color: var(--color-navy);
  color: var(--color-white);
}

.badge-secondary {
  background-color: var(--color-teal);
  color: var(--color-navy);
}

.badge-success {
  background-color: var(--color-success);
  color: var(--color-white);
}

.badge-warning {
  background-color: var(--color-warning);
  color: var(--color-white);
}

.badge-danger {
  background-color: var(--color-danger);
  color: var(--color-white);
}
```

---

## Color & Typography

### Color Palette Reference

**Primary Colors:**
```
Navy         #001F3F - Trust, authority, primary
Dark Navy    #000F1F - Darker variant for depth
Teal         #00D9FF - Innovation, energy, CTA
Light Teal   #B3F1FF - Teal tint for backgrounds
```

**Neutral Colors:**
```
Dark Text     #2C3E50 - Primary text, headings
Medium Text   #55606B - Secondary text
Light Text    #7F8C8D - Tertiary text, disabled
White         #FFFFFF - Pure backgrounds
Light Grey    #ECF0F1 - Backgrounds, sections
Lighter Grey  #F8F9FA - Subtle backgrounds
Border        #E0E0E0 - Dividers, borders
```

**Semantic Colors:**
```
Success  #27AE60 - Confirmations, approved
Warning  #F39C12 - Alerts, attention
Danger   #E74C3C - Errors, critical
Info     #3498DB - Information, helpful
```

### Typography System

**Heading Scale:**
```
h1  2.5rem / 40px  - Page title, hero
h2  2rem   / 32px  - Section header
h3  1.5rem / 24px  - Subsection
h4  1.25rem/ 20px  - Small heading
h5  1.125rem/18px  - Tiny heading
h6  1rem   / 16px  - Smallest heading
```

**Body Text:**
```
Body    1rem     / 16px  - Normal text
Small   0.875rem / 14px  - Labels, captions
Tiny    0.75rem  / 12px  - Metadata, timestamps
```

**Font Weights:**
```
Thin        300  - Not commonly used
Normal      400  - Body text, regular
Medium      500  - Emphasized text
Semibold    600  - Secondary headers, labels
Bold        700  - Headings, emphasis
Extrabold   800  - Primary headings (h1, h2)
```

---

## Stack Guidelines

### HTML/Tailwind (Current Stack)

**Best Practices:**

1. **Use CSS Variables:** Reference design-system.css variables
```html
<!-- ✅ GOOD -->
<button class="bg-navy text-white hover:bg-teal hover:text-navy">
  Search
</button>

<!-- ✅ GOOD: Using CSS vars directly -->
<div style="background-color: var(--color-navy);">Content</div>
```

2. **Semantic HTML:** Use proper tags for accessibility
```html
<!-- ✅ GOOD -->
<header>...</header>
<nav>...</nav>
<main>...</main>
<article>...</article>
<aside>...</aside>
<footer>...</footer>

<!-- ❌ BAD -->
<div id="header">...</div>
<div class="nav">...</div>
```

3. **Accessibility First:**
```html
<!-- ✅ GOOD: Accessible form -->
<label for="search">Search Jobs</label>
<input id="search" type="text" placeholder="Job title..." />

<!-- ❌ BAD: Missing label -->
<input type="text" placeholder="Search..." />
```

4. **Image Optimization:**
```html
<!-- ✅ GOOD: Responsive images -->
<picture>
  <source srcset="hero-mobile.webp" media="(max-width: 768px)">
  <source srcset="hero.webp">
  <img src="hero.jpg" alt="Recruitment platform hero" />
</picture>

<!-- ❌ BAD: Large unoptimized image -->
<img src="hero-large-uncompressed.png" />
```

5. **Animation Classes:**
```html
<!-- ✅ GOOD: Use defined animation classes -->
<h1 class="animate-slide-down">Find Your Dream Job</h1>
<p class="animate-fade-in">Explore opportunities</p>

<!-- ❌ BAD: Inline animation -->
<h1 style="animation: custom-animation 1s;">Title</h1>
```

### React/Next.js

**Component Structure:**
```jsx
// ✅ GOOD: Breaks down into composable pieces
export function JobCard({ job }) {
  return (
    <article className="card hover-lift">
      <header className="card-header">
        <h3 className="card-title">{job.title}</h3>
        <span className="badge badge-primary">{job.type}</span>
      </header>
      <div className="card-body">
        <p className="text-medium-text">{job.company}</p>
        <p className="text-light-text">{job.location}</p>
      </div>
      <footer className="card-footer">
        <button className="btn btn-primary">Apply Now</button>
      </footer>
    </article>
  );
}
```

**Performance:**
- Use `React.memo()` for expensive card list renders
- Implement virtualization for large lists (1000+ items)
- Use `@next/image` for optimization
- Implement skeleton screens for loading states

### Vue

**Component Template:**
```vue
<template>
  <article class="card hover-lift">
    <header class="card-header">
      <h3 class="card-title">{{ job.title }}</h3>
      <span class="badge badge-primary">{{ job.type }}</span>
    </header>
    <div class="card-body">
      <p class="text-medium-text">{{ job.company }}</p>
      <p class="text-light-text">{{ job.location }}</p>
    </div>
    <footer class="card-footer">
      <button
        class="btn btn-primary"
        @click="applyJob(job.id)"
        :disabled="isApplying"
      >
        {{ isApplying ? 'Applying...' : 'Apply Now' }}
      </button>
    </footer>
  </article>
</template>

<script setup>
import { ref } from 'vue';

defineProps({ job: Object });
const isApplying = ref(false);

async function applyJob(jobId) {
  isApplying.value = true;
  try {
    await api.applyJob(jobId);
  } finally {
    isApplying.value = false;
  }
}
</script>
```

### Svelte

**Component:**
```svelte
<script>
  export let job;
  let isApplying = false;

  async function handleApply() {
    isApplying = true;
    try {
      await api.applyJob(job.id);
    } finally {
      isApplying = false;
    }
  }
</script>

<article class="card hover-lift">
  <header class="card-header">
    <h3 class="card-title">{job.title}</h3>
    <span class="badge badge-primary">{job.type}</span>
  </header>
  <div class="card-body">
    <p class="text-medium-text">{job.company}</p>
    <p class="text-light-text">{job.location}</p>
  </div>
  <footer class="card-footer">
    <button
      class="btn btn-primary"
      on:click={handleApply}
      disabled={isApplying}
    >
      {isApplying ? 'Applying...' : 'Apply Now'}
    </button>
  </footer>
</article>
```

### SwiftUI (Mobile)

**View:**
```swift
struct JobCardView: View {
  let job: Job
  @State var isApplying = false

  var body: some View {
    VStack(alignment: .leading, spacing: 12) {
      HStack {
        VStack(alignment: .leading) {
          Text(job.title)
            .font(.system(size: 18, weight: .bold))
            .foregroundColor(Color(#colorLiteral(red: 0, green: 0.31, blue: 0.25, alpha: 1))) // Navy

          Text(job.company)
            .font(.body)
            .foregroundColor(Color(#colorLiteral(red: 0.33, green: 0.43, blue:0.45, alpha: 1))) // Medium grey
        }

        Spacer()

        Badge(job.type)
      }

      Text(job.location)
        .font(.caption)
        .foregroundColor(Color(#colorLiteral(red: 0.5, green: 0.55, blue: 0.55, alpha: 1))) // Light grey

      Button(action: { handleApply() }) {
        Text(isApplying ? "Applying..." : "Apply Now")
          .font(.headline)
          .frame(maxWidth: .infinity)
          .padding()
          .foregroundColor(.white)
          .background(Color(#colorLiteral(red: 0, green: 0.85, blue: 1, alpha: 1))) // Teal
          .cornerRadius(8)
      }
      .disabled(isApplying)
    }
    .padding()
    .background(Color.white)
    .cornerRadius(12)
    .shadow(radius: 4)
  }
}
```

### React Native

**Component:**
```jsx
import { View, Text, TouchableOpacity, ActivityIndicator } from 'react-native';

export function JobCard({ job, onApply }) {
  const [isApplying, setIsApplying] = useLocalSearchParams();

  async function handleApply() {
    setIsApplying(true);
    try {
      await onApply(job.id);
    } finally {
      setIsApplying(false);
    }
  }

  return (
    <View style={styles.card}>
      <View style={styles.header}>
        <View>
          <Text style={styles.title}>{job.title}</Text>
          <Text style={styles.company}>{job.company}</Text>
        </View>
        <Badge label={job.type} />
      </View>

      <Text style={styles.location}>{job.location}</Text>

      <TouchableOpacity
        style={[styles.button, isApplying && styles.buttonDisabled]}
        onPress={handleApply}
        disabled={isApplying}
      >
        {isApplying ? (
          <ActivityIndicator color="#001F3F" />
        ) : (
          <Text style={styles.buttonText}>Apply Now</Text>
        )}
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#FFFFFF',
    borderLeftWidth: 4,
    borderLeftColor: '#001F3F',
    borderRadius: 12,
    padding: 16,
    marginBottom: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 3,
    elevation: 3,
  },
  // ... more styles
});
```

### Flutter

**Widget:**
```dart
class JobCard extends StatefulWidget {
  final Job job;
  final Function(String) onApply;

  const JobCard({
    required this.job,
    required this.onApply,
  });

  @override
  State<JobCard> createState() => _JobCardState();
}

class _JobCardState extends State<JobCard> {
  bool isApplying = false;

  void _handleApply() async {
    setState(() => isApplying = true);
    try {
      await widget.onApply(widget.job.id);
    } finally {
      setState(() => isApplying = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
        side: BorderSide(
          color: Color(0xFF001F3F),
          width: 4,
        ),
      ),
      child: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      widget.job.title,
                      style: TextStyle(
                        fontSize: 18,
                        fontWeight: FontWeight.bold,
                        color: Color(0xFF001F3F),
                      ),
                    ),
                    Text(
                      widget.job.company,
                      style: TextStyle(
                        fontSize: 14,
                        color: Color(0xFF55606B),
                      ),
                    ),
                  ],
                ),
                Chip(label: Text(widget.job.type)),
              ],
            ),
            SizedBox(height: 8),
            Text(
              widget.job.location,
              style: TextStyle(
                fontSize: 12,
                color: Color(0xFF7F8C8D),
              ),
            ),
            SizedBox(height: 12),
            SizedBox(
              width: double.infinity,
              child: ElevatedButton(
                onPressed: isApplying ? null : _handleApply,
                style: ElevatedButton.styleFrom(
                  backgroundColor: Color(0xFF00D9FF),
                  foregroundColor: Color(0xFF001F3F),
                ),
                child: isApplying
                    ? CircularProgressIndicator(
                        valueColor: AlwaysStoppedAnimation<Color>(
                          Color(0xFF001F3F),
                        ),
                      )
                    : Text('Apply Now'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
```

---

## Common Patterns

### Hero Section

```html
<section class="hero-section">
  <div class="hero-background">
    <div class="hero-overlay"></div>
  </div>

  <div class="container">
    <div class="hero-content">
      <h1 class="hero-title animate-slide-down">
        Find Your Dream Job
      </h1>
      <p class="hero-subtitle animate-fade-in">
        Explore thousands of job opportunities with all the information you need
      </p>

      <form class="hero-form animate-slide-up" method="get" action="{{ url('search') }}">
        <input type="text" name="title" placeholder="Job title..." />
        <input type="text" name="location" placeholder="Location..." />
        <select name="employment">
          <option>Employment type</option>
          <option>Full-time</option>
          <option>Part-time</option>
        </select>
        <button type="submit" class="btn btn-primary">Search Job</button>
      </form>
    </div>
  </div>
</section>
```

**CSS:**
```css
.hero-section {
  position: relative;
  min-height: 600px;
  display: flex;
  align-items: center;
  overflow: hidden;
}

.hero-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('hero.jpg');
  background-size: cover;
  background-position: center;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg,
    rgba(0, 31, 63, 0.75),
    rgba(0, 15, 31, 0.85)
  );
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  color: var(--color-white);
}

.hero-title {
  font-size: var(--text-h1);
  font-weight: var(--weight-extrabold);
  font-family: var(--font-display);
  margin-bottom: var(--spacing-md);
}

.hero-subtitle {
  font-size: 1.25rem;
  color: var(--color-light-teal);
  margin-bottom: var(--spacing-xl);
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero-form {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: var(--spacing-md);
  max-width: 100%;
  margin-top: var(--spacing-lg);
}

@media (max-width: 768px) {
  .hero-form {
    grid-template-columns: 1fr;
    gap: var(--spacing-sm);
  }
}
```

### Job Listing Grid

```html
<section class="jobs-section">
  <div class="container">
    <h2 class="section-title">Latest Job Opportunities</h2>

    <div class="jobs-grid animate-stagger">
      {% for job in jobs %}
      <div class="scroll-target">
        <div class="card hover-lift">
          <div class="card-header">
            <div>
              <h3 class="card-title">{{ job.title }}</h3>
              <p class="text-medium-text">{{ job.company }}</p>
            </div>
            <span class="badge badge-primary">{{ job.type }}</span>
          </div>

          <div class="card-body">
            <p class="text-light-text mb-2">
              <span class="icon-location"></span>
              {{ job.location }}
            </p>
            <p>{{ job.description|truncatewords:20 }}</p>
          </div>

          <div class="card-footer">
            <a href="{% url 'job_detail' job.id %}" class="btn btn-sm btn-secondary">
              View Details
            </a>
            <button class="btn btn-sm btn-primary">Apply Now</button>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
```

**CSS:**
```css
.jobs-section {
  padding: var(--spacing-3xl) 0;
  background-color: var(--color-lighter-grey);
}

.section-title {
  font-size: var(--text-h2);
  font-weight: var(--weight-bold);
  font-family: var(--font-display);
  margin-bottom: var(--spacing-xl);
  color: var(--color-navy);
}

.jobs-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--spacing-lg);
}

@media (max-width: 768px) {
  .jobs-grid {
    grid-template-columns: 1fr;
  }
}
```

### Testimonials Section

```html
<section class="testimonials-section">
  <div class="container">
    <h2 class="section-title">Success Stories</h2>

    <div class="testimonials-grid">
      {% for testimonial in testimonials %}
      <div class="testimonial-card scroll-target animate-fade-in">
        <div class="stars">
          {% for i in "12345" %}
          <span class="icon-star-full"></span>
          {% endfor %}
        </div>

        <p class="testimonial-text">"{{ testimonial.text }}"</p>

        <div class="testimonial-author">
          <img src="{{ testimonial.avatar }}" alt="{{ testimonial.name }}" />
          <div>
            <p class="author-name">{{ testimonial.name }}</p>
            <p class="author-title">{{ testimonial.title }}</p>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
```

---

## Anti-Patterns

### ❌ Don't: Use Emoji as Icons

```html
<!-- BAD -->
🔍 Search
📌 Pin
❌ Delete
⭐ Star
🎯 Target

<!-- GOOD: Use SVG Icons -->
<svg class="icon" viewBox="0 0 24 24">
  <path d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
</svg>
```

Why? Emojis are:
- Unreliable across browsers/OS
- Not accessible (no text alternatives)
- Inconsistent sizing
- Unprofessional for business apps

**Solution:** Use icon libraries:
- **Heroicons** (official Tailwind icons)
- **Lucide** (modern, lightweight)
- **Font Awesome** (comprehensive)
- **Simple Icons** (brand logos)

### ❌ Don't: Use Color Alone to Convey Information

```html
<!-- BAD: Only color indicates status -->
<div class="bg-red-500">Application rejected</div>  <!-- Red = danger -->
<div class="bg-green-500">Application approved</div> <!-- Green = success -->

<!-- GOOD: Color + text + icon -->
<div class="badge badge-danger">
  <span class="icon-x-circle"></span> Rejected
</div>

<div class="badge badge-success">
  <span class="icon-check-circle"></span> Approved
</div>
```

Why? 8% of men are colorblind and can't distinguish red-green.

### ❌ Don't: Skip Accessibility

```html
<!-- BAD: No labels, no alt text -->
<input type="text" placeholder="Your name" />
<img src="company-logo.png" />

<!-- GOOD: Proper semantics -->
<label for="name">Your Name</label>
<input id="name" type="text" placeholder="Your name" />
<img src="company-logo.png" alt="Company name logo" />
```

### ❌ Don't: Animate Layout Properties

```css
/* BAD: Causes jank (layout reflows) */
@keyframes grow {
  from { width: 100px; height: 100px; }
  to { width: 150px; height: 150px; }
}

/* GOOD: GPU-accelerated */
@keyframes grow {
  from { transform: scale(1); }
  to { transform: scale(1.5); }
}
```

### ❌ Don't: Use Fixed Width on Mobile

```html
<!-- BAD: Horizontal scroll on mobile -->
<div style="width: 1200px;">
  Content
</div>

<!-- GOOD: Responsive -->
<div class="w-full max-w-7xl mx-auto">
  Content
</div>
```

### ❌ Don't: Forget Focus States

```css
/* BAD: No feedback on keyboard navigation */
.btn:hover { background: navy; }
.btn:focus { /* Missing! */ }

/* GOOD: Visible focus for keyboard users */
.btn:focus {
  outline: 2px solid var(--color-teal);
  outline-offset: 2px;
}
```

### ❌ Don't: Use Low-Contrast Text

```html
<!-- BAD: 2.5:1 contrast (fails WCAG AA) -->
<p style="color: #999; background: white;">Low contrast text</p>

<!-- GOOD: 7:1 contrast (WCAG AAA) -->
<p style="color: #2C3E50; background: white;">High contrast text</p>
```

### ❌ Don't: Make Touch Targets Too Small

```css
/* BAD: 24x24px (too small for touch) */
.icon-button {
  width: 24px;
  height: 24px;
}

/* GOOD: 44x44px minimum */
.icon-button {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

### ❌ Don't: Use Generic Naming

```html
<!-- BAD: Ambiguous -->
<button class="btn-1">Click Me</button>
<div class="box">Content</div>
<span class="text">Label</span>

<!-- GOOD: Semantic, descriptive -->
<button class="btn btn-primary">Apply Now</button>
<article class="job-card">Content</article>
<label>Job Title</label>
```

### ❌ Don't: Hide Important Information

```html
<!-- BAD: Information only on hover -->
<div title="Full job description">
  Job Title
</div>

<!-- GOOD: Always visible -->
<div class="card">
  <h3>Job Title</h3>
  <p>Full job description is visible</p>
</div>
```

---

## Pre-Delivery Checklist

Before shipping any UI changes, verify ALL items:

### ✅ Visual Quality

- [ ] No emojis used as icons (use SVG)
- [ ] All icons from a consistent set (Heroicons/Lucide)
- [ ] Logo is correct (verified from official source)
- [ ] Hover states don't cause layout shift
- [ ] Colors use CSS variables (not hardcoded hex)
- [ ] Typography hierarchy is clear (size + weight variation)
- [ ] Spacing is consistent (multiples of 8px)
- [ ] Shadows add depth (not flat appearance)
- [ ] Responsive preview looks good at 375px, 768px, 1440px

### ✅ Interaction & UX

- [ ] All clickable elements have `cursor-pointer`
- [ ] Hover states provide clear visual feedback
- [ ] Focus states are visible (keyboard navigation)
- [ ] Touch targets are minimum 44x44px
- [ ] Buttons show loading state during async operations
- [ ] Error messages appear near problem field
- [ ] Form placeholder text is not the label
- [ ] All interactive elements work on keyboard (Tab, Enter, Space)

### ✅ Light & Dark Mode

- [ ] Light mode text has 4.5:1+ contrast
- [ ] Dark mode backgrounds are >= #1F2937
- [ ] Borders are visible in both modes
- [ ] Glass/transparent elements readable in both
- [ ] Colors maintain accessibility in both modes

### ✅ Accessibility

- [ ] All images have meaningful alt text
- [ ] Form inputs have associated labels
- [ ] Buttons have aria-label if icon-only
- [ ] Color is not the only indicator (use icons + text)
- [ ] Focus order is logical (left-to-right, top-to-bottom)
- [ ] ARIA roles used correctly
- [ ] Page structure is semantic (header, nav, main, footer)
- [ ] Text can be zoomed to 200% without breaking

### ✅ Performance

- [ ] Images are optimized (WebP with fallback)
- [ ] Animations respect `prefers-reduced-motion`
- [ ] No layout reflows during animations
- [ ] Animations are smooth (60fps on phone)
- [ ] CSS animations (not JS when possible)
- [ ] No console warnings/errors
- [ ] Page load time is acceptable (<3s)

### ✅ Code Quality

- [ ] CSS uses design system variables
- [ ] No inline styles (use classes)
- [ ] BEM or similar naming conventions
- [ ] DRY principle applied (no duplication)
- [ ] Responsive classes used correctly
- [ ] No hardcoded colors
- [ ] No pixel-perfect hacks

### ✅ Components

- [ ] Buttons follow button styles exactly
- [ ] Cards use proper card component
- [ ] Forms have proper labels and validation
- [ ] Navigation matches navbar style
- [ ] Modals/overlays have proper z-index
- [ ] Badges use proper badge styles

### ✅ Browser Support

- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile browsers (iOS Safari, Chrome Android)

### ✅ Final Review

- [ ] Designer approval?
- [ ] Product owner approval?
- [ ] Accessibility review?
- [ ] Performance acceptable?
- [ ] All edge cases handled?
- [ ] Documentation updated?
- [ ] Ready for production?

---

## Search Reference

### Quick Lookups

| Need | Where | Command |
|------|-------|---------|
| Color for CTAs | Color Palette | Primary = Teal |
| Font for headings | Typography | Poppins 700-800 |
| Spacing between elements | Spacing Scale | 16px (spacing-sm) |
| Button size | Component Library | 44px minimum |
| Focus ring color | Accessibility | Teal border + glow |
| Animation duration | Motion | 0.3s ease-out |
| Icon source | Anti-Patterns | Heroicons, Lucide |
| Touch target | Touch | 44x44px minimum |
| Contrast ratio | Accessibility | 4.5:1 (AA), 7:1 (AAA) |

### Common Questions Answered

**Q: What color should this button be?**
A: Primary action = Teal (#00D9FF)
Secondary action = Navy (#001F3F)

**Q: How much space between elements?**
A: Use 16px (spacing-sm), 24px (spacing-md), or 32px (spacing-lg)

**Q: Can I use this emoji as an icon?**
A: No. Use SVG from Heroicons or Lucide instead.

**Q: What focus state should this have?**
A: Teal border with 3px glow: `border-color: var(--color-teal); box-shadow: 0 0 0 3px rgba(0, 217, 255, 0.1);`

**Q: How fast should this animation be?**
A: 0.3s ease-out for standard interactions, 0.2s for micro, 0.5s for dramatic

**Q: Can I use this color for text?**
A: Check contrast ratio. Navy on white = 7.5:1 ✅. Light grey on white = 4.5:1 ⚠️

---

## Implementation Guide

### Phase 1: Foundation ✅
All design tokens defined in CSS variables.
Ready for use in all components.

### Phase 2: Component Audit
Review each component for:
- Color compliance (Navy + Teal)
- Typography hierarchy (Poppins + Inter)
- Spacing consistency (8-step scale)
- Accessibility (focus states, contrast)
- Responsive behavior (375px, 768px, 1440px)

### Phase 3: Animation Review
Check all animations for:
- Appropriate timing (0.2s-0.5s)
- GPU acceleration (transform, opacity)
- prefers-reduced-motion support
- Smooth 60fps performance

### Phase 4: Testing
- [ ] Manual testing in all browsers
- [ ] Automated accessibility tests (axe, Lighthouse)
- [ ] Performance profiling
- [ ] Mobile testing (iOS, Android)
- [ ] Keyboard navigation testing
- [ ] Screen reader testing

### Phase 5: Deployment
- [ ] All items from pre-delivery checklist verified
- [ ] Documentation updated
- [ ] Team trained on new design system
- [ ] Monitoring set up for performance
- [ ] Ready for production release

---

## Style Guide Summary

| Aspect | Value |
|--------|-------|
| **Brand Colors** | Navy #001F3F + Teal #00D9FF |
| **Display Font** | Poppins (700-800) |
| **Body Font** | Inter (400-600) |
| **Primary CTA** | Teal with Navy text |
| **Button Size** | 44x44px minimum |
| **Card Border** | 4px Navy, left side |
| **Shadow Depth** | 4px shadow (0 4px 12px) |
| **Animation Duration** | 0.3s ease-out |
| **Focus Ring** | Teal border + glow |
| **Spacing Unit** | 8px (16px, 24px, 32px, etc.) |
| **Contrast Minimum** | 4.5:1 (AAA = 7:1) |
| **Touch Target** | 44x44px |
| **Icon Library** | Heroicons, Lucide, or SVG |
| **Responsive Breakpoints** | Mobile 375px, Tablet 768px, Desktop 1024px, Large 1440px |
| **Mobile Font Size** | Minimum 16px (no zoom) |

---

## Resources

- **Design System:** `docs/DESIGN_SYSTEM.md`
- **Implementation Details:** `docs/PHASE1_IMPLEMENTATION.md`
- **Quick Reference:** `docs/QUICKSTART.md`
- **CSS Variables:** `mysite/static/mysite/css/design-system.css`
- **Animations:** `mysite/static/mysite/css/animations.css`

---

**Last Updated:** 2026-06-09
**Status:** Phase 1 Complete
**Version:** 1.0
**Aesthetic:** Professional + Innovative ✨
