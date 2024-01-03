from selectolax.parser import HTMLParser


def get_css_selectors(html):
    parser = HTMLParser(html)
    nodes = parser.css('*')
    for node in nodes:
        print(node.css_selector)

def main():
    with open('html_content.html', 'r') as file:
        html = file.read()
    get_css_selectors(html)

if __name__ == "__main__":
    main()
