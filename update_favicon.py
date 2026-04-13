import codecs

def process_file(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()

    # Change the favicon pointing to the new optimized favicon.png
    content = content.replace(
        '<link rel="icon" type="image/png" href="https://tarkib-athath-ahsa.com/images/imported.png">',
        '<link rel="icon" type="image/png" href="https://tarkib-athath-ahsa.com/favicon.png">'
    )
    content = content.replace(
        '<link rel="apple-touch-icon" href="https://tarkib-athath-ahsa.com/images/imported.png">',
        '<link rel="apple-touch-icon" href="https://tarkib-athath-ahsa.com/favicon.png">'
    )

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)

process_file('index.html')
process_file('service.html')
