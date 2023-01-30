# слово - word

# dict
# словарь - изменяемый, итерируемый тип данных. Вместо индекса имеет ключи. Состоит из пар - ключ: значение

# Ключи могут быть только неизменяемыми типами данных и должны быть уникальными

# Значениями могут быть любые типы данных

# литералы - {}

# passport = {'name': 'Meerim', 'last_name': 'Kairatovna', 'age': 25, 'gender': 'F'}

# print(passport['name'])
# passport['last_name']
# passport['age']
# passport['gender']
# passport['license'] # KeyError

# passport['license'] = 'Can drive B'
# passport['license'] # 'Can drive B'
# print(passport)


""" Создание словаря """
# dict_ = {1: 10}

# dict_2 = dict(name='Vasya', age=23)
# print(dict_2)

# dict_3 = dict([('name', 'Vasya'), ('age', 23)])
# print(dict_3)

# dict_4 = dict.fromkeys(['a', 'b'], 10)
# print(dict_4)


# human = {
#     'name': 'Bakai',
#     'age': 25,
#     'friends': ['Sasha', 'Artur'],
#     'name': 'Bakyt'
# }
# print(human)

# a = 1
# a = 2
# a # 2

# dict_5 = {
#     'name': 'Ak-Maral',
#     [1, 2]: 'ERROR' # TypeError
# }

""" Получение значений из словаря """
# car = {
#     "marka": "Toyota",
#     "model": "Camry",
#     "color": "black",
#     "volume": 3.5,
#     "year": 2012
# }
# print(car['marka']) # Toyota
# print(car['kuzov']) # KeyError

# print(car.get('marka')) # Toyota
# print(car.get('kuzov')) # None
# print(car.get('kuzov', 'Такого ключа нет!')) # Такого ключа нет!

# print(car.setdefault('year'))
# print(car.setdefault('kuzov', 'Sedan'))
# print(car)


""" Добавление данных в словарь """
# house = {
#     'Color': 'White',
#     'category': 'elite',
#     'rooms': 4,
#     'warmness': True
# }

# house['area'] = '30x40'
# # print(house)

# house.update({'floor': 3, 'door': 'wooden'})
# # print(house)

# house.update([['square', '12-mkr'], ['pool', False]])
# # print(house)

# house.setdefault('pool', False)
# print(house)

# house['color'] = 'yellow'

# house.update({'rooms': 6})
# print(house)

""" Удаление данных из словаря """
# movie = {
#     'title': 'Вторая жизнь Уве',
#     'country': 'Швеция',
#     'year': 2015,
#     'genre': ['Comedy', 'Drama']
    
# }

# deleted_key = movie.pop('country')
# print(movie)
# print(deleted_key)

# deleted_pair = movie.popitem()
# print(deleted_pair)
# print(movie)

# del movie['title']
# print(movie)

# movie.clear()
# print(movie)



""" Перебор словаря """
# game = {
#     'title': 'Fable The Lost Chapters',
#     'year': 2006,
#     'author': 'Peter',
#     'category': 'RPG'
# }
# for key in game:
#     print(key)

# for key in game:
#     print(game[key])

# print(game.values()) # - .values() возвращает список значений словаря в виде dict_values
# for value in game.values():
#     print(value)

# list(game.values())[1] # 2006


# print(game.keys()) # .keys() возвращает список ключей словаря в виде dict_keys

# for key in game.keys():
#     print(key)


# print(game.items()) # .items() возвращает пару ключ-значение в виде списка из кортежей с типом dict_items

# a = 5
# b = 10

# a, b = 5, 10

# key, value = ('title', 'GTA')

# for key, value in game.items():
#     print(f'Ключ {key}, значение {value}')



# human = {
#     'name': 'Aliya',
#     'age': 22,
#     'gender': 'F',
#     'friends': ['Melis', 'Begimay']
# }
# human2 = human.copy()
# # print(id(human))
# # print(id(human2))
# human2['friends'].append('Aidai')
# print(human2['gender'])
# print(human['friends'])
# print(human2)
# print(human)


# from copy import deepcopy
# human3 = deepcopy(human)
# print(human3['friends'] is human)


# person = {
#     'name': 'Abdul',
#     'age': 22,
#     'passport': {
#         'ID': 216515612154,
#         'nationality': 'kyrgyz'
#     },
#     'driver_license': {
#         'category': 'B',
#         'year': 2011
#     }
# }

# print(person['passport']['nationality'])



# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# for k, v in list(a.items()):
#     if v % 2 == 0:
#         a[k] = 2
# print(a)
