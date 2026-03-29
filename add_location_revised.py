import os
import re

directory = r'c:\Users\NAIGA\Desktop\Web Programming'
google_maps_url = 'https://www.google.com/maps/place/Bugema+University'

# Target pattern: whatsapp social icon
whatsapp_pattern = re.compile(r'<a href="https://wa\.me/256777567890" target="_blank" class="social-icon whatsapp">.*?</a>', re.DOTALL)

def process_html_files(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if location icon is already present
                if 'social-icon location' in content:
                    continue

                def add_location(match):
                    return match.group(0) + f'\n                    <a href="{google_maps_url}" target="_blank" class="social-icon location" title="Our Location"><i class="fas fa-map-marker-alt"></i></a>'

                new_content = whatsapp_pattern.sub(add_location, content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

process_html_files(directory)
