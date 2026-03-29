import os
import re

folder = r"c:\Users\NAIGA\Desktop\Web Programming"

new_files_config = {
    'programs.html': 'Academic Programs',
    
    'research.html': 'Research & Publications',
    'admissions.html': 'Admissions'
}

# Ensure new files exist by copying from about.html
about_path = os.path.join(folder, 'about.html')
with open(about_path, 'r', encoding='utf-8') as f:
    about_content = f.read()

for new_file, title in new_files_config.items():
    new_file_path = os.path.join(folder, new_file)
    if not os.path.exists(new_file_path):
        # We replace title
        content = re.sub(r'<title>.*?</title>', f'<title>{title} | Bugema University</title>', about_content, flags=re.DOTALL)
        # We replace the header text
        content = re.sub(r'<header class="about-hero">.*?</header>', f'<header class="about-hero">\n        <h1>{title}</h1>\n        <p style="max-width: 700px; margin: auto; font-size: 1.2rem; opacity: 0.9;">Excellence in Service</p>\n    </header>', content, flags=re.DOTALL)
        # Empty out container
        content = re.sub(r'<div class="container">.*?</div>\s*<footer', '<div class="container">\n\n</div>\n\n<footer', content, flags=re.DOTALL)
        
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(content)

# Update nav in all files
nav_template = """        <div class="nav-links">
            <a href="index.html"{home}>Home</a>
            <a href="about.html"{about}>About</a>
            <a href="programs.html"{prog}>Programs</a>
            <a href="research.html"{res}>Research</a>
            <a href="admissions.html"{adm}>Admissions</a>
            <a href="#contact"{cont}>Contact</a>
        </div>"""

html_files = [f for f in os.listdir(folder) if f.endswith('.html')]
for file in html_files:
    file_path = os.path.join(folder, file)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    active_map = {
        'home': ' class="active"' if file == 'index.html' else '',
        'about': ' class="active"' if file == 'about.html' else '',
        'prog': ' class="active"' if file == 'programs.html' else '',
        'res': ' class="active"' if file == 'research.html' else '',
        'adm': ' class="active"' if file == 'admissions.html' else '',
        'cont': '' # Anchor links don't usually have active state across pages
    }
    
    new_nav = nav_template.format(**active_map)
    content = re.sub(r'<div\s+class="nav-links"\s*>.*?</div>', new_nav, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navigation and new template pages updated successfully.")
