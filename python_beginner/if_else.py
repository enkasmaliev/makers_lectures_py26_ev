""" Условные выражения (if-elif-else) """

# bool() = неизменяемый тип данных, который имеет всего 2 значения: True, False
    # булевый тип данных bool
# 10 > 2 # True
# > - больше
# < - меньше
# <= - less or equal
# >= - more or equal
# != - неравенство
# == - равенство

# print(25 == 23) # False
# print(25.0 == 25) # True
# print('Apple' > 2) # Error


# print(bool(0)) # False
# print(bool(1)) # True

# print(bool(2)) # True
# print(bool(-2)) # True

# print(bool('it')) # True
# print(bool('')) # False

# bool([]) # False
# bool({}) # False
# bool(set()) # False
# bool(None) # False

""" if """

# num = 10
# print(num)

# num = 15
# if num > 10:
#     print('Number is bigger than 10')

""" if else """
# num = 15
# if num > 20:
#     print('num bigger than 20')
# else:
#     print('num less than 20')


# temperature = 40
# if temperature < 20:
#     print('cold')
# else:
#     if temperature < 30:
#         print('warm')
#     else:
#         if temperature > 35:
#             print('hot')


""" if elif else """
# temperature = 40
# if temperature < 20:
#     print('cold')
# elif temperature < 30:
#     print('warm')
# elif temperature > 35:
#     print('hot')
# else:
#     print('not right temperature')


# num2 = 15
# if num2 < 20:
#     print('num2 < 20')
# elif num2 > 10:
#     print('num2 > 10')

# num2 = 15
# if num2 < 20:
#     print('num2 < 20')
# if num2 > 10:
#     print('num2 > 10')


# mark = input('Введите оценку от 1 до 5: ')
# if mark.isdigit():
#     mark = int(mark)
#     msg = ''
#     if mark == 5:
#         msg = 'Ты молодец!'
#     elif mark == 4:
#         msg = 'Хорошо!'
#     elif mark <= 3:
#         msg = 'подтяни предмет'
#     print(msg)
# else:
#     print('Вы ввели не число!')


# """ and, or, not """
# age = 15
# if age >= 18 and age < 28:
#     print('Входите')
# else:
#     print('Входа нет')

# False # False
# True # True
# False and False # False
# True and True # True
# False and True # False
# True and False # False

# False or False # False
# True or True # True 
# False or True # True
# True or False # True

# not True # False
# not False # True
# (False or True) and (False and False) # False




""" is, ==, in """
# a = 10
# print(a is 10)

# a = 300
# b = 300
# print(id(a))
# print(id(b))
# print(a is b) # False
# print(a == b) # True

# string = 'hello world'
# print('world' in string) # True

""" Тернарный оператор """
# msg = input('Введите сообщение ')
# if len(msg) > 10:
#     print('Сообщение длиннее 10')
# else:
#     print('Сообщение короче 10')
# msg = input('Введите сообщение ')
# res = 'сообщение длиннее 10' if len(msg) > 10 else "Сообщение короче 10"
# print(res)

# if условие:
#     действие 1
# else:
#     действие 2

# действие 1 if условие else действие 2

# if условие1:
#     действие1
# elif условие2:
#     действие2
# else:
#     действие3
