const fs = require('fs');
const path = require('path');

const filePath = path.join('d:', 'Hosting', 'sites', 'Green Haven', 'index.html');
let html = fs.readFileSync(filePath, 'utf8');

const oldNavPattern = /<div class="nav-links" id="navigation-menu-links">[\s\S]*?<\/div>/;
const newNav = `<div class="nav-links" id="navigation-menu-links">
            <a href="index.html">Home</a>
            <a href="about.html">About</a>
            <a href="features.html">Features</a>
            <a href="packages.html">Packages</a>
            <a href="team.html">Team</a>
            <a href="reviews.html">Reviews</a>
            <a href="contact.html">Contact</a>
        </div>`;

html = html.replace(oldNavPattern, newNav);

let htmlHome = html.replace('<a href="index.html">Home</a>', '<a href="index.html" class="active">Home</a>');
fs.writeFileSync(filePath, htmlHome, 'utf8');

const firstCommentIdx = html.indexOf('<!-- =========================================');
const headPart = html.substring(0, firstCommentIdx);

const footerIdx = html.indexOf('<!-- Final Master Footer Bar -->');
const scriptsIdx = html.indexOf('<!-- FLOATING WHATSAPP INTERACTIVE BUTTON -->');
const footerInner = html.substring(footerIdx, scriptsIdx);
const scriptsPart = html.substring(scriptsIdx);

const sections = {
    'about.html': { id: 'home-section', navName: 'About' },
    'features.html': { id: 'features-section', navName: 'Features' },
    'packages.html': { id: 'packages-section', navName: 'Packages' },
    'team.html': { id: 'team-section', navName: 'Team' },
    'reviews.html': { id: 'reviews-section', navName: 'Reviews' },
    'contact.html': { id: 'contact-section', navName: 'Contact' }
};

for (const [filename, info] of Object.entries(sections)) {
    const startStr = `<div id="${info.id}"`;
    const startIdx = html.indexOf(startStr);
    
    let nextCommentIdx = html.indexOf('<!-- =========================================', startIdx);
    
    let pageHtml = '';
    
    if (info.id === 'contact-section') {
        const sectionStartComment = html.lastIndexOf('<!-- =========================================', startIdx);
        const sectionContent = html.substring(sectionStartComment, scriptsIdx);
        pageHtml = headPart + sectionContent + scriptsPart;
    } else {
        const sectionStartComment = html.lastIndexOf('<!-- =========================================', startIdx);
        const sectionContent = html.substring(sectionStartComment, nextCommentIdx);
        
        const customFooter = `    <!-- =========================================\n         FOOTER SECTION\n         ========================================= -->\n    <div class="section-wrapper" style="margin-top: 40px; margin-bottom: 40px;">\n        ` + footerInner;
        pageHtml = headPart + sectionContent + customFooter + scriptsPart;
    }
    
    pageHtml = pageHtml.replace(`<a href="${filename}">${info.navName}</a>`, `<a href="${filename}" class="active">${info.navName}</a>`);
    
    const outPath = path.join('d:', 'Hosting', 'sites', 'Green Haven', filename);
    fs.writeFileSync(outPath, pageHtml, 'utf8');
}

console.log("Pages created successfully!");
