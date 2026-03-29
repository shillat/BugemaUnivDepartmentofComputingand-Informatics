import os
import re

directory = r'c:\Users\NAIGA\Desktop\Web Programming'

def update_navigation(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace staff.html links with about.html#staff
                new_content = re.sub(r'href=["\'](?:\./)?staff\.html["\']', 'href="about.html#staff"', content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated navigation in {filepath}")

update_navigation(directory)

# Update nav_updater.py if it exists
updater_path = os.path.join(directory, 'nav_updater.py')
if os.path.exists(updater_path):
    with open(updater_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove staff.html from config
    content = content.replace("'staff.html': 'Our Staff & Faculty',", "")
    # Update nav_template to use about.html#staff
    content = content.replace('<a href="staff.html"{staff}>Staff</a>', '<a href="about.html#staff"{staff}>Staff</a>')
    # Update active_map logic for staff
    # Actually, it's simpler to just remove 'staff' from active_map keys if we use about.html#staff
    content = content.replace("'staff': ' class=\"active\"' if file == 'staff.html' else '',", "'staff': '',")
    
    with open(updater_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated nav_updater.py")

# Delete staff.html
staff_path = os.path.join(directory, 'staff.html')
if os.path.exists(staff_path):
    os.remove(staff_path)
    print("Deleted staff.html")

# Also in subdir
staff_path_sub = os.path.join(directory, 'BugemaUnivDepartmentofComputingand-Informatics', 'staff.html')
if os.path.exists(staff_path_sub):
    os.remove(staff_path_sub)
    print(f"Deleted {staff_path_sub}")
