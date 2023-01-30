""" task 7 decorators """
# def route(func):
#     def wrapper(path):
#         return 'https://www.mywebsite.com/' + func(path)
#     return wrapper

# @route
# def get_page(path):
#     return path
 
# print(get_page('about/'))
# print(get_page('products/'))


# def sort_names(func):
#     def wrapper(list_):
#         new_list = sorted(list_, key=lambda x: x[2])
#         return func(new_list)
#     return wrapper

# @sort_names
# def prefix_name(person):
#     new_list = [f'Mr. {i[0]} {i[1]}' if 'M' in i else f'Ms. {i[0]} {i[1]}' for i in person]
#     return new_list

# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
#       ('Carrie', 'Fisher', 35, 'F'),
#       ('Harrison', 'Ford', 38, 'M')]))


# def get_full_number(func):
#     def wrapper(list_):
#         new_list = []
#         for i in list_:
#             num = i.replace('0', '+996', 1)
#             new_i = num[:4] + ' ' + num[4:7] + ' ' + num[7:]
#             new_list.append(new_i)
#         return func(new_list)
#     return wrapper
    
# @get_full_number
# def sort_phone_nums(list_):
#     new_list = sorted(list_)
#     return '#'.join(new_list)

# print(sort_phone_nums(['0777987456', '0555123456', '0770369852']))




# def type_check(correct_type):
#     def wrapper(func):
#         def wrapper2(ele):
#             if type(ele) == correct_type:
#                 func(ele)
#             else:
#                 print('Неверный тип данных :(')
#         return wrapper2
#     return wrapper
    

# @type_check(int)
# def func1(num):
#     print(num*2)
 
# func1(2)
# func1({1: 'какой-то', 2: 'словарь'})

# def read_last(lines: int, filename: str):
#     with open('article.txt', 'r') as filename:
#         new_list = []
#         for i in filename.readlines(lines)[::-1]:
#              new_list.append(i)
#     return new_list
            

# print(read_last(7, 'article.txt'))

# with open('article.txt', 'r') as filename:
#         for i in filename.readlines()[::-1]:
#             print(i)


# def read_last(lines: int, filename: str):
#     with open(filename, 'r') as filename:
#         file_lines = filename.readlines()[::-1]
#     try:
#         for i in range(lines):
#             print(file_lines[i].strip('\n'))
#     except IndexError:
#         pass
    

# read_last(5, 'article.txt')

""" Files task 7 """

""" Вам дан файл article.txt
Требуется реализовать функцию longest_words(filename: str), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). """

# def longest_words(filename: str):
#     with open(filename, 'r') as filename:
#         file = filename.read().split()
#         word = []

#         first_ele = file[0]
#         for i in file:
#             if len(i) > len(first_ele):
#                 first_ele = i
#         print(first_ele)


# import json
# with open('db.json', 'r') as f:
#     res = json.loads(f.read())
#     for i in res:
#         if i['id'] == 3:
#             res.remove(i)
# with open('new_db.json', 'w') as f1:
#     res1 = json.dumps(res)
#     f1.write(res1)


# import json

# def create_new(id: int, title: str, description: str, price: int, rating: float):
#     dict_ = {
#         "id": id,
#         "title": title,
#         "description": description,
#         "price": price,
#         "rating": rating
#     }
#     with open('db.json', 'r') as f:
#         res = json.loads(f.read())
#     res.append(dict_)
#     with open('new_db.json', 'w') as f1:
#         res1 = json.dumps(res)
#         f1.write(res1)


# import json

# def get_sorted(json_filename: str):
#     with open(json_filename, 'r') as f:
#         res = json.loads(f.read())
#         list_ = []
#         def get_key():

# import json

# def get_sorted(json_filename: str):
#     with open(json_filename, 'r') as f:
#         res = json.loads(f.read())
#         list_ = (sorted(res,  key = lambda k: res[res.index(k)]['rating'],  reverse=True))
#     return list_

# import json
# def update(id: int, title: str=None, price: int=None, rating: float=None):
#     with open('new_db.json', 'w+') as f:
#         res = json.loads(f.read())
#         for i in res:
#             if id in i:
#                 i.update({'title': title})
#                 i.update({'price': price})
#                 i.update({'rating': rating})
#             elif id not in i:
#                 raise ValueError
#         f.seek(0)
#         f.write(res)


# import csv
# import datetime
# import time

# with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
#     csv_writer = csv.writer(f)
#     csv_writer.writerow(['№', 'Seconds', 'Microseconds'])
#     for i in range(1, 301):
#         csv_writer.writerow([i, datetime.datetime.now().second, datetime.datetime.now().microsecond])
#         time.sleep(0.01)

# with open('rows_300_example.csv', 'r') as f1:
#     print(f1.read())


# import requests
# response = requests.get('https://stackoverflow.com/questions')
# source = response.status_code
# print(source)


# def calc_price(filename: str):
#     with open(filename, 'r') as f:
#         summa = 0

#         for line in f.readlines():
#             arr = line.split()
#             summa += float(arr[1]) * float(arr[2])
    
#     return summa

# import csv
# def read_csv(filename: str):
#     with open('data.csv', 'r') as f:
#         dict_ = {}
#         reader = csv.reader(f)
#         for row in reader:
#             dict_.update({row[0]:row[1:]})
    
#     return dict_

# def filter_text(text_filename: str):
#     with open('forbidden_words.txt', 'r') as f1:
#         forbidden = f1.read().split()
#     with open(text_filename, 'r') as f:
#         res = f.read().split()
#         filtred = []
#         for i in res:
#             if i.lower() in forbidden:
#                 new = '*' * len(i)
#                 filtred.append(new)
#             elif i.lower().rstrip(',') in forbidden:
#                 mew = '*' * (len(i) - 1)
#                 filtred.append(mew + ',')
#             elif i.lower().rstrip('....') in forbidden:
#                 pew = '*' * (len(i) - 4)
#                 filtred.append(pew + '....')
#             elif any(item in i for item in forbidden):
#                 wew = '*' * len(i)
#                 filtred.append(wew)
#             else:
    #             filtred.append(i)
    # return ' '.join(filtred)

# def filter_text(text_filename: str):
#     with open('forbidden_words.txt') as forbidden_words, open(text_filename) as to_change:
#         pattern, text = forbidden_words.read().split(), to_change.read()
#     text_lower = text.lower()
#     for word in pattern:
#         text_lower = text_lower.replace(word, '*' * len(word))
#     result = ''.join((y, x)[x == '*'] for x, y in zip(text_lower, text))
#     return result

