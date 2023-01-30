import csv
import json

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag


URL = 'https://www.sulpak.kg/'


def get_html(url: str, category: str, params: str=''):
    html = requests.get(
        url=url + 'f/' + category,
        params=params,
        verify=False
    )
    return html.text


def get_cards_from_html(html: str) -> ResultSet:
    soup = BeautifulSoup(html, 'lxml')
    cards = soup.find_all('div', class_='product__item-inner')
    return cards


def parse_data_from_cards(cards: ResultSet) -> list:
    result = []
    for card in cards:
        try:
            title = card.find('div', class_='product__item-name').text
        except AttributeError:
            title = 'Нет названия'
        try:
            price = card.find('div', class_="product__item-price").text
        except AttributeError:
            price = 'Нет цены'
        try:
            description = card.find('div', class_="product__item-description").text
        except AttributeError:
            description = 'Нет описания'
        try:
            in_stock = card.find('div', class_="product__item-showcase").text
        except AttributeError:
            in_stock = 'Нет в наличии'
        try:
            img_link = card.find('img', class_="image-size-cls").get('src')
        except AttributeError:
            img_link = 'Нет картинки'

        obj = {
            'title': title,
            'price': price,
            'in_stock': in_stock,
            'description': description,
            'image_link': img_link
        }
        result.append(obj)
    return result


def write_to_csv(data: list, filename: str) -> None:
    fieldnames = data[0].keys()
    with open(f'{filename}.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def get_last_page(html: str) -> int:
    soup = BeautifulSoup(html, 'lxml')
    last_page = soup.find('div', class_='pagination').get('data-pagescount')
    return int(last_page)



def main() -> None:
    result = []
    html = get_html(URL, 'smartfoniy')
    last_page = get_last_page(html)
    for page in range(1, last_page+1):
        html = get_html(URL, 'smartfoniy', params=f'page={page}')
        cards = get_cards_from_html(html)
        result_from_page = parse_data_from_cards(cards)
        result.extend(result_from_page)
    write_to_csv(result, 'smartphones')



if __name__ == '__main__':
    main()

