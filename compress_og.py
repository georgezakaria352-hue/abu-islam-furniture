import codecs

def process_file(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()

    # Specifically replace only in meta tags, keep the others intact if possible, but safe to global replace
    content = content.replace(
        "https://tarkib-athath-ahsa.com/images/imported.png",
        "https://tarkib-athath-ahsa.com/images/og-image.jpg"
    )

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)

process_file('index.html')
process_file('service.html')
