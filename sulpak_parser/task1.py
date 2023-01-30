# import requests
# from bs4 import BeautifulSoup
# def getTitle(url):
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'lxml')
#     header = soup.find('h1')
#     if header != None:
#         return header
#     else:
#         return "Title could not be found"

# # print(getTitle('http://www.example.com/'))
# print(getTitle('https://www.w3resource.com/'))