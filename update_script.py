import os
import re

folder = r"c:\Users\NAIGA\Desktop\Web Programming"

# Renaming map
rename_map = {
    "department_timetable.html": "timetable.html",
    "registrationForm.html": "register.html",
    "usefulWebsitesForStudents.html": "websites.html"
}

# Rename files First
for old_name, new_name in rename_map.items():
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} -> {new_name}")

# Now go through all HTML files
html_files = [f for f in os.listdir(folder) if f.endswith(".html")]

for file in html_files:
    path = os.path.join(folder, file)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update references
    content = content.replace("department_timetable.html", "timetable.html")
    content = content.replace("registrationForm.html", "register.html")
    content = content.replace("usefulWebsitesForStudents.html", "websites.html")
    content = content.replace("apply.html", "register.html")

    # 2. Update "Apply Now" and "Apply" text
    content = re.sub(r'>\s*Apply Now\s*<', '>Register<', content, flags=re.IGNORECASE)
    content = re.sub(r'>\s*Apply Online\s*<', '>Register Online<', content, flags=re.IGNORECASE)
    content = re.sub(r"onmouseout=\"[^\"]*\">Apply", lambda m: m.group(0).replace("Apply", "Register"), content)

    # For navigation, create a new nav links string
    nav_links = [
        ("index.html", "Home"),
        ("about.html", "About"),
        ("department.html", "Department"),
        ("timetable.html", "Timetable"),
        ("list.html", "List"),
        ("profile.html", "Profile"),
        ("websites.html", "Websites"),
        ("contact.html", "Contact")
    ]
    
    new_nav_html = '<div class="nav-links">\n'
    for href, text in nav_links:
        if href == file:
            new_nav_html += f'            <a href="{href}" style="color: #3498db;" class="active">{text}</a>\n'
        else:
            new_nav_html += f'            <a href="{href}">{text}</a>\n'
    new_nav_html += '        </div>'

    # Replace <div class="nav-links">...</div> with the new one
    content = re.sub(r'<div\s+class="nav-links"\s*>.*?</div>', new_nav_html, content, flags=re.DOTALL)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {file}")
