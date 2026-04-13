import codecs

def process_file(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()

    # We only change the og:title (social media) and NOT the main <title> tag.
    content = content.replace(
        '<meta property="og:title" content="فني تركيب أثاث وايكيا بالأحساء - 0574426629 اتصل الآن">',
        '<meta property="og:title" content="أبو إسلام لتركيب الأثاث بالأحساء">'
    )

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)

process_file('index.html')
process_file('service.html')
