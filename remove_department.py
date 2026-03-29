import os
import re

directory = r'c:\Users\NAIGA\Desktop\Web Programming'

def remove_department_links(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace department.html with about.html
                new_content = re.sub(r'href=["\'](?:\./)?department\.html["\']', 'href="about.html"', content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated links in {filepath}")

remove_department_links(directory)

# Delete department.html
dept_path = os.path.join(directory, 'department.html')
if os.path.exists(dept_path):
    os.remove(dept_path)
    print("Deleted department.html")

# Also in subdir
dept_path_sub = os.path.join(directory, 'BugemaUnivDepartmentofComputingand-Informatics', 'department.html')
if os.path.exists(dept_path_sub):
    os.remove(dept_path_sub)
    print(f"Deleted {dept_path_sub}")
