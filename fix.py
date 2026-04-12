import codecs
import re
import os

def process_file(filepath, replacements):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()
    
    for r in replacements:
        content = re.sub(r[0], r[1], content)
        
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)

idx_replacements = [
    (r'<meta name="viewport" content="width=device-width, initial-scale=1.0">',
     '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="format-detection" content="telephone=no">'),
    
    (r'onclick="window\.location\.href=\'service\.html\?id=(srv\d+)\'"',
     r'onclick="navigateToService(\'service.html?id=\1\')"'),
     
    (r'body\s*{[^}]*}',
     """body {
            font-family: var(--font-ar);
            background-color: var(--background);
            color: var(--text-main);
            line-height: 1.6;
            overflow-x: hidden;
            transition: all 0.3s ease;
            animation: fadeInPage 0.4s ease-out forwards;
        }
        @keyframes fadeInPage {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .page-transitioning {
            opacity: 0;
            transform: translateY(-10px);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }"""),
        
    (r'\.nav-links \{\s*display: none;\s*flex-direction: column;\s*position: absolute;\s*top: 100%; left: 0; width: 100%;\s*background: rgba\(255, 255, 255, 0\.98\);\s*box-shadow: var\(--shadow-md\);\s*padding: 20px; text-align: center; gap: 20px;\s*border-bottom: 2px solid var\(--accent\);\s*\}',
     """.nav-links { 
                display: flex; 
                flex-direction: column; 
                position: absolute; 
                top: 100%; left: 0; width: 100%; 
                background: rgba(255, 255, 255, 0.98); 
                box-shadow: var(--shadow-md); 
                padding: 20px; text-align: center; gap: 20px;
                border-bottom: 2px solid var(--accent);
                
                visibility: hidden;
                opacity: 0;
                transform: translateY(-20px);
                transition: opacity 0.3s ease, transform 0.3s ease, visibility 0.3s;
            }"""),
            
    (r'\.nav-links\.active \{\s*display: flex;\s*\}',
     """.nav-links.active { 
                visibility: visible;
                opacity: 1;
                transform: translateY(0);
            }"""),
            
    (r'<p><span data-key="footerPhone">.*?</span>\s*<strong style="direction: ltr; display: inline-block;">\+966 574426629</strong></p>',
     '<p style="margin-top: 10px;"><span data-key="footerPhone">التواصل المباشر:</span> <a href="tel:+966574426629" style="color: white; text-decoration: none; font-weight: bold; direction: ltr; display: inline-block;">+966 574426629</a></p>'),
     
    (r'fadeElements\.forEach\(el => fadeObserver\.observe\(el\)\);',
     """fadeElements.forEach(el => fadeObserver.observe(el));

        // --- Page Navigation Animation ---
        function navigateToService(url) {
            document.body.classList.add('page-transitioning');
            setTimeout(() => {
                window.location.href = url;
            }, 300);
        }""")
]

srv_replacements = [
    (r'<meta name="viewport" content="width=device-width, initial-scale=1.0">',
     '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta name="format-detection" content="telephone=no">'),
     
    (r'body\s*{[^}]*}',
     """body {
            font-family: var(--font-ar);
            background-color: var(--background);
            color: var(--text-main);
            line-height: 1.6;
            overflow-x: hidden;
            transition: all 0.3s ease;
            animation: fadeInPage 0.4s ease-out forwards;
        }
        @keyframes fadeInPage {
            0% { opacity: 0; transform: translateY(10px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .page-transitioning {
            opacity: 0;
            transform: translateY(-10px);
            transition: opacity 0.3s ease, transform 0.3s ease;
        }"""),
        
    (r'href="index\.html"',
     r'href="javascript:void(0)" onclick="navigateToService(\'index.html\')"'),
     
    (r'</script>\s*</body>',
     """    function navigateToService(url) {
            document.body.classList.add('page-transitioning');
            setTimeout(() => { window.location.href = url; }, 300);
        }
    </script>
</body>""")
]

process_file('index.html', idx_replacements)
process_file('service.html', srv_replacements)

