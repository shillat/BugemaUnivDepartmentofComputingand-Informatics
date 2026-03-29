import os
import re

folder = r"C:\Users\NAIGA\Desktop\Web Programming"

# The link we want to add
admission_link = '                    <li><a href="admissionform.html">Apply for Admission</a></li>\n'

# Pattern to look for the Explore list
explore_pattern = r'<h4 class="footer-heading">Explore</h4>\s*<ul class="footer-links">(.*?)</ul>'

html_files = [f for f in os.listdir(folder) if f.endswith('.html')]

print(f"Updating footer 'Explore' links on {len(html_files)} files...")

for file in html_files:
    file_path = os.path.join(folder, file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if admissions is already there
        if 'admissionform.html' in content:
            print(f" - Admissions link already exists in: {file}")
            continue

        # Find the Explore section
        match = re.search(explore_pattern, content, flags=re.DOTALL)
        if match:
            # We insert it before Register Online if possible, or just at the end
            current_links = match.group(1)
            
            # Pattern to find the last </ul> end
            new_links = current_links + admission_link
            
            # Reconstruct the section
            new_section = f'<h4 class="footer-heading">Explore</h4>\n                <ul class="footer-links">{new_links}                </ul>'
            
            new_content = re.sub(explore_pattern, new_section, content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f" - Updated: {file}")
        else:
            print(f" - Explore section not found in: {file}")
            
    except Exception as e:
        print(f" - Error processing {file}: {e}")

print("Footer link update complete.")
