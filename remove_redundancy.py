import os
import re

directory = r'c:\Users\NAIGA\Desktop\Web Programming'

# Target strings to remove
targets = [
    r'<a href="department\.html">Departments</a>',
    r'<a href="staff\.html">Staff Profile</a>',
    r'<a href="staff\.html">Staff Profiles</a>',
    r'<a href="about\.html#staff">Staff Profiles</a>',
    r'<a href="about\.html#staff">Staff Profile</a>'
]

def remove_redundant_links(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for target in targets:
                    # Remove the line containing the target link
                    # We match the entire line if it's just the link, or just the link itself
                    new_content = re.sub(target + r'\s*', '', new_content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

remove_redundant_links(directory)

# Update the two nav_updater.py files
updaters = [
    os.path.join(directory, 'nav_updater.py'),
    os.path.join(directory, 'BugemaUnivDepartmentofComputingand-Informatics', 'nav_updater.py')
]

for updater in updaters:
    if os.path.exists(updater):
        with open(updater, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove mentions in nav templates
        # Note: some updaters might have different structures.
        # My previous edits changed them to:
        # <a href="department.html"{dept}>Departments</a>
        # <a href="about.html#staff"{staff}>Staff</a>
        
        content = re.sub(r'<a href="department\.html"\{dept\}>Departments</a>\s*', '', content)
        content = re.sub(r'<a href="about\.html#staff"\{staff\}>Staff</a>\s*', '', content)
        content = re.sub(r'<a href="staff\.html"\{staff\}>Staff</a>\s*', '', content)
        
        # Also remove from maps if they exist
        content = re.sub(r"'dept': .*?,\s*", "", content)
        content = re.sub(r"'staff': .*?,\s*", "", content)
        
        with open(updater, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {updater}")
