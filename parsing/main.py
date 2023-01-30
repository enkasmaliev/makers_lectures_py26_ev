# from bs4 import BeautifulSoup
# from bs4.element import ResultSet, Tag

# with open('template/index.html', 'r') as html:
#     html_code = html.read()
#     soup = BeautifulSoup(html_code, 'html.parser')
#     p = soup.find_all('p')
#     # for tag in p:
#     #     print(tag.text)
#     # p_a1 = soup.find_all('p', class_='a1')
#     # print(p_a1)
#     # span = soup.find('span').find('p').text
#     # print(span)
#     # image = soup.find('img').get('src')
#     # print(image)


# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://enter.kg/').text
# soup = BeautifulSoup(response, 'html.parser')

# menu = soup.find_all('li', class_='VmClose')
# category_list = []
# for category in menu:
#     category_list.append(category.a.text)
# center = soup.find_all('span', class_="category-product-count")
# for category in center:
#     category_list.append(category.text.strip())

# def find_category(categories: list, keyword: str):
#     new_list = []
#     for i in categories:
#         if keyword.lower() in i.lower():
#             new_list.append(i)
#     return new_list

# # print(category_list)
# print(find_category(category_list, 'Ноутбуки'))

# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://www.imdb.com/chart/top').text
# soup = BeautifulSoup(response, 'html.parser')

# movies = soup.find_all('td', class_="titleColumn")
# title_list = []
# title_links = []
# for movie in movies:
#     title_list.append(movie.a.text)
#     title_links.append('https://www.imdb.com' + movie.a.get('href'))

# def get_link(title_list, name):
#     global title_links
#     for title in title_list:
#         if name.lower() in title.lower():
#             film = title_list.index(title)
#             return title_links[film]
# print(get_link(title_list, 'END'))