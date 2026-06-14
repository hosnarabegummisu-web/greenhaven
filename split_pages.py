import os
import re

file_path = r"d:\Hosting\sites\Green Haven\index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

old_nav_pattern = r'<div class="nav-links" id="navigation-menu-links">.*?</div>'
new_nav = '''<div class="nav-links" id="navigation-menu-links">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="features.html">Features</a>
            <a href="packages.html">Packages</a>
            <a href="team.html">Team</a>
            <a href="reviews.html">Reviews</a>
            <a href="contact.html">Contact</a>
        </div>'''
html = re.sub(old_nav_pattern, new_nav, html, flags=re.DOTALL)

# Add active class for home in main file
html_home = html.replace('<a href="index.html">Home</a>', '<a href="index.html" class="active">Home</a>')
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_home)

first_comment = html.find('<!-- =========================================')
head_part = html[:first_comment]

footer_idx = html.find('<!-- Final Master Footer Bar -->')
scripts_idx = html.find('<!-- FLOATING WHATSAPP INTERACTIVE BUTTON -->')
footer_inner = html[footer_idx:scripts_idx]
scripts_part = html[scripts_idx:]

sections = {
    'about.html': ('home-section', 'About'),
    'features.html': ('features-section', 'Features'),
    'packages.html': ('packages-section', 'Packages'),
    'team.html': ('team-section', 'Team'),
    'reviews.html': ('reviews-section', 'Reviews'),
    'contact.html': ('contact-section', 'Contact')
}

for filename, (section_id, nav_name) in sections.items():
    start_str = f'<div id="{section_id}"'
    start_idx = html.find(start_str)
    
    next_comment_idx = html.find('<!-- =========================================', start_idx)
    
    if section_id == 'contact-section':
        section_start_comment = html.rfind('<!-- =========================================', 0, start_idx)
        section_content = html[section_start_comment:scripts_idx]
        page_html = head_part + section_content + scripts_part
    else:
        section_start_comment = html.rfind('<!-- =========================================', 0, start_idx)
        section_content = html[section_start_comment:next_comment_idx]
        
        custom_footer = '    <!-- =========================================\n         FOOTER SECTION\n         ========================================= -->\n    <div class="section-wrapper" style="margin-top: 40px; margin-bottom: 40px;">\n        ' + footer_inner
        page_html = head_part + section_content + custom_footer + scripts_part
        
    page_html = page_html.replace(f'<a href="{filename}">{nav_name}</a>', f'<a href="{filename}" class="active">{nav_name}</a>')
    
    out_path = os.path.join(r"d:\Hosting\sites\Green Haven", filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html)

print("Pages created successfully!")