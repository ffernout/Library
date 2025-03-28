import requests
from bs4 import BeautifulSoup as BS
from django.conf.locale import bs
from django.template.defaultfilters import title

URL = 'https://mybook.ru/catalog/'


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_data(html):
    soup = BS(html, features='html.parser')
    items = soup.find_all('div', class_='sc-1hf4y1s-1 kHOKic swiper-container swiper-container-initialized swiper-container-horizontal swiper-container-free-mode')
    parser_book = []
    for item in items:
        title_element = item.find('div', class_='lnjchu-1 fkvOUV sc-7dmtki-5 eKTHUu')
        title = title_element.get_text() if title_element else None
        href = item.find('a').get('href') if item.find('a') else None
        parser_book.append({
            'title': title,
            'href': href
        })
    return parser_book


def parse_book(parser_book):
    response = get_html(URL)
    if response.status_code == 200:
        parse_book2 = []
        for book in range(1, 2):
            response = get_html(f"https://mybook.ru/catalog/", params={'book': book})
            if response.status_code == 200:
                parse_book2.append(get_data(response.text))
                return parse_book2
    else:
            raise Exception('error')
