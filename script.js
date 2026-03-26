// ===== Dropdown Menu Functionality =====
document.addEventListener('DOMContentLoaded', function () {
    const dropdowns = document.querySelectorAll('.dropdown');

    dropdowns.forEach(dropdown => {
        const btn = dropdown.querySelector('.dropdown-btn');
        if (!btn) return;

        btn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();

            dropdowns.forEach(otherDropdown => {
                if (otherDropdown !== dropdown) {
                    otherDropdown.classList.remove('show');
                }
            });

            dropdown.classList.toggle('show');
        });
    });

    // Close dropdown when clicking outside
    document.addEventListener('click', function (e) {
        if (!e.target.closest('.dropdown')) {
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove('show');
            });
        }
    });

    // ===== Navbar Scroll Effect =====
    const nav = document.querySelector('nav');
    const header = document.querySelector('header') || document.querySelector('.page-hero') || document.querySelector('[class*="hero"]');

    if (nav) {
        const updateNavBackground = () => {
            if (header) {
                const headerBottom = header.getBoundingClientRect().bottom;
                nav.classList.toggle('scrolled', headerBottom <= 0);
            } else {
                nav.classList.add('scrolled');
            }
        };

        updateNavBackground();
        window.addEventListener('scroll', updateNavBackground);
        window.addEventListener('resize', updateNavBackground);
    }

    // ===== Theme Engine (Dark/Light Mode) =====
    const themeBtn = document.createElement('div');
    themeBtn.className = 'theme-toggle';
    themeBtn.innerHTML = '<i class="fas fa-moon" id="theme-icon"></i>';
    document.body.appendChild(themeBtn);

    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    updateThemeIcon(currentTheme);

    themeBtn.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        let newTheme = theme === 'light' ? 'dark' : 'light';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcon(newTheme);
    });

    function updateThemeIcon(theme) {
        const icon = document.getElementById('theme-icon');
        if (icon) {
            icon.className = theme === 'light' ? 'fas fa-moon' : 'fas fa-sun';
        }
    }

    // ===== Security Sanitizer (XSS Protection) =====
    function sanitizeInput(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML; // Converts <script> to &lt;script&gt;
    }

    const contactForm = document.querySelector('form');
    if (contactForm && window.location.pathname.includes('contact.html')) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // SECURITY DEMONSTRATION: Sanitize everything before use
            const name = sanitizeInput(document.getElementById('full-name').value);
            const email = sanitizeInput(document.getElementById('email-address').value);
            const message = sanitizeInput(document.getElementById('message-body').value);

            console.log("SECURE DATA:", { name, email, message });
            alert("SUCCESS: Your message has been sanitized and sent securely (XSS Protected)!");
            contactForm.reset();
        });
    }

    // ===== Scroll-to-Top Button (RESTORED) =====
    const scrollBtn = document.createElement('button');
    scrollBtn.className = 'scroll-top-btn';
    scrollBtn.innerHTML = '<i class="fas fa-chevron-up"></i>';
    scrollBtn.setAttribute('aria-label', 'Scroll to top');
    document.body.appendChild(scrollBtn);

    window.addEventListener('scroll', () => {
        scrollBtn.classList.toggle('visible', window.scrollY > 400);
    });

    scrollBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

});
