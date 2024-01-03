import requests
from selectolax.parser import HTMLParser


def scrape_page(url):
    response = requests.get(url)
    html = HTMLParser(response.text)
    return html

def extract_deals(html):
    deals = []
    for deal in html.css('li.list_item_wrapper'):
        title = deal.css_first('h2.offer_title a').text()
        dealer = deal.css_first('p.offer_dealer a').text()
        deals.append({'title': title, 'dealer': dealer})
    return deals

def extract_pagination(html):
    pagination = []
    for page in html.css('ul.pagination_pages a'):
        pagination.append(page.attrs['href'])
    return pagination

def main():
    url = 'https://www.redflagdeals.com/deals/'
    while url:
        html = scrape_page(url)
        deals = extract_deals(html)
        print(deals)
        pagination = extract_pagination(html)
        url = pagination[0] if pagination else None

if __name__ == "__main__":
    main()
