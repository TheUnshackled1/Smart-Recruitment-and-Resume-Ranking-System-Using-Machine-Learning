/*
 * Smart Recruitment - Main Script
 * Scroll animations and interactive effects
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize scroll animations
  initScrollAnimations();

  // Add hover effects to cards
  initCardHovers();

  // Logo and branding style
  initBranding();
});

/**
 * Initialize scroll-triggered animations
 */
function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe all scroll targets
  document.querySelectorAll('.scroll-target').forEach(el => {
    observer.observe(el);
  });

  // Observe job listing cards
  document.querySelectorAll('.job-listing').forEach((el, index) => {
    el.classList.add('scroll-target');
    el.style.animationDelay = `${index * 0.1}s`;
    observer.observe(el);
  });

  // Observe section headers
  document.querySelectorAll('h2, h3').forEach((el) => {
    if (!el.classList.contains('animate-fade-in')) {
      el.classList.add('scroll-target');
      observer.observe(el);
    }
  });
}

/**
 * Add hover lift effect to cards
 */
function initCardHovers() {
  const cards = document.querySelectorAll('.card, .job-listing, .job-card');

  cards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-8px)';
    });

    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });
}

/**
 * Initialize branding styles
 */
function initBranding() {
  const navbar = document.querySelector('.site-navbar');

  if (navbar) {
    navbar.style.opacity = '0';
    navbar.style.animation = 'fadeIn 0.8s ease-out forwards';
  }
}

/**
 * Smooth scroll for anchor links
 */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});
