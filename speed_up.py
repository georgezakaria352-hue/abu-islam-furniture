import codecs

def process_file(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        content = f.read()

    # Speed up fade-up CSS duration
    content = content.replace("transition: opacity 0.8s ease-out, transform 0.8s ease-out;", "transition: opacity 0.4s ease-out, transform 0.4s ease-out;")
    
    # Speed up fadeInPage animation
    content = content.replace("animation: fadeInPage 0.4s ease-out forwards;", "animation: fadeInPage 0.2s ease-out forwards;")
    
    # Speed up page-transition exit duration
    content = content.replace("transition: opacity 0.3s ease;", "transition: opacity 0.2s ease;")
    
    # Speed up JS setTimeout for navigation
    content = content.replace("}, 300);", "}, 200);")
    
    # Speed up stagger delays
    content = content.replace("transition-delay: 0.1s", "transition-delay: 0.05s")
    content = content.replace("transition-delay: 0.2s", "transition-delay: 0.10s")
    content = content.replace("transition-delay: 0.3s", "transition-delay: 0.15s")
    content = content.replace("transition-delay: 0.4s", "transition-delay: 0.20s")

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(content)

process_file('index.html')
process_file('service.html')
