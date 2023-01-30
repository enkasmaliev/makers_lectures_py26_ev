""" strings (строки) """

# str()

# string - неизменяемый, упорядоченный, индексируемый, итерируемый тип данных

# string = "Hello"
# string2 = 'Hello'

# doc_string = """ Строка документации - используется для описания кода в несколько строк """
# doc_string = ''' Строка документации '''

# # string3 = 'Hello, i'm student # Error

# string4 = "Hello, i'm student"
# string5 = 'Hello, i\'m student' # Экранирование

# str1 = 'Hello'
# str2 = 'World'
# print(str1 + str2) #HelloWorld 
#Конкатенация - склеивание/сложение строк


# frog = 'Quak'
# print(frog * 3) #QuakQuakQuak


""" Функции и методы строк """

# greeting = 'Hello everyone'

# print(len(greeting)) # 14
# len(x) - подсчитывает количество элементов
# print(dir(greeting))
# dir(x) - возвращает список методов переданного объекта


# Метод - функция, принадлежащая определенному типу данных и может быть вызвана только через объект


# my_str = 'Hello world'

# print(my_str.lower())
# print(my_str.upper())
# print(my_str.split()) # str.split() -> возвращает список из строк по делителю, если не передавать делитель - по пробелу

# my_str2 = '    #hello #world    '

# my_str2.title() # Hello World
# my_str2.capitalize() # Hello world
# my_str2.count('l') # 3
# my_str2.replace('o', 'm') # hellm wmrld
# print(my_str2.strip()) # удаляет пробел с двух сторон
# my_str2.lstrip() # слева
# my_str2.rstrip() # справа


# string6 = 'Some string with 5 words'
# string6.isalpha() # False
# string6.isdigit() # False
# string6.isalnum() # False
# string6.startswith('S') # True
# string6.endswith('ds') # True

# # in
# 'with' in string6 # True


""" Форматирование/интерполяция строк """

# name = 'Айгуль'
# party = input('party ')

# inv1 = 'Дорогой(-ая) %s, приглашаем тебя на %s' % (name, party)
# print(inv1)

# inv2 = 'Дорогой(-ая) {a1}, приглашаем тебя на {b2}' .format(a1=name, b2=party)
# inv3 = f'Дорогой(-ая) {name}, приглашаем тебя на {party}'


""" Индексы и срезы """

# str10 = 'makers'
# str10[0] # 'm'
# Индексы - порядковый номер элемента в строке/списке/кортеже. В программировании индексация начинается с нуля
# 'hello'
#  01234
# -5-4-3-2-1

# string2 = 'house'
# string2[len(string2)-1] # 'e'
# print(string2[-1]) # 'e'


# string3 = 'hello world'
# start = 0
# stop = 5
# step = 1
# print(string3[start:stop:step])
# print(string3[::])
# print(string3[::-1])


""" Экранирование строк """

# print('Hello\nworld')
# """ 
# Hello
# World
# """
# print('Hello\n\tworld')
# """ 
# Hello
#     World
# """
# path = "C:\\Users\\new\\tanks"
# print(path)

# string = 'hello Nazik'
# string1 = (string + '\n') * 3
# print(string1)