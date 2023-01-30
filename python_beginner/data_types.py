# 8 основных типа данных, которые делятся на 2 типа:
# 1) изменяемые типы данных
# 2)неизменяемые типы данных

# Типы данных:
# 1) int - целыйчисловой тип данных:
#     a) float - числа с плавающей точкой
#     б) complex - числа с буквенным выражением (1234123n)
# 2) str - строковый тип данных ("строка")
# 3) bool - булевый типа данных/логический (True/False)
# 4) list - список ({[]})
# 5) tuple - кортеж/неизменяемый список
# 6) set - множество ({})
# 7) dict - словарь ({})
# 8) NoneType - тип данных для обозначения отсутствия значения (None)

# Изменяемые (mutable):
# list
# dict
# set

#print("Hello world")

# a = 1
# print(a)

# - это однострочный комментарий
"""" 
Многострочный
Очень длинный
Комментарий
"""

""" Переменные """
a = 10  # Ok
# !$%^myvar = 10 # Error
# 12myvar = 10 # Error
# Название переменной не должно начинаться со спец символов и цифр

#my_num = 20 # Ok - snake_case
# myNUm = 20 # Ok - camel_case

# my-num = 1 
# my num = 1 # Error

# Название переменной не должно совпадать с названиями ключевых слов Python
# print = 10 # Error
# if = 10 # Error


# MY_CONST = 10 # Обозначение константы

# Давайте своим переменным осмысленные и логичные имена
# num = 10
# a = 10


""""
Функции для вывода(print) и ввода(input) данных в терминал
"""

# print() # - функция для вывода информации в терминал
# input() # - функция для ввода информации с клавиатуры/в терминал. По умолчанию дает сторчный тип данных (str)
# type() # - функция для вывода типа переданных в нее данных 

# () - обозначают вызов функции, также служит вместилищем для передачи данных

# num = 10
# print(num)
# print(type(num))

# info = input('Введите число') # 23 -> "23" , # Hello world -> "Hello world"
# print(type(info))

# get_num = int(input())
# print(type(get_num))


# get_first_num = int(input('1 '))
# get_second_num = int(input('2 '))
# result = get_first_num + get_second_num
# print("Ответ будет", result)

#Tasks

# Task 1

# day = int(input('Day of birth: '))
# month = int(input('Month of birth: '))
# year = int(input('Year of birth: '))
# print(day + month + year)

# Task 2

# pay = 600
# skid = int(input('Введите скидку: '))
# summa = int(pay * (100 - skid) / 100)
# print("Оставшаяся сумма платежа составляет: ", str(summa) + '$')

# Task 3 
# import math

# radius = int(input('Type radius of a circle: '))

# square = (math.pi) * (radius ** 2)
# perimetr = (math.pi) * 2 * radius
# print('An area of a circle is: ', round(square, 2), '\n'
#     'A length of a circle is:', round(perimetr, 2))













