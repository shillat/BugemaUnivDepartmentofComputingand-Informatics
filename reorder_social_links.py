import os
import re

folder = r"C:\Users\NAIGA\Desktop\Web Programming"

# The new HTML block for the social icons (Reordered and Cleaned)
new_social_block = """                <div style="display: flex; gap: 12px; margin-bottom: 25px;">
                    <a href="https://wa.me/256709749084" target="_blank" class="social-icon whatsapp" title="WhatsApp Us"><i class="fab fa-whatsapp"></i></a>
                    <a href="mailto:info@bugemauniv.ac.ug" class="social-icon email" title="Email Us"><i class="fas fa-envelope"></i></a>
                    <a href="https://www.google.com/maps/place/Bugema+University" target="_blank" class="social-icon location" title="Our Location"><i class="fas fa-map-marker-alt"></i></a>
                </div>"""

# Regex to find the social icons div block
social_regex = r'<div style="display:\s*flex;\s*gap:\s*12px;\s*margin-bottom:\s*25px;">\s*(<a.*?</a>\s*)+</div>'

html_files = [f for f in os.listdir(folder) if f.endswith('.html')]

print(f"Starting footer update on {len(html_files)} files...")

for file in html_files:
    file_path = os.path.join(folder, file)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the block
        if re.search(social_regex, content, flags=re.DOTALL):
            new_content = re.sub(social_regex, new_social_block, content, flags=re.DOTALL)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f" - Updated: {file}")
        else:
            print(f" - Social block not found in: {file}")
            
    except Exception as e:
        print(f" - Error processing {file}: {e}")

print("Social links reordering and cleanup complete.")
