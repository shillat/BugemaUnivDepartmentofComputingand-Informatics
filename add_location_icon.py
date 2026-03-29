import os

directory = r'c:\Users\NAIGA\Desktop\Web Programming'
google_maps_url = 'https://www.google.com/maps/place/Bugema+University'

# Target structure to find:
find_str = '<a href="https://wa.me/256777567890" target="_blank" class="social-icon whatsapp"><i class="fab fa-whatsapp"></i></a>'
# New structure with location icon:
replace_str = find_str + f'\n                    <a href="{google_maps_url}" target="_blank" class="social-icon location" title="Our Location"><i class="fas fa-map-marker-alt"></i></a>'

def process_html_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if find_str in content and 'social-icon location' not in content:
                    new_content = content.replace(find_str, replace_str)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

process_html_files(directory)

# Also update styles.css to include hover color for location
styles_path = os.path.join(directory, 'styles.css')
if os.path.exists(styles_path):
    with open(styles_path, 'r', encoding='utf-8') as f:
        styles_content = f.read()
    
    if '.social-icon.location:hover' not in styles_content:
        new_styles = styles_content.replace('.social-icon.whatsapp:hover {', '.social-icon.location:hover {\n    background: #4285f4; /* Google Blue for Location */\n}\n\n.social-icon.whatsapp:hover {')
        with open(styles_path, 'w', encoding='utf-8') as f:
            f.write(new_styles)
        print("Updated styles.css with location hover color")
