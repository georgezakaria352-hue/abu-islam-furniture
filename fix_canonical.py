import codecs

def process_file(filepath, canonical_url):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()

    # Add canonical tag before the first meta tag or in head
    canonical_tag = f'<link rel="canonical" href="{canonical_url}">\n    '
    if '<link rel="canonical"' not in content:
        content = content.replace('<head>', '<head>\n    ' + canonical_tag)

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)

process_file('index.html', 'https://tarkib-athath-ahsa.com/')
process_file('service.html', 'https://tarkib-athath-ahsa.com/service.html')
