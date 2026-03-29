import os
import re

directory = r'c:\Users\NAIGA\Desktop\Web Programming'

html_files = [f for f in os.listdir(directory) if f.endswith('.html')]

for filename in html_files:
    # Skip contact.html itself as we will delete it, but let's process it anyway in case it's used as a template
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update links to contact.html to #contact
    # Also handle variants like ./contact.html
    new_content = re.sub(r'href=["\'](?:\./)?contact\.html["\']', 'href="#contact"', content)

    # 2. Add id="contact" to the "Stay Connected" heading in the footer
    # Looking for: <h4 class="footer-heading">Stay Connected</h4>
    # We want: <h4 class="footer-heading" id="contact">Stay Connected</h4>
    new_content = new_content.replace('<h4 class="footer-heading">Stay Connected</h4>', '<h4 class="footer-heading" id="contact">Stay Connected</h4>')

    # Also handle potential variations if any
    new_content = new_content.replace('<h4 class="footer-heading">Stay Connected </h4>', '<h4 class="footer-heading" id="contact">Stay Connected</h4>')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")

# Also check the subdirectory BugemaUnivDepartmentofComputingand-Informatics
subdir = os.path.join(directory, 'BugemaUnivDepartmentofComputingand-Informatics')
if os.path.isdir(subdir):
    html_files_sub = [f for f in os.listdir(subdir) if f.endswith('.html')]
    for filename in html_files_sub:
        filepath = os.path.join(subdir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = re.sub(r'href=["\'](?:\./)?contact\.html["\']', 'href="#contact"', content)
        new_content = new_content.replace('<h4 class="footer-heading">Stay Connected</h4>', '<h4 class="footer-heading" id="contact">Stay Connected</h4>')
        new_content = new_content.replace('<h4 class="footer-heading">Stay Connected </h4>', '<h4 class="footer-heading" id="contact">Stay Connected</h4>')
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")

# Finally, delete contact.html
contact_html = os.path.join(directory, 'contact.html')
if os.path.exists(contact_html):
    os.remove(contact_html)
    print("Deleted contact.html")

contact_html_sub = os.path.join(subdir, 'contact.html')
if os.path.exists(contact_html_sub):
    os.remove(contact_html_sub)
    print(f"Deleted {contact_html_sub}")
