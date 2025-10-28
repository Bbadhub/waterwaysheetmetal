/**
 * Water Ways Sheet Metal - Main JavaScript
 * Handles mobile navigation, dropdown menus, FAQ accordions, smooth scrolling, and form validation
 * Pattern: Pattern-CONTEXT-002
 */

'use strict';

// =================================================================
// MOBILE MENU FUNCTIONALITY
// =================================================================

/**
 * Mobile hamburger menu toggle
 * Opens/closes full-screen mobile navigation overlay
 */
function initMobileMenu() {
  const hamburger = document.querySelector('.hamburger');
  const mobileMenu = document.querySelector('.mobile-menu');
  const body = document.body;

  if (!hamburger || !mobileMenu) return;

  // Toggle mobile menu
  hamburger.addEventListener('click', () => {
    const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';

    hamburger.setAttribute('aria-expanded', !isExpanded);
    mobileMenu.setAttribute('aria-hidden', isExpanded);

    // Toggle active class for animation
    hamburger.classList.toggle('active');
    mobileMenu.classList.toggle('active');

    // Prevent body scroll when menu open
    body.classList.toggle('menu-open');
  });

  // Close menu when clicking outside
  mobileMenu.addEventListener('click', (e) => {
    if (e.target === mobileMenu) {
      hamburger.click(); // Trigger the same toggle function
    }
  });

  // Close menu on escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
      hamburger.click();
    }
  });
}

// =================================================================
// DESKTOP DROPDOWN MENU FUNCTIONALITY
// =================================================================

/**
 * Desktop Services dropdown hover/click behavior
 */
function initDesktopDropdown() {
  const dropdown = document.querySelector('.nav-dropdown');
  const dropdownToggle = document.querySelector('.dropdown-toggle');
  const dropdownMenu = document.querySelector('.dropdown-menu');

  if (!dropdown || !dropdownToggle || !dropdownMenu) return;

  let closeTimeout;

  // Show dropdown on hover (desktop only)
  dropdown.addEventListener('mouseenter', () => {
    clearTimeout(closeTimeout);
    dropdownToggle.setAttribute('aria-expanded', 'true');
    dropdownMenu.classList.add('active');
  });

  // Hide dropdown after delay
  dropdown.addEventListener('mouseleave', () => {
    closeTimeout = setTimeout(() => {
      dropdownToggle.setAttribute('aria-expanded', 'false');
      dropdownMenu.classList.remove('active');
    }, 300); // 300ms delay before closing
  });

  // Toggle on click (for keyboard/touch users)
  dropdownToggle.addEventListener('click', (e) => {
    e.preventDefault();
    const isExpanded = dropdownToggle.getAttribute('aria-expanded') === 'true';
    dropdownToggle.setAttribute('aria-expanded', !isExpanded);
    dropdownMenu.classList.toggle('active');
  });

  // Close dropdown on outside click
  document.addEventListener('click', (e) => {
    if (!dropdown.contains(e.target)) {
      dropdownToggle.setAttribute('aria-expanded', 'false');
      dropdownMenu.classList.remove('active');
    }
  });
}

// =================================================================
// MOBILE DROPDOWN FUNCTIONALITY
// =================================================================

/**
 * Mobile Services dropdown toggle
 */
function initMobileDropdown() {
  const mobileDropdownToggle = document.querySelector('.mobile-dropdown-toggle');
  const mobileDropdownMenu = document.querySelector('.mobile-dropdown-menu');

  if (!mobileDropdownToggle || !mobileDropdownMenu) return;

  mobileDropdownToggle.addEventListener('click', (e) => {
    e.preventDefault();
    const isExpanded = mobileDropdownToggle.getAttribute('aria-expanded') === 'true';

    mobileDropdownToggle.setAttribute('aria-expanded', !isExpanded);
    mobileDropdownMenu.classList.toggle('active');

    // Rotate dropdown icon
    const icon = mobileDropdownToggle.querySelector('.dropdown-icon');
    if (icon) {
      icon.style.transform = isExpanded ? 'rotate(0deg)' : 'rotate(180deg)';
    }
  });
}

// =================================================================
// FAQ ACCORDION FUNCTIONALITY
// =================================================================

/**
 * FAQ accordion expand/collapse
 * Only one FAQ open at a time
 */
function initFAQAccordion() {
  const faqQuestions = document.querySelectorAll('.faq-question');

  if (faqQuestions.length === 0) return;

  faqQuestions.forEach(question => {
    question.addEventListener('click', () => {
      const faqItem = question.parentElement;
      const faqAnswer = faqItem.querySelector('.faq-answer');
      const isExpanded = question.getAttribute('aria-expanded') === 'true';

      // Close all other FAQs
      document.querySelectorAll('.faq-item').forEach(item => {
        if (item !== faqItem) {
          const otherQuestion = item.querySelector('.faq-question');
          const otherAnswer = item.querySelector('.faq-answer');
          otherQuestion.setAttribute('aria-expanded', 'false');
          item.classList.remove('active');
          if (otherAnswer) {
            otherAnswer.style.maxHeight = null;
          }
        }
      });

      // Toggle current FAQ
      question.setAttribute('aria-expanded', !isExpanded);
      faqItem.classList.toggle('active');

      if (!isExpanded) {
        faqAnswer.style.maxHeight = faqAnswer.scrollHeight + 'px';
      } else {
        faqAnswer.style.maxHeight = null;
      }
    });
  });
}

// =================================================================
// SMOOTH SCROLLING FOR ANCHOR LINKS
// =================================================================

/**
 * Smooth scroll to anchor links (e.g., #quote-form, #process, #why-copper)
 */
function initSmoothScrolling() {
  const anchorLinks = document.querySelectorAll('a[href^="#"]');

  anchorLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');

      // Skip if just "#" (no target)
      if (href === '#') return;

      const targetId = href.substring(1);
      const targetElement = document.getElementById(targetId);

      if (targetElement) {
        e.preventDefault();

        const headerHeight = document.querySelector('.header').offsetHeight;
        const targetPosition = targetElement.offsetTop - headerHeight - 20; // 20px offset

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });

        // Update URL without jumping
        history.pushState(null, null, href);

        // Focus target for accessibility
        targetElement.setAttribute('tabindex', '-1');
        targetElement.focus();
      }
    });
  });
}

// =================================================================
// STICKY HEADER ON SCROLL
// =================================================================

/**
 * Add shadow to header when scrolled
 */
function initStickyHeader() {
  const header = document.querySelector('.header');

  if (!header) return;

  let lastScrollY = window.scrollY;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }

    lastScrollY = window.scrollY;
  });
}

// =================================================================
// CONTACT FORM VALIDATION
// =================================================================

/**
 * Client-side form validation for contact form
 * Validates before allowing submission
 */
function initFormValidation() {
  const form = document.querySelector('.contact-form');

  if (!form) return;

  form.addEventListener('submit', (e) => {
    let isValid = true;
    const errors = [];

    // Get form fields
    const name = form.querySelector('#name');
    const email = form.querySelector('#email');
    const phone = form.querySelector('#phone');
    const message = form.querySelector('#message');

    // Clear previous error states
    document.querySelectorAll('.error-message').forEach(el => el.remove());
    document.querySelectorAll('.input-error').forEach(el => el.classList.remove('input-error'));

    // Validate name
    if (!name.value.trim()) {
      isValid = false;
      errors.push({ field: name, message: 'Please enter your name' });
    }

    // Validate email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email.value.trim()) {
      isValid = false;
      errors.push({ field: email, message: 'Please enter your email' });
    } else if (!emailRegex.test(email.value.trim())) {
      isValid = false;
      errors.push({ field: email, message: 'Please enter a valid email address' });
    }

    // Validate phone (optional but format check if provided)
    const phoneRegex = /^[\d\s\-\(\)\.]+$/;
    if (phone.value.trim() && !phoneRegex.test(phone.value.trim())) {
      isValid = false;
      errors.push({ field: phone, message: 'Please enter a valid phone number' });
    }

    // Validate message
    if (!message.value.trim()) {
      isValid = false;
      errors.push({ field: message, message: 'Please enter a message' });
    } else if (message.value.trim().length < 10) {
      isValid = false;
      errors.push({ field: message, message: 'Message must be at least 10 characters' });
    }

    // Show errors if validation failed
    if (!isValid) {
      e.preventDefault();

      errors.forEach(error => {
        const formGroup = error.field.closest('.form-group');
        error.field.classList.add('input-error');

        const errorMessage = document.createElement('span');
        errorMessage.className = 'error-message';
        errorMessage.textContent = error.message;
        errorMessage.style.color = 'var(--color-copper-dark)';
        errorMessage.style.fontSize = 'var(--font-size-sm)';
        errorMessage.style.marginTop = '4px';
        errorMessage.style.display = 'block';

        formGroup.appendChild(errorMessage);
      });

      // Focus first error
      if (errors.length > 0) {
        errors[0].field.focus();
      }
    }

    // If valid, form submits normally (mailto: link or server endpoint)
  });

  // Remove error state on input
  const inputs = form.querySelectorAll('input, textarea, select');
  inputs.forEach(input => {
    input.addEventListener('input', () => {
      input.classList.remove('input-error');
      const errorMessage = input.closest('.form-group').querySelector('.error-message');
      if (errorMessage) {
        errorMessage.remove();
      }
    });
  });
}

// =================================================================
// LAZY LOAD IMAGES (Native lazy loading fallback)
// =================================================================

/**
 * Add lazy loading to images without loading attribute
 * Modern browsers support loading="lazy" but this adds fallback
 */
function initLazyLoading() {
  if ('loading' in HTMLImageElement.prototype) {
    // Native lazy loading supported
    return;
  }

  // Fallback for older browsers using Intersection Observer
  const images = document.querySelectorAll('img[loading="lazy"]');

  if (images.length === 0) return;

  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src || img.src;
        img.classList.add('loaded');
        observer.unobserve(img);
      }
    });
  });

  images.forEach(img => imageObserver.observe(img));
}

// =================================================================
// ACTIVE NAVIGATION STATE
// =================================================================

/**
 * Highlight current page in navigation
 */
function initActiveNavigation() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');

  navLinks.forEach(link => {
    const linkPath = new URL(link.href).pathname;

    // Exact match or parent match (for service pages)
    if (linkPath === currentPath ||
        (currentPath.includes('/services/') && link.textContent.toLowerCase().includes('services'))) {
      link.classList.add('active');
    }
  });
}

// =================================================================
// INITIALIZE ALL FUNCTIONALITY ON PAGE LOAD
// =================================================================

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initDesktopDropdown();
  initMobileDropdown();
  initFAQAccordion();
  initSmoothScrolling();
  initStickyHeader();
  initFormValidation();
  initLazyLoading();
  initActiveNavigation();

  console.log('Water Ways Sheet Metal - All JavaScript initialized');
});

// =================================================================
// HANDLE PAGE VISIBILITY (Pause animations when tab hidden)
// =================================================================

document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    // Pause any animations or auto-play features
  } else {
    // Resume when tab becomes visible again
  }
});
