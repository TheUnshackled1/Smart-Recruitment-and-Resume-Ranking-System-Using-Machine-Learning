# Smart Recruitment Design System

**Aesthetic Direction:** Professional + Innovative
**Target Audience:** Recruiters & Job Seekers
**Emotional Tone:** Trustworthy, Forward-Thinking, Energetic

---

## Color Palette

### Primary Colors
```css
--color-navy: #001F3F;      /* Deep trust, stability, authority */
--color-teal: #00D9FF;      /* Innovation, energy, forward-thinking */
--color-dark-navy: #000F1F; /* Darker variant for depth */
--color-light-teal: #B3F1FF; /* Lighter teal for backgrounds */
```

### Neutral Colors
```css
--color-dark-grey: #2C3E50;   /* Headers, body text */
--color-medium-grey: #7F8C8D; /* Secondary text, disabled state */
--color-light-grey: #ECF0F1;  /* Backgrounds, dividers */
--color-white: #FFFFFF;       /* Pure white for contrast */
```

### Semantic Colors
```css
--color-success: #27AE60;  /* Green for confirmations */
--color-warning: #F39C12;  /* Orange for alerts */
--color-danger: #E74C3C;   /* Red for errors */
--color-info: #3498DB;     /* Blue for information */
```

---

## Typography

### Display Font (Headlines)
**Family:** [Poppins](https://fonts.google.com/specimen/Poppins)
**Import:** `https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap`
**Weights:** 400, 500, 600, 700, 800

**Usage:**
```css
h1, h2, h3, .display-text {
  font-family: 'Poppins', sans-serif;
  font-weight: 700; /* Bold for impact */
}
```

### Body Font
**Family:** [Inter](https://fonts.google.com/specimen/Inter)
**Import:** `https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap`
**Weights:** 300, 400, 500, 600

**Usage:**
```css
body, p, .body-text {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  line-height: 1.6;
}
```

### Scale
```
h1: 2.5rem / 40px
h2: 2rem / 32px
h3: 1.5rem / 24px
h4: 1.25rem / 20px
body: 1rem / 16px
small: 0.875rem / 14px
```

---

## Visual Principles

### 1. Spacing & Layout
- **Generous whitespace:** Breathing room between sections
- **Asymmetric grids:** Break predictable patterns on hero/key pages
- **16px base unit:** All spacing multiples of 16px (16, 24, 32, 48, 64)

### 2. Motion & Animation
- **Page load:** Staggered reveals for hero content (300-500ms stagger)
- **Scroll triggers:** Job cards fade in as user scrolls
- **Hover states:** Subtle lift effect (transform: translateY) on cards
- **Transitions:** All interactions use 0.3s ease-out

### 3. Components
- **Buttons:** Poppins, 600 weight, Teal background with navy text hover
- **Cards:** Subtle shadow (0 4px 12px rgba), Navy border-left accent
- **Inputs:** Navy focus ring, Teal placeholder text
- **Badges:** Navy background with Teal text

### 4. Backgrounds & Details
- **Hero section:** Linear gradient from Navy to Dark Navy, image overlay with 60% opacity
- **Section dividers:** Teal accent line (2px) at top of major sections
- **Decorative elements:** Subtle geometric shapes (circles, angles) positioned asymmetrically
- **Textures:** Fine noise overlay (1% opacity) for depth

---

## CSS Variable Map

```css
:root {
  /* Colors */
  --primary-color: #001F3F;
  --accent-color: #00D9FF;
  --dark-text: #2C3E50;
  --light-bg: #ECF0F1;
  --border-color: #E0E0E0;

  /* Typography */
  --font-display: 'Poppins', sans-serif;
  --font-body: 'Inter', sans-serif;

  /* Spacing */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 1.5rem;
  --spacing-lg: 2rem;
  --spacing-xl: 3rem;

  /* Motion */
  --transition-fast: 0.2s ease-out;
  --transition-base: 0.3s ease-out;
  --transition-slow: 0.5s ease-out;
}
```

---

## Implementation Phases

### Phase 1: Foundation (CSS)
- [ ] Replace Nunito with Poppins + Inter in `base.html`
- [ ] Create `design-system.css` with CSS variables
- [ ] Override Bootstrap colors
- [ ] Set base typography rules

### Phase 2: Hero Section Redesign
- [ ] Add gradient background to hero
- [ ] Implement staggered animation on page load
- [ ] Asymmetric layout for search form
- [ ] Teal accent lines

### Phase 3: Component Polish
- [ ] Update buttons (navy → teal, hover state)
- [ ] Update cards (Navy left border, subtle shadow)
- [ ] Update form inputs (Navy focus ring)
- [ ] Add decorative elements

### Phase 4: Page Animations
- [ ] Job listing cards: Scroll-triggered fade-in
- [ ] Modal/overlay transitions
- [ ] Hover states for interactive elements
- [ ] Loading states

### Phase 5: Fine Details
- [ ] Decorative geometric shapes (SVG overlays)
- [ ] Texture overlays on sections
- [ ] Custom focus/selection colors
- [ ] Polish responsive behavior

---

## Files to Create/Modify

### New Files:
- `mysite/static/mysite/css/design-system.css` — CSS variables & base rules
- `mysite/static/mysite/css/animations.css` — Keyframes & animation utilities

### Modify:
- `mysite/templates/mysite/base.html` — Font imports, stylesheet links
- `mysite/static/mysite/css/custom-bs.css` — Bootstrap color overrides
- `mysite/static/mysite/css/style.css` — Component-specific updates
- Template files — Add animation classes, adjust layouts

---

## Reference Inspiration

Sites with similar "Professional + Innovative" energy:
- **Stripe** (Navy + clean, minimal but bold)
- **Vercel** (Black + minimal, tech-focused)
- **Linear** (Dark + vibrant, modern workflows)

---

## Next Steps

1. ✅ Design system defined
2. ⏭️ Implement CSS variables
3. ⏭️ Update typography
4. ⏭️ Design hero section with animations
5. ⏭️ Polish components
6. ⏭️ Add page animations
7. ⏭️ Test responsiveness
