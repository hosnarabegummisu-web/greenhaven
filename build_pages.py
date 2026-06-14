import os

base_path = r"d:\Hosting\sites\Green Haven"
template_file = os.path.join(base_path, "new_ui_template.html")

with open(template_file, "r", encoding="utf-8") as f:
    template = f.read()

# Define the contents for the new pages based on the user's single page html
pages = {
    'index.html': {
        'nav_active': 'Home',
        'content': '''
  <!-- HERO -->
  <section class="hero">
    <div class="hero-text reveal">
      <div class="about-script">About</div>
      <h2>Green Heaven <span>Super Hostel</span></h2>
      <div class="ribbon">A Safe, Disciplined & Study-Friendly Home for Students</div>
      <p>
        <b>Green Heaven Super Hostel</b> is dedicated to providing students with a secure,
        comfortable and academic-focused environment. Our goal is to ensure proper discipline,
        quality accommodation, hygienic food and a peaceful atmosphere where students can focus
        on building a successful future.
      </p>
      <div class="hero-cta">
        <a href="contact.html" class="btn btn-primary" style="text-decoration:none;"><i class="fa-solid fa-graduation-cap"></i> Apply for Admission</a>
        <a href="features.html" class="btn btn-ghost" style="text-decoration:none;"><i class="fa-solid fa-building"></i> Our Facilities</a>
      </div>
    </div>
    <div class="hero-img reveal">
      <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?auto=format&fit=crop&w=1100&q=80" alt="Green Heaven Super Hostel building">
      <div class="sign">
        <div class="leaf-mark"><svg viewBox="0 0 60 60"><path d="M30 52 C14 40 10 22 22 8 C36 16 42 34 30 52Z" fill="#9fd9ab"/><path d="M34 50 C46 42 50 28 42 16 C32 24 28 38 34 50Z" fill="#dff3e3"/></svg></div>
        <h3>GREEN HEAVEN</h3>
        <small>— SUPER HOSTEL —</small>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- STATS -->
  <section class="stats reveal">
    <div class="stat"><div class="num" data-target="500">0</div><div class="lbl">Happy Students</div></div>
    <div class="stat"><div class="num" data-target="12">0</div><div class="lbl">Years of Trust</div></div>
    <div class="stat"><div class="num" data-target="98">0</div><div class="lbl">% Guardian Satisfaction</div></div>
    <div class="stat"><div class="num" data-target="24">0</div><div class="lbl">Hour Care & Security</div></div>
  </section>
'''
    },
    'about.html': {
        'nav_active': 'About',
        'content': '''
  <div class="content-wrapper reveal">
      <div class="section-title">About Us</div>
      <p style="font-size: 1.1rem; text-align: center; max-width: 800px; margin: 0 auto 30px;">
        <b>Green Heaven Super Hostel</b> is dedicated to providing students with a secure,
        comfortable and academic-focused environment. Our goal is to ensure proper discipline,
        quality accommodation, hygienic food and a peaceful atmosphere where students can focus
        on building a successful future.
      </p>
      
      <div class="divider" style="margin: 0 auto 40px;"></div>
      
      <!-- MISSION / VISION -->
      <section class="mv-grid" style="padding-bottom:10px;">
        <div class="mv-card reveal">
          <div class="mv-ico"><i class="fa-solid fa-bullseye"></i></div>
          <div>
            <h3>Our Mission</h3>
            <p>To create a safe, disciplined and motivating environment where students can grow academically and personally.</p>
          </div>
        </div>
        <div class="mv-card reveal">
          <div class="mv-ico"><i class="fa-solid fa-flag"></i></div>
          <div>
            <h3>Our Vision</h3>
            <p>To become one of the most trusted and student-friendly hostels.</p>
          </div>
        </div>
      </section>
  </div>
'''
    },
    'features.html': {
        'nav_active': 'Features',
        'content': '''
  <!-- FEATURES + STUDY IMAGE -->
  <div class="section-title reveal" style="margin-top:20px;">Our Facilities</div>
  <section class="features-zone" id="facilities">
    <div class="feature-grid reveal">
      <div class="fcard" data-title="24/7 Security" data-icon="fa-shield-halved" data-desc="Round-the-clock CCTV surveillance, biometric entry and trained security guards keep every student completely safe — day and night.">
        <div class="ico"><i class="fa-solid fa-shield-halved"></i></div><h4>24/7<br>Security</h4>
      </div>
      <div class="fcard" data-title="Army-Style Supervision" data-icon="fa-user-tie" data-desc="Strict yet caring supervision with disciplined daily routines, attendance tracking and structured study hours — building responsibility for life.">
        <div class="ico"><i class="fa-solid fa-user-tie"></i></div><h4>Army-Style<br>Supervision</h4>
      </div>
      <div class="fcard" data-title="Hygienic Food" data-icon="fa-utensils" data-desc="Fresh, nutritious and hygienically prepared meals served 3 times daily, planned by a balanced menu to keep students healthy and energetic.">
        <div class="ico"><i class="fa-solid fa-utensils"></i></div><h4>Hygienic<br>Food</h4>
      </div>
      <div class="fcard" data-title="Study-Friendly Environment" data-icon="fa-book-open" data-desc="Quiet study halls, dedicated reading hours and a peaceful atmosphere designed so students can focus entirely on academic excellence.">
        <div class="ico"><i class="fa-solid fa-book-open"></i></div><h4>Study-Friendly<br>Environment</h4>
      </div>
      <div class="fcard" data-title="High Speed WiFi" data-icon="fa-wifi" data-desc="Unlimited high-speed internet across the campus for online classes, research and learning resources — available 24 hours a day.">
        <div class="ico"><i class="fa-solid fa-wifi"></i></div><h4>High Speed<br>WiFi</h4>
      </div>
      <div class="fcard" data-title="Guardian Communication" data-icon="fa-phone-volume" data-desc="Regular updates to parents and guardians about attendance, health and academic progress through calls and messaging — full transparency.">
        <div class="ico"><i class="fa-solid fa-phone-volume"></i></div><h4>Guardian<br>Communication</h4>
      </div>
      <div class="fcard" data-title="Regular Cleaning Service" data-icon="fa-broom" data-desc="Daily housekeeping, sanitized washrooms and clean common areas — maintained by a dedicated cleaning staff for a healthy living space.">
        <div class="ico"><i class="fa-solid fa-broom"></i></div><h4>Regular<br>Cleaning Service</h4>
      </div>
      <div class="fcard" data-title="Modern Student Facilities" data-icon="fa-house-laptop" data-desc="Washing machines, refrigerators, water purifiers, generators and common rooms — every modern amenity a student needs under one roof.">
        <div class="ico"><i class="fa-solid fa-house-laptop"></i></div><h4>Modern Student<br>Facilities</h4>
      </div>
    </div>

    <div class="study-col reveal">
      <div class="study-img">
        <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1000&q=80" alt="Students studying together">
      </div>
      <div class="quote-card">
        <span class="q">&ldquo;</span>
        <p>We don't just provide a place to stay, we provide a place to grow, learn and succeed.&rdquo;</p>
        <div class="qline"><span></span>
          <div class="leaf-mark"><svg viewBox="0 0 60 60"><path d="M30 52 C14 40 10 22 22 8 C36 16 42 34 30 52Z" fill="#9fd9ab"/><path d="M34 50 C46 42 50 28 42 16 C32 24 28 38 34 50Z" fill="#dff3e3"/></svg></div>
        <span></span></div>
      </div>
    </div>
  </section>
'''
    },
    'contact.html': {
        'nav_active': 'Contact',
        'content': '''
  <div class="section-title reveal" style="margin-top:20px;">Contact & Admission</div>
  <!-- ADMISSION FORM -->
  <section class="admission reveal" id="admission">
    <div>
      <h3><i class="fa-solid fa-graduation-cap"></i> Book a Seat Today</h3>
      <p>Limited seats available! Fill out the form and our admission team will contact you within 24 hours to schedule a campus visit.</p>
      <ul class="adm-list">
        <li><i class="fa-solid fa-circle-check"></i> AC & Non-AC rooms available</li>
        <li><i class="fa-solid fa-circle-check"></i> 2, 3 & 4 seater room options</li>
        <li><i class="fa-solid fa-circle-check"></i> Free campus tour for guardians</li>
        <li><i class="fa-solid fa-circle-check"></i> Monthly & yearly packages</li>
      </ul>
      
      <div style="margin-top: 30px;">
          <h4 style="color:var(--green-800); margin-bottom: 10px;">Contact Info</h4>
          <p style="margin-bottom: 5px;"><i class="fa-solid fa-phone" style="color:var(--green-600);width:20px;"></i> 01323-581036</p>
          <p style="margin-bottom: 5px;"><i class="fa-brands fa-whatsapp" style="color:var(--green-600);width:20px;"></i> Chat on WhatsApp</p>
          <p><i class="fa-solid fa-envelope" style="color:var(--green-600);width:20px;"></i> greenheavensuperhostel@gmail.com</p>
      </div>
    </div>
    <form class="form-grid" id="admForm" novalidate>
      <div class="fld"><label>Student Name *</label><input type="text" id="fName" placeholder="Full name"></div>
      <div class="fld"><label>Phone Number *</label><input type="tel" id="fPhone" placeholder="01XXXXXXXXX"></div>
      <div class="fld"><label>Institution</label><input type="text" id="fInst" placeholder="College / University"></div>
      <div class="fld"><label>Room Preference</label>
        <select id="fRoom">
          <option>2 Seater (AC)</option>
          <option>2 Seater (Non-AC)</option>
          <option selected>3 Seater (Non-AC)</option>
          <option>4 Seater (Non-AC)</option>
        </select>
      </div>
      <div class="fld full"><label>Message (optional)</label><textarea id="fMsg" rows="3" placeholder="Any question for us?"></textarea></div>
      <div class="form-msg" id="formMsg"></div>
      <div class="full"><button type="submit" class="btn btn-primary" style="width:100%;justify-content:center;"><i class="fa-solid fa-paper-plane"></i> Submit Application</button></div>
    </form>
  </section>
'''
    }
}

for filename, data in pages.items():
    page_html = template.replace('<!-- INJECT_CONTENT_HERE -->', data['content'])
    
    # Set active navigation correctly
    if filename == "index.html":
        # It's already active in the template
        pass
    else:
        # Remove active from Home
        page_html = page_html.replace('<a href="index.html" class="active">Home</a>', '<a href="index.html">Home</a>')
        # Add active to the current page
        old_link = f'<a href="{filename}">{data["nav_active"]}</a>'
        new_link = f'<a href="{filename}" class="active">{data["nav_active"]}</a>'
        page_html = page_html.replace(old_link, new_link)
    
    out_path = os.path.join(base_path, filename)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page_html)

print("Main pages successfully created!")
