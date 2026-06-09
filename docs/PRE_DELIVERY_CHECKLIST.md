# Pre-Delivery Checklist — Smart Recruitment

**Purpose:** Verify all components are production-ready before deployment
**Date Created:** 2026-06-09
**Version:** 1.0

---

## Checkbox Format

Use this template for each component/page before shipping:

```markdown
- [ ] Item name
- [ ] Item name
```

Mark complete with `[x]` when verified.

---

## 1. Visual Quality (7 items)

- [ ] No emojis used as icons (SVG only)
- [ ] All icons are from consistent set (Heroicons/Lucide)
- [ ] Logo is correct (verified from official source)
- [ ] Hover states don't cause layout shift
- [ ] Colors use CSS variables (not hardcoded hex)
- [ ] Typography hierarchy clear (size + weight variation)
- [ ] Spacing consistent (multiples of 8px)

---

## 2. Interaction & UX (8 items)

- [ ] All clickable elements have `cursor-pointer`
- [ ] Hover states provide clear visual feedback (color/shadow/border)
- [ ] Focus states are visible (keyboard navigation)
- [ ] Touch targets are minimum 44x44px
- [ ] Buttons disabled during async operations
- [ ] Error messages appear near problem field
- [ ] Form placeholder text is not replacing label
- [ ] All interactive elements work on keyboard (Tab, Enter, Space)

---

## 3. Light & Dark Mode (4 items)

- [ ] Light mode text has 4.5:1+ contrast
- [ ] Dark mode backgrounds are >= #1F2937
- [ ] Borders are visible in both modes
- [ ] Glass/transparent elements readable in both modes

---

## 4. Accessibility (8 items)

- [ ] All images have meaningful alt text
- [ ] Form inputs have associated labels
- [ ] Buttons have aria-label if icon-only
- [ ] Color is not the only indicator (use icons + text)
- [ ] Focus order is logical (left-to-right, top-to-bottom)
- [ ] ARIA roles used correctly (for complex widgets)
- [ ] Page structure is semantic (header, nav, main, footer)
- [ ] Text can be zoomed to 200% without breaking layout

---

## 5. Performance (8 items)

- [ ] Images are optimized (WebP with JPG fallback)
- [ ] Animations respect `prefers-reduced-motion`
- [ ] No layout reflows during animations
- [ ] Animations smooth (60fps on phone)
- [ ] CSS animations preferred (not JS)
- [ ] No console warnings or errors
- [ ] Page load time < 3 seconds
- [ ] Lighthouse score >= 90 (Desktop), >= 80 (Mobile)

---

## 6. Code Quality (7 items)

- [ ] CSS uses design system variables
- [ ] No inline styles (use classes)
- [ ] BEM or similar naming conventions used
- [ ] DRY principle applied (no duplication)
- [ ] Responsive classes used correctly
- [ ] No hardcoded color values
- [ ] No pixel-perfect hacks or workarounds

---

## 7. Components (6 items)

- [ ] Buttons follow button styles exactly
- [ ] Cards use proper card component
- [ ] Forms have proper labels and validation
- [ ] Navigation matches navbar style
- [ ] Modals/overlays have proper z-index
- [ ] Badges use proper badge styles

---

## 8. Browser Support (5 items)

- [ ] Chrome (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Edge (latest)
- [ ] Mobile browsers (iOS Safari, Chrome Android)

---

## 9. Final Review (6 items)

- [ ] Design system applied consistently
- [ ] No regression from previous versions
- [ ] Team review completed
- [ ] Security review (if needed)
- [ ] Accessibility audit (axe, Lighthouse)
- [ ] Ready for production deployment

---

## Component-Specific Checklists

### Button Checklist

- [ ] Primary variant: Teal bg, Navy text
- [ ] Secondary variant: Navy border, transparent bg
- [ ] Hover state: Colors swap with smooth transition
- [ ] Disabled state: Opacity 0.6, cursor not-allowed
- [ ] Focus state: 2px teal outline
- [ ] Sizes: sm (36px), md (44px), lg (52px) min-height
- [ ] Touch target: Minimum 44x44px

### Card Checklist

- [ ] Navy left border (4px)
- [ ] Card header: light grey background
- [ ] Card body: padding consistent
- [ ] Card footer: border-top with actions
- [ ] Hover state: translateY(-4px), shadow-lg
- [ ] Border color changes to teal on hover
- [ ] No layout shift on hover

### Form Checklist

- [ ] Label paired with input (id matching)
- [ ] Focus ring: 3px teal glow
- [ ] Invalid state: red border
- [ ] Valid state: green border
- [ ] Error message: red text, small font, below input
- [ ] Placeholder: light grey, not replacing label
- [ ] Disabled state: grey bg, cursor not-allowed

### Navigation Checklist

- [ ] Logo styled correctly (font-display, navy)
- [ ] Nav links: white text, teal on hover
- [ ] Active link: teal bottom border
- [ ] Mobile menu: hamburger toggle
- [ ] Sticky navbar: z-index correct
- [ ] No overlap with page content
- [ ] Responsive on all breakpoints

### Hero Section Checklist

- [ ] Background image loaded
- [ ] Gradient overlay applied correctly
- [ ] Title: animate-slide-down class
- [ ] Subtitle: animate-fade-in class
- [ ] Form: animate-slide-up class
- [ ] Staggered animation timing correct
- [ ] Mobile responsive (title smaller, form stack)

### Job Listing Checklist

- [ ] Grid responsive (1 col mobile, 3 col desktop)
- [ ] Cards use JobCard component
- [ ] Scroll animations trigger (IntersectionObserver)
- [ ] "Apply" button shows loading state
- [ ] Hover effects work smoothly
- [ ] No horizontal scroll on mobile

---

## Pre-Deployment Verification

Run these checks before pushing to production:

### Automated Tests
```bash
# Accessibility audit
npm run audit:a11y

# Lighthouse audit
npm run audit:performance

# Visual regression tests
npm run test:visual

# Component tests
npm run test:components
```

### Manual Tests
```
1. Test on Chrome, Firefox, Safari, Edge
2. Test on iPhone (iOS Safari)
3. Test on Android (Chrome)
4. Test keyboard navigation (Tab, Enter, Escape)
5. Test with screen reader (NVDA, JAWS, VoiceOver)
6. Test zoom to 200%
7. Test light & dark mode
8. Test with reduced motion enabled
9. Test on slow 3G network
10. Test without JavaScript (where applicable)
```

### Browser DevTools
- [ ] No console errors
- [ ] No console warnings
- [ ] No accessibility warnings
- [ ] Lighthouse score acceptable
- [ ] No layout shifts (cls < 0.1)
- [ ] Performance metrics within bounds

---

## Sign-Off

| Role | Name | Date | Status |
|------|------|------|--------|
| Developer | ___________ | _____ | ☐ Approved |
| Designer | ___________ | _____ | ☐ Approved |
| QA | ___________ | _____ | ☐ Approved |
| Product Owner | ___________ | _____ | ☐ Approved |

---

## Deployment Checklist

After all items checked:

- [ ] Create release branch
- [ ] Update version number
- [ ] Update changelog
- [ ] Create pull request
- [ ] Merge after approval
- [ ] Tag release
- [ ] Deploy to staging
- [ ] Verify staging deployment
- [ ] Deploy to production
- [ ] Monitor for errors (1 hour)
- [ ] Announce release

---

## Rollback Plan

If critical issues found:

1. Identify scope of issue
2. Create hotfix branch
3. Fix issue
4. Test thoroughly
5. Deploy hotfix
6. Verify fix
7. Document issue & resolution

---

## Common Issues & Solutions

### Layout Shift on Hover
**Problem:** Card shifts when hover effect applied
**Solution:** Use `transform: translateY()` instead of changing height/width

### Accessibility Warning
**Problem:** "Color contrast too low"
**Solution:** Use dark text (#2C3E50) on light backgrounds, light text on dark

### CSS Variable Not Working
**Problem:** Color not applying
**Solution:** Ensure `var(--color-navy)` in CSS, not inline styles

### Animation Jank
**Problem:** Animation stutters
**Solution:** Use `transform` and `opacity` only, add `will-change: transform`

### Focus Ring Invisible
**Problem:** Can't see focus ring
**Solution:** Use `outline: 2px solid var(--color-teal); outline-offset: 2px;`

### Mobile Touch Too Small
**Problem:** Can't tap button
**Solution:** Ensure button is 44x44px minimum (use utilities if needed)

---

## Notes

- Run automated checks weekly for regression
- Update checklist when adding new components
- Keep browser version list current
- Review accessibility guidelines quarterly

---

**Sign this checklist before deployment.**

Valid until: 2026-12-09 (6 months)
