import codecs
import re

def process_file(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()
    
    # 1. Update URLs
    content = content.replace(
        "https://raw.githubusercontent.com/georgezakaria352-hue/abu-islam-furniture/main/images/imported.png",
        "https://tarkib-athath-ahsa.com/images/imported.png"
    )
    content = content.replace(
        "https://abu-islam-furniture.vercel.app",
        "https://tarkib-athath-ahsa.com"
    )
    
    # 2. Add Favicons
    favicon_tags = """<meta name="format-detection" content="telephone=no">
    <!-- Favicon & Social Meta -->
    <link rel="icon" type="image/png" href="https://tarkib-athath-ahsa.com/images/imported.png">
    <link rel="apple-touch-icon" href="https://tarkib-athath-ahsa.com/images/imported.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:image" content="https://tarkib-athath-ahsa.com/images/imported.png">
    <meta name="twitter:title" content="أبو إسلام لخدمات تركيب الأثاث بالأحساء">"""
    
    content = content.replace('<meta name="format-detection" content="telephone=no">', favicon_tags)
        
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)

process_file('index.html')
process_file('service.html')
