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

    // ===== Global Form Handler (Optional) =====
    // No specific contact form handling needed as contact.html was removed.
    // Navigation to socials is now handled via #contact anchor tag in HTML.

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
    // ===== Dynamic Course Unit System (Embedded DB for Local Reliability) =====
    const progSelect = document.getElementById('programmeSelect');
    const semSelect = document.getElementById('semesterSelect');
    const courseGrid = document.getElementById('courseGrid');
    const totalCreditsSpan = document.getElementById('totalCredits');

    const coursesData = {
        "B.Sc. Software Engineering": {
            "Year 1, Sem I": [
                {"code": "SE 1101", "name": "Intro to Software Engineering", "credits": 4},
                {"code": "CSC 1102", "name": "Programming Fundamentals", "credits": 3},
                {"code": "MTH 1103", "name": "Discrete Mathematics", "credits": 4}
            ],
            "Year 1, Sem II": [
                {"code": "SE 1201", "name": "Software Requirements Engineering", "credits": 4},
                {"code": "CSC 1202", "name": "Data Structures & Algorithms", "credits": 3},
                {"code": "ENG 1203", "name": "Communication Skills", "credits": 3}
            ]
        },
        "Bachelor of Records and Archives Management": {
            "Year 1, Sem I": [
                {"code": "BRAM 1101", "name": "Principles of Archival Science", "credits": 3},
                {"code": "BRAM 1102", "name": "Information Theory", "credits": 4},
                {"code": "ENG 1103", "name": "Communication Skills", "credits": 3}
            ],
            "Year 1, Sem II": [
                {"code": "BRAM 1201", "name": "Digital Records Management", "credits": 3},
                {"code": "BRAM 1202", "name": "Preservation & Conservation", "credits": 3},
                {"code": "IT 1203", "name": "Web Design for Archives", "credits": 3}
            ]
        },
        "Bachelor of Information Technology": {
            "Year 1, Sem I": [
                {"code": "BIT 1101", "name": "Fundamentals of IT", "credits": 4},
                {"code": "CSC 1102", "name": "Programming in C", "credits": 3},
                {"code": "IT 1103", "name": "Intro to Databases", "credits": 4}
            ],
            "Year 1, Sem II": [
                {"code": "BIT 1201", "name": "Systems Administration", "credits": 3},
                {"code": "BIT 1202", "name": "Computer Networking", "credits": 4},
                {"code": "ENG 1203", "name": "Technical Writing", "credits": 3}
            ]
        },
        "BSc Network Systems Administration": {
            "Year 1, Sem I": [
                {"code": "NSA 1101", "name": "Cisco Routing & Switching", "credits": 4},
                {"code": "NSA 1102", "name": "System Security", "credits": 3}
            ],
            "Year 1, Sem II": [
                {"code": "NSA 1201", "name": "Server Administration", "credits": 4},
                {"code": "NSA 1202", "name": "Cloud Computing Fundamentals", "credits": 3}
            ]
        },
        "BSc Applied Data Science and Artificial Intelligence": {
            "Year 1, Sem I": [
                {"code": "DS 1101", "name": "Python for Data Science", "credits": 4},
                {"code": "DS 1102", "name": "Probability & Statistics", "credits": 3}
            ],
            "Year 1, Sem II": [
                {"code": "DS 1201", "name": "Machine Learning I", "credits": 4},
                {"code": "DS 1202", "name": "Data Visualization", "credits": 3}
            ]
        }
    };

    if (progSelect && semSelect && courseGrid) {
        const updateGrid = () => {
            const prog = progSelect.value;
            const sem = semSelect.value;
            
            // Need both selections to fetch
            if (!prog || !sem) {
                courseGrid.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:20px; color:#64748b;">Please select both Programme and Semester level to see units.</div>`;
                return;
            }

            const units = coursesData[prog]?.[sem] || [];
            courseGrid.innerHTML = ''; 

            if (units.length === 0) {
                courseGrid.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:20px; color:#ef4444; font-weight:600;">No units found for ${prog} - ${sem}.</div>`;
                return;
            }

            units.forEach(unit => {
                const div = document.createElement('div');
                div.className = 'course-item';
                div.innerHTML = `
                    <input type="checkbox" class="course-check" data-credits="${unit.credits}" checked>
                    <div style="display:flex; flex-direction:column;">
                        <strong style="color:var(--bu-blue);">${unit.code}</strong>
                        <span style="font-size:0.8rem; font-weight:600;">${unit.name} (${unit.credits} CU)</span>
                    </div>
                `;
                courseGrid.appendChild(div);
            });

            calculateCredits();
            
            document.querySelectorAll('.course-check').forEach(check => {
                check.addEventListener('change', calculateCredits);
            });
        };

        function calculateCredits() {
            let total = 0;
            document.querySelectorAll('.course-check:checked').forEach(check => {
                total += parseFloat(check.getAttribute('data-credits') || 0);
            });
            totalCreditsSpan.textContent = total;
        }

        progSelect.addEventListener('change', updateGrid);
        semSelect.addEventListener('change', updateGrid);
    }
});
