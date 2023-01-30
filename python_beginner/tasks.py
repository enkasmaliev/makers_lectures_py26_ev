""" Дана переменная t с целочисленным значением веса муки в 255 тонн, найдите сколько это будет в граммах, килограммах, центнерах, распечатайте результат в терминале """

# t = 255
# g = t * 1_000_000
# kg = t * 1_000
# ts = t * 10
# print(g, kg, ts)

# string1 = 'America'
# string2 = 'Japan'
# string3 = string1[0] + string2[0] + string1[int(len(int(string1)/2))] + string2[int(len(int(string2)/2))] + string1[-1] + string2[-1]
# print(string3)

""" if else Task 7 """
# x = 11
# y = 33
# z = 32
# if x == y and y == z and z == x:
#     print(3)
# elif (x == y) or (z == x) or (y == z):
#     print(2)
# else:
#     print(0)

""" if else Task 8 """
# x = int(input())
# y = int(input())
# z = x // y
# if x % y == 0:
#     print('x делится на y\nЧастное:', z)
# else:
#     print('x не делится на y\nЧастное:', z, '\nОстаток:', x % y)

""" if else Task 16" """

# a = int(input())
# b = int(input())
# c = int(input())
# if a > b > c:
#     print(a, b, c)
# elif b > a > c:
#     print (b, a, c)
# elif c > a > b:
#     print(c, a, b)


# month = int(input())
# if month not in range(1, 13):
#     print("Такого месяца нет")
# elif month == 1 or month ==2 or month ==12:
#     print("зима")
# elif month == 3 or month ==4 or month ==5:
#     print("весна")
# elif month == 6 or month ==7 or month ==8:
#     print("лето")
# elif month == 9 or month ==10 or month ==11:
#     print("осень")


# a = int(input())
# b = int(input())
# c = int(input())

# if a + b > c:
#     print('yes')
# elif b + c > a:
#     print('yes')
# elif a + c > b:
#     print('yes')
# elif a == 0 and b == 0 and c == 0:
#     print('no')
# else:
#     print('no')


# a = int(input())
# b = int(input())
# c = int(input())

# if (a**2 == b**2+c**2) and (b**2 == a**2 + c**2) and (c**2 == a**2 + b**2):
#     print('rectangular')
# elif (a**2 < b**2 + c**2) and (b**2 < a**2 + c**2) and (c**2 < a**2 + b**2):
#     print("acute")
# elif (a**2 > b**2 + c**2) and (b**2 > a**2 + c**2) and (c**2 > a**2 + b**2):
#     print("obtuse")
# else:
#     print('impossible')


""" TAsk 21 if else 
Даны три стороны треугольника a, b, c (inputs). Определите тип треугольника с заданными сторонами.
Выведите одно из четырех слов: rectangular для прямоугольного треугольника, acute для остроугольного треугольника, obtuse для тупоугольного треугольника или impossible, если треугольника с такими сторонами не существует.
"""
# a1, b1, c1 = int(input()), int(input()), int(input())
# c = max(a1, b1, c1)
# b = min(a1, b1, c1)
# a = sum([a1, b1, c1]) - min(a1, b1, c1) - max(a1, b1, c1)
# if c >= a + b:
#     print('impossible')
# elif c**2 == a**2 + b**2:
#     print('rectangular')
# elif c**2 < a**2 + b**2:
#     print('acute')
# elif c**2 > a**2 + b**2:
#     print('obtuse')
# else:
#     print('impossible')


""" Для данного числа n (input, <100) закончите фразу “На лугу пасется...” одним из возможных продолжений: “n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”. """

# n = int(input())
# n < 100
# if n == 1, 2, 3



# data = input('Введите имя, фамилию и возраст через пробел: ')
# name = data[0]
# surname = data[1]
# age = data[-1]

# name = input('Введите имя: ')
# surname = input ('Last nime: ')
# age = input('age: ')


# name = name.replace('a', '')
# surname = '*'.join(list(surname))
# print((name + surname) * int(age))

# name = input('Vvedite stroku: ').lower()
# a = name.count('a')
# i = name.count('i')
# o = name.count('o')
# u = name.count('u')
# y = name.count('y')
# e = name.count('e')
# print(f'V vashei stroke nasshitano {a+i+o+u+y+e} strok')


# name = input('Vvedite username: ')
# mid = int(len(name)/2)
# username = name[:mid] + '&' + name[mid:] + '$'
# print('Vam sgeneririovan parol', username.swapcase())



# labels = ['Lexus', 'Toyota', 'Nissan', 'BMW']
# for x in labels:
#     print(f'I like  brand {x}')

""" Task 11 if else """
# num = int(input())
# chr(num)
# if chr(num).isalpha():
#     print(f'Это буква "{chr(num)}"')
# else:
#     print(f'Это не буква, а символ "{chr(num)}"')

""" Task 15 if else """
# string = '123456'
# if string[0] + string[1] + string[2] == string[3] + string[4] + string[5]:
#     print('да')
# else:
#     print('нет')


""" Task 20 if else """
# a = int(input())
# b = int(input())
# c = int(input())
# if (a + b > c and a + c > b and b + c > a) and a >0 and b > 0 and c > 0:
#     print('yes')
# else:
#     print('no')



""" Task 22 if else """
# n = int(input())
# if n >= 11 and n <= 14:
#         print('На лугу пасется', n, 'коров')
# else:
#         temp = n % 10
#         if temp == 0 or (temp >= 5 and temp <= 9):
#                 print('На лугу пасется', n, 'коров')
#         if temp == 1:
#                 print('На лугу пасется', n, 'корова')
#         if temp >=2 and temp <=4:
#                 print('На лугу пасется', n, 'коровы')

""" Task 24 """

# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == y1 and x2 == y2 and x1 == (8 - x1) and y1 = (8 - y1) and x2 == (8 - x2) and y2 == (8 - y2):
#     print('YES')
# else:
#     print('NO')



""" List Task 3 """
# name_of_list = ['Helloworld!']
# center = len(name_of_list[0]) // 2 + len(name_of_list[0]) % 2
# print(center)
# new_list = name_of_list[0][(center):] + name_of_list[0][:(center)]
# print(list(new_list))

# list_ = ['world', 'hello']
# new_list = list_.sort()
# print(new_list)

""" Task 4 lists """
# list_ = ['world', 'hello'] 
# list_.remove('hello')
# new_list = list_.insert(0, 'hello')
# print(new_list)

# list_ = ['world', 'hello']
# list_.reverse()
# new_list = list_
# print(new_list)

# """ Task 6 """
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for res in nums:
#     if res < 5:
#         print(list(res))

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for num in list_:
#     str(num)
#     new_list.append(num)
# print(new_list)



# list1 = [11, 23, 45, 7, 9]
# list2 = [21, 4, 16, 8, 10]
# list3 = list1 + list2
# print(sum(list3))


# list_ = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# number = 8
# length = []
# for element in list_:
#     if element == number:
#         length.append(element)
# print(len(length))


# list_ = []
# tuple_ = ()
# values = input()
# ints_as_strs = values.split(',')
# list_ = list(ints_as_strs)
# tuple_ = tuple(list_)
# print(list_)
# print(tuple_)


# def large(arr): 
#     max_ = arr[0]
#     for ele in arr:
#         if ele < max_:
#            max_ = ele
#     return max_ 


# list1 = [1,4,5,2,6]
# result = large(list1)
# print(result)  # вернется 6


# cleared_tuples = ()
# tuples = [(), ('ram','15','8'), (), ('laxman', 'sita')]
# for num in tuples:
#     if num != ():
#         tuples.append(num)
# print(cleared_tuples)

# value1 = input().split()
# value2 = input().split()
# value3 = input().split()
# value4 = input().split()
# value5 = input().split()
# surnames = []
# if len(value1) == 2:
#     surnames.append(value1[1:])
#     surnames.append(value2[1:])
#     # surnames.append(value3[1:])
#     # surnames.append(value4[1:])
#     # surnames.append(value5[1:])
#     # surn = surnames[0] + surnames[1] + surnames[2] + surnames[3] + surnames [4]
#     surn = surnames[0] + surnames[1]
#     surn.sort()
#     print(surn)
# elif len(value1) > 2:
#     surnames.append(value1[1:])
#     surn1 = surnames[0]
#     surname1 = ' '.join(str(e) for e in surn1)
#     surssur = [surname1]
#     print(surssur)

# value1 = input().split()
# value2 = input().split()
# value3 = input().split()
# value4 = input().split()
# value5 = input().split()
# surnames = []
# surnames.append(value1[-1])
# surnames.append(value2[-1])
# surnames.append(value3[-1])
# surnames.append(value4[-1])
# surnames.append(value5[-1])
# # surn = surnames[0] + surnames[1] + surnames[2] + surnames[3] + surnames [4]
# print(surnames)

# list_ = [1, 2, 3, 4]
# for val in list_:
#     val = input().split()
#     val += 1
# print(val)



""" Task 20 lists """
# total = 0
# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# for element in list_:
#     if type(element) == type(int):
#         total = total + list_[element]
#     elif type(element) == type(str):
#         str_to_int = int(element)
#         if type(str_to_int) == type(str):
#             pass
#         elif type(str_to_int) == type(int):
#             total = total + list_[str_to_int]
# print(total)


# a = {'a': 1, 'b': 2, 'c': 3}
# print(a.get('b'))


# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# result = {}
# for k, v in list(a.items()):   
#     if k and v != None:
#             result.update({k:v})
# print(result)


""" Task 11 dict """
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
# for k, v in list(a.items()):
#     a.update({k:(v/5)})
# print(a)


# a = {'apple': 2, 'orange': 5, 'banana': 10}
# result = {}
# for k, v in list(a.items()):   
#     if v % 2 != 0:
#             result.update({k:v})
# print(result)


# a = {'a': 3, 'b': 2}
# print((a['a']) + (a['b'])) 

# a = {'a': 3, 'b': 2}
# print(sum(a.values()))



# dict_ = {'a': 32, 'b': 56, 'c': 37, 'd': 21}
# final_dict = []
# for k, v in list(dict_.items()):
#     final_dict.append(v)
# print(max(final_dict))



# dict1 = {'a': 3, 'b': 4, 'c': 9, 'd': 5, 'e': 6}
# dict2 = {}

# for k, v in list(dict1.items()):
#     if v % 2 == 0:
#         dict2.update({k:v})
#     else:
#         dict2.update({k:1})
# print(dict2)


""" Task 22 dict """
# dict_ = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# for k, v in list(dict_.items()):
#     if v != None:
#         del dict_[k]
# print(dict_)


# dict1 = {25: 'apple', 26: 'orange', 27: 'banana'} 
# dict2 = {}
# for k, v in list(dict1.items()):
#     dict2.update({(k**2):v})
# print(dict2)


# list_ = ['Bootcamp', 'Makers', 'coding', 'hello']
# dict_ = {}
# for k in list_:
#     dict_.update({k:(len(k))})
# print(dict_)

""" TASk 25 """
# dict_ = {'Bootcamp': 4, 'Makers': 6, 'coding': 6, 'hello': 5}
# m = max(dict_.values())
# x = next(k for k, v in dict_.items() if v == m)
# print(x)



# dict1 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
# dict2 = {}
# for k, v in list(dict1.items()):
#     dict2.update({k:(pow(v, 3))})
# print(dict2)



# a = {'a': 10, 'b': 9, 'c': 3}
# b = a['a']
# c = a['b']
# d = a['c']
# result = b * c * d
# print(result)

# dict_ = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# b = {}
# for k, v in list(dict_.items()):
#     for key, value in list(v.items()):
#         b.update({k:value})
# print(b)


# from itertools import product
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k, v in list(dict1.items()):
#     for key, value in list(v.items()):
#         dict2.update({key:value})



# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = int(input())
# for k, v in list(dict_.items()):
#     if k == key:
#         print("Key is present in the dictionary")
#     else:
#         print("Key is not present in the dictionary")




# dict1 = {1:10, 2:20}
# dict2 = {3:30, 4:40}
# dict3 = {5:50, 6:60}
# dict4 = {}
# dict4.update(dict1)
# dict4.update(dict2)
# dict4.update(dict3)
# print(dict4)



# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
# dict_ = {}
# for key, value in zip(list1, list2):
#     dict_.update({key:value})
# print(dict_)



# hashtags = '#makers#bootcamp#программирование#it#курсы'
# print(hashtags.lstrip().split('#'))


# x = 3
# y = 10
# z = 7
# print(max(x, y, z))

# hashtags = '#makers#bootcamp#программирование#it#курсы'


# string = hashtags.lstrip('#').split('#')
# print(hashtags)

""" Task 20 LIsts """

# list_ = [1, 'abcd', 3, '1', 4, 'xyz', 5, 'pqr', 7, 5, 12]
# new_list = []
# sum_of_int = 0
# for element in list_:
#     string = str(element)
#     if string.isdigit():
#         num = int(string)
#         new_list.append(num)
# for i in range(len(new_list)):
#     sum_of_int = sum_of_int + new_list[i]
# print(sum_of_int)


#     if type(element) == type(int):
#         new_list.append(element)
#     elif type(element) == type(str):
#         if element.isdigit():
#             new_list.append(element)
# print(new)

# str_list = ['abc', 'xyz', 'aba', '1221']
# indexs = []
# for element in str_list:
#     if element[0] == element[-1]:
#         indexs.append(element)
# print(indexs)


# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# max_list = max(lists, key=len)
# min_list = min(lists, key=len)
# print('max_list', max_list)
# print('min_list', min_list)

# def large(arr): 
#     max_ = arr[0]
#     for ele in arr:
#         if len(ele) > len(max_):
#            max_ = ele
#     return max_
# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# result = large(lists)
# print('max_list', result)
# def large(arr): 
#     max_ = arr[0]
#     for ele in arr:
#         if len(ele) < len(max_):
#            max_ = ele
#     return max_
# result1 = large(lists)
# print('min_list', result1)



# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# lists.sort()
# print('max_list', lists[-1])
# print('min_list', lists[0])

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# if lists == [[]]:
#     max_list = []
#     min_list = None
# elif lists[0] == lists[1]:
#     max_list = lists[0]
#     min_list = None
# else:
#     max_list = max(lists, key=len)
#     min_list = min(lists, key=len)
# print('max_list', max_list)
# print('min_list', min_list)



# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new1 = []
# new2 = []
# new3 = []
# if step > 2:
#     counter = 0
#     while counter < len(list_):
#         new1.append(list_[counter])
#         counter += step
#     counter = 1
#     while counter < len(list_):
#         new2.append(list_[counter])
#         counter += step
#     counter = 2
#     while counter < len(list_):
#         new3.append(list_[counter])
#         counter += step
#     new_lists = [new1, new2, new3]
# elif step == 2:
#     counter = 0
#     while counter < len(list_):
#         new1.append(list_[counter])
#         counter += step
#     counter = 1
#     while counter < len(list_):
#         new2.append(list_[counter])
#         counter += step
# else:
#     counter = 0
#     while counter < len(list_):
#         new1.append(list_[counter])
#         counter += step
#     new_lists = [new1]
# print(new_lists)



# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new_list = []
# counter = 0
# while counter < step:
#     new_list.append(list_[counter])
#     counter += 1
#     while counter < len(list_):
#         new_list.append(list_[counter])
#         counter += step

# print(new_list)
    

# input_ = input()
# new_list = []
# list_ = ['sun', 'flowers', 'rumor', 'stranger', 'adventure', 'architect', 'accompany', 'abandon', 'cartoon']
# for element in list_:
#     if input_ == element[0]:
#         new_list.append(element)
# print(new_list)



# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# differs1 = []
# differs2 = []
# counter = 0
# while counter < len(colors1):
#     counter += 1
#     if colors1[counter] != colors2[counter]:
#         differs1.append(colors1[counter])
#         differs2.append(colors2[counter])
#     elif colors1[counter] == colors2[counter]:
#         pass
# print(differs1, differs2)


# colors1 = ["red", "orange", "green", "blue", "white"]
# colors2 = ["black", "yellow", "green", "blue"]
# c = []
# d = []
# for i in colors1:
#         if i not in colors2:
#             c.append(i)
# for j in colors2:
#         if j not in colors1:
#             d.append(j) 
# print(c)
# print(d)


# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# for i in list1:
#     if i not in list2:
#         print(False)
#     else:
#         print(True)

        
# robert = {5, 7, 11, 10, 28}
# kail = {1, 6, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# if robert.isdisjoint(kail) and robert.isdisjoint(merri):
#     print('no one')
# elif robert.intersection(kail) != set() and robert.isdisjoint(merri):
#     print('kail')
# elif robert.intersection(merri) != set() and robert.isdisjoint(kail):
#     print('merri')
# else:
#     print('kail merri')


# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'}
# timur = {'OchakKebab', 'FreshBox'}
# aleksandr = {'FreshBox', 'KFC'}
# elina = {'Dodo', 'ImperiaPizza', 'FreshBox', 'OchakKebab', 'KFC'}
# inter = tilek & timur & aleksandr & elina
# print(inter)


# ingredients = {"cыр чеддар","грибы", "соус","шпинат"}
# ingredients.add('помидор')
# ingredients.discard('колбаса')
# ingredients.remove('шпинат')
# ingredients.add('базилик')
# ingredients.remove('cыр чеддар')
# ingredients.add('сыр моцарелла')
# print(ingredients)



# step = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new_list = []
# for i in range(step):
#     n_list = []
#     for j in range(i, len(list_), step):        
#         n_list.append(list_[j])
#     new_list.append(n_list)
# print(new_list)


# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# if inp2 == 1:
#     a[0].add(inp1)
#     a[1].add('default value')
#     a[2].add('default value')
# elif inp2 == 2:
#     a[1].add(inp1)
#     a[0].add('default value')
#     a[2].add('default value')
# elif inp2 == 3:
#     a[2].add(inp1)
#     a[1].add('default value')
#     a[0].add('default value')
# print(a)

# a = [set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# for i in range(len(a)):
#     if inp2 == i +1:
#         a[i].add((inp1))
#     else:
#         a[i].add('default value')
# print(a)



# list_ = ['hello', 23, 56, 'world', 928, 'Makers', 456, 'word', 223, 89, 'bootcamp', 'coding']
# dict_ = {}
# string = []
# numbers = []
# for i in list_:
#     if type(i) == int:
#         numbers.append(i)
#     elif type(i) == str:
#         string.append(i)
# for k, v in zip(string, numbers):
#     dict_.update({k:v})
# print(dict_)



# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dict = {}
# sorted_keys = sorted(dict_, key=dict_.get)

# for i in sorted_keys:
#     sorted_dict[i] = dict_[i]

# print(sorted_dict)




# dict_ = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# sorted_dic = {}
# sorted_keys = sorted(dict_, key=dict_.get)
# for i in sorted_keys:
#     sorted_dic[i] = dict_[i]
# items = list(sorted_dic.items())
# sorted_dict = {k: v for k, v in reversed(items)}

# dict_ = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# key = int(input())
# # for k, v in list(dict_.items()):
# #     if k == key:
# #         print("Key is present in the dictionary")
# #     elif k != key:
# #         print("Key is not present in the dictionary")
# if key in dict_:
#     print("Key is present in the dictionary")
# else:
#     print("Key is not present in the dictionary")


# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }
# dict_['math']['sum'] = sum(dict_['vars'][i] for i in dict_['vars'])
# print(dict_['math']['sum'])

# from math import prod
# a = {'a': 10, 'b': 9, 'c': 3}
# print(prod(list(a.values())))


# from functools import reduce
# a = {'a': 10, 'b': 9, 'c': 3}
# list_ = prod(list(a.values()))
# result = reduce(lambda x, y: x*y, list_)
# print(result)



# list_ = [4, 6, 4, 3, 3, 8, 4, 3, 4, 3, 8, 8]
# repeats = 3
# res = []
# for i in list_:
#     if list_.count(i) >= repeats:
#         res.append(i)
# print(res)



# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = []
# for num in list_:
#     if num > 0:
#         if num % 2 == 0:
#             int_list.append(num)
# print(int_list)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [num for num in list_ if num % 2 == 0 and num > 0 ]
# print(int_list)


# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = []
# for num in str_list:
#     int_list.append(int(num))
# print(int_list)

# int_list = [int(num) for num in str_list]
# print(int_list)

# list_ = [True if num % 2 == 0 else False for num in range(1, 11)]
# print(list_)

# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# new_list = ['shorter' if len(ele) <= 4 else 'longer' for ele in list_name]
# print(new_list)


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {}
# for k, v in list(a.items()):
#     dict_.update({k:list(range(1, v + 1))})
# print(dict_)

# dict_ = {k:list(range(1, v + 1)) for k, v in a.items()}

# dict_ = {'first': 1, 'second': 2, 'third': 3}
# # a = {}
# # for k, v in dict_.items():
# #     if v % 2 == 0:
# #         a.update({k:'even'})
# #     else:
# #         a.update({k: 'odd'})
# # print(a)

# a = {key:'even' if value % 2 == 0 else 'odd' for key, value in dict_.items()}
# print(a)


# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list1 = string_.split()
# # list_ = []
# # for ele in list1:
# #     if ele.isdigit():
# #         list_.append(ele)
# # print(list_)

# list_ = [ele for ele in list1 if ele.isdigit()]
# print(list_)


# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# res = {}
# # for key in dict_.items():
# #     for k, v in key[-1].items():
# #         if v == max(key[-1].values()):
# #             res.update({key[0]:k})
# # print(res)

# res = {key[0]: k for key in dict_.items() for k, v in key[-1].items() if v == max(key[-1].values())}
# print(res)


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 
# dict_ = {}
# for k, v in my_dict.items():
#     for key, value in v.items():
#         dict_.update({k:value})
# print(dict_)

# dict_ = {k:value for k, v in my_dict.items() for key, value in v.items()}
# print(dict_)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = []
# for num in list_:
#     if num < 0:
#         int_list.append(1)
#     else:
#         int_list.append(num)
# print(int_list)

# int_list = [1 if num < 0 else num for num in list_]
# print(int_list)

# list1 = [1, 2, 'hello', 3, 'world', 4, 5, 'book', 'code', 6, 'Makers', 7, 8, 9, 10]
# list2 = []
# for ele in list1:
#     if type(ele) == str:
#         list2.append(ele)
# print(list2)

# list2 = [ele for ele in list1 if type(ele) == str]

# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# list_ = []
# for k, v in dict_.items():
#     for key, value in v.items():
#         list_.append(value)
# print(list_)


# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# list_ = []
# for k, v in dict_.items():
#     if v > 200 and v < 5000:
#         list_.append(k)
# print(list_)
# list_ = [key for key, value in dict_.items() if value > 200 and value < 5000]


# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# dict2 = {}
# for k, v in dict1.items():
#     dict2.update({k.replace('i', ''): k.count('i')})
# print(dict2)

# dict2 = {k.replace('')}

# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# list2 = [ele for ele in list1 if ele != 0 and ele != [] and ele != {} and ele != '' and ele != None]
# print(list2)

# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# readers = []

# # for patron in SPL_Patrons:
# dict_ = dict(SPL_Patrons)
# for k, v in dict_.items():
#     if v > 100:
#         readers.append(k)
# print(readers)



# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# saved_amount = []
# dict_ = dict(SPL_Patrons)
# for k, v in dict_.items():
#     saved_amount.append(round(v * 11.95, 2))
# print(saved_amount)


# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]


# result = []
# for element in prairie_pirates:
#     if element[-1] == True:
#         result.append([element[0], element[1] * 42])
# print(result)


# result = [[element[0]], element[1] * 42 for element in prairie_pirates if element[-1] == True]
# print(result)


# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }
# summa = []

# for k, v in dict_.items():
#     if v['rating'] > 3:
#         summa.append(v['likes'])
# print(sum(summa))


# dict_ = {
#     'Dasha': {
#         'likes': 15,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#         ],
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#         ],
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': [
#             {'id': 1, 'text': 'some text'},
#             {'id': 2, 'text': 'some text'},
#             {'id': 3, 'text': 'some text'},
#             {'id': 4, 'text': 'some text'},
#             {'id': 5, 'text': 'some text'},
#             {'id': 6, 'text': 'some text'},
#         ],
#         'rating': 2
#     }
# }

# comments = []
# for k, v in dict_.items():
#     if len(v['comments']) > 3:
#         for i in range(len(v['comments'])):
#             comments.append(v['comments'][i]['id'])
# print(comments)


# comments = [v['comments'][i]['id'] for k, v in dict_.items() for i in range(len(v['comments'])) if len(v['comments']) > 3]
# print(comments)



# dict_ = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four'
# }

# dict1 = {k: len(v) if k % 2 == 0 else len(v) ** 3 for k, v in dict_.items()}
# print(dict1)


# set1 = {i for i in range(0, 10)}
# set2 = {j for j in range(8, 18)}
# full_set = set1.union(set2)
# inter = set1.intersection(set2)
# if len(full_set) < 20:
#     print(f"В этом сете было {len(inter)} повторения, его длина составляет {len(full_set)}")
# else:
#     print("Ваш объединенный сет полностью уникальный!")

# set1 = {i for i in range(0, 10) if i % 2 == 0}
# set2 = {j for j in range(0, 10) if j % 2 == 1}
# if set1.isdisjoint(set2):
#     print('Множества не пересекаются!')
# else:
#     print('Множества пересекаются!')
# from math import prod
# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}
# for k, v in dict1.items():
#     for i in range(len(v)):
#         print(v[i])
#     # dict2.update({k: v[0] * v[-1]})
# #         dict2.update({k: v[0] * v[-1]})
# # print(dict2)


# string = "pythonist"
# dict_ = {}
# # for k, v in dict_.items():
# for i in string:
#     dict_.update({i:string.count(i)})
# print(dict_)



# list_ = [1, 2, 3]
# for i in list_:
#     print(i)


# num1 = int(input())
# num2 = int(input())
# try:
#     num1 = int(input())
#     num2 = int(input())
#     result = num1 + num2
#     print(result)
# except:
#     print('Введите число!')


# try:
#     cash = int(input())
#     if cash < 0:
#         raise ValueError('Сумма не может быть отрицательной!')
#     else:
#         print(cash)
# except ValueError:
#     print('no')


# list_ = [1, 2, 3]
# list_.get(1)


# for i in range(10):
#     list_.append(i)


# list_ = [1, 2, 3, 4]
# for i in range(0, len(list_) + 1):
#     print(list_[i])

# warehouse = [
#     ['1', '2', '3'],
#     [1, 2],
#     [[1], [2], [3]],
#     [[1, 2, 3], [1, 2, 3, 4, 5], {'hello': 'world'}],
# ]
# for i in warehouse:
#     if len(warehouse) > 10 or len(i) > 3:
#         raise ValueError

# k = 300
# assert k >= 0, "Холоднее абсолютного нуля!"
# to_fahrenheit = ((k - 273.15) * 9.0 / 5 + 32)
# print(to_fahrenheit)

# try:
#     num = 1000000
#     while num != 1:
#         pass
# except 
        
# def to_fahrenheit(k: int):
#     assert k >= 0, "Холоднее абсолютного нуля!"
#     result = (k - 273.15) * 9.0 / 5 + 32
#     return result
# print(to_fahrenheit(300))


# def filter_comment(comment: str, banlist=[]):
#     try:
#         if 

# def get_type(a, b):
#     type_a = type(a)
#     type_b = type(b)

# print(get_type(5, 's'))


# num = 6
# def check(num):
#     if num % 2 == 0:
#         return "It is even number"
#     elif num % 2 == 1:
#         return "It is odd number"

# check(num)


# def is_palindrome(elem):
#     if elem == elem[::-1]:
#         return True
#     else:
#         return False

# print(is_palindrome('helleh'))


# def multiply_list(list_):
#     counter = 0
#     for i in list_:
#         counter = counter * i
#     return counter

# print(multiply_list([1, 2, 3, 4, 5, 6]))

# def sum_digits(num):
#     suma = 0
#     while num > 0:
#         digit = num % 10
#         suma = suma + digit
#         num = num // 10
#     return suma

# print(sum_digits(105))

# def sum_of_digits(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum

# print(sum_of_digits(1557)) # 18


# def func11(x, y, z):
#     try:
#         result = (x + y) / z
#         return result
#     except ZeroDivisionError:
#         result = x + y
#         return result
    

# def func12(list_, case):
#     new_list = []
#     if case == 'lower':
#         for ele in list_:
#             new_list.append(ele.lower())
#     else:
#         for ele in list_:
#             new_list.append(ele.upper())
#     return new_list

# def func13(string):
#     dict_ = {}
#     for i in string:
#         dict_.update({i:string.count(i)})
#     return dict_
    

# def func16(km, fuel):
#     result = (fuel * 100) / km
#     return f'На 100км было расходовано {round(result)}л горючего'

# print(func16(300, 30))


# colors = ["Red", "Green", "Blue", "White", "Black", "Yellow", "Orange"]
# new_colors = []
# for i in colors:
#     new_colors.append(i[::-1])
# new_colors.sort(key=len)
# print(new_colors)

""" Создать функцию func18, которая в качестве аргумента будет принимать список со строками и числами, задача, отсортировать числа в отдельный список, а строки в отдельный и распечатать оба списка """


# def func18(list_):
#     string = []
#     integer = []
#     for i in list_:
#         if type(i) == int:
#             integer.append(i)
#         else:
#             string.append(i)
#     return integer, string
        



# list_ = [1,2,3,4,5,6,7,8,9,0]
# step = 2
# element = 'A'
# counter = step
# for i in range(len(list_) // step):
#     list_.insert(counter, element)
#     counter += step + 1
# print(list_)


# lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
# new_lists = []
# for i in lists:
#     new_lists.append([sum(i)])
# print(lists[new_lists.index(max(new_lists))])

# list_ = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# repeated = []
# for num in list_:
#     if list_.count(num) > 1 and num not in repeated:
#         repeated.append(num)
# print(repeated)


# chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# merge_from = 'a'
# merge_to = 'd'
# list_ = []
# chars[chars.index(merge_from):chars.index(merge_to) + 1] = [''.join(chars[chars.index(merge_from):chars.index(merge_to) + 1])]
# print(chars)

# K = 3

# list_ = []

# for i in range(K):
#     list_.append([0] * K)

# print(list_)



# from itertools import permutations
# list_ = [1, 2, 3] 
# comb = permutations(list_, 3)
  
# for i in comb:
#     print(i)


# list_ = [1, 2, 3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if j != i and i != k and j != k:
#                 print(list_[i], list_[j], list_[k])


# list1 = [1,2,3,4,5]
# list2 = [5,6,7,8,9]
# set1 = set(list1)
# set2 = set(list2)
# if set1.intersection(set2) != set():
#     print(True)
# else:
#     print(False)


# dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
# dict2 = {}

# for k, v in dict1.items():
#     result = 1
#     for key, value in v.items():
#         result = result * value
#         dict2.update({k:result})

# print(dict2)

""" Дан словарь. Найдите сумму значений словаря, который хранится под ключом vars, используя значение словаря, под ключом math """
# dict_ = {
#     'math': {
#         'sum': sum
#     },
#     'vars': {
#         'a': 5,
#         'b': 20,
#         'c': 50
#     }
# }
# summa = []
# # for k, v in dict_.items():
# #     for key, value in v.items():
# #         summa.append(value)
# # print(summa)
# print(dict_['math']['sum'](dict_['vars'].values()))


# for i in range(1, 10):
#     i -= 5
# print(i)


# a = list('py')
# print(len(a))


# a = [1, 3]
# print(int(a))

# d = {1:2, 2:4, 3:9}
# print(d[1])

# d = dict([(2, 1)])
# print(d)


# set1 = set(num for num in range(0, 10) if num % 2 == 0)
# set2 = set(i for i in range(0, 10) if i % 2 == 1)
# if set1.intersection(set2) != set():
#     print('Множества пересекаются!')
# else:
#     print('Множества не пересекаются!')


# def collect_all_possibles(list_: list, num: int):
#     new_list = []
#     for i in list_:
#         if type(i) == str:
#             new_list.append(i * num)
#         elif type(i) == list:
#             new_list.append(i*num)
#         elif type(i) == int:
#             new_list.append(i + num)
#             new_list.append(i - num)
#             new_list.append(i * num)
#             new_list.append(i ** num)
#             new_list.append(i // num)
#     return new_list

# list_ = [
#     'hello',
#     6, 
#     [1,2,3]
# ]

# num = 2

# print(collect_all_possibles(list_, num))


""" Напишите программу, которая запрашивает ввод двух значений inp1, inp2.

Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е. соединение, строк.

В остальных случаях введенные числа суммируются. """

# inp1 = input()
# inp2 = input()

# try:
#     sum = int(inp1) + int(inp2)
# except ValueError:
#     sum = inp1 + inp2

# print(sum)

# def collect_all_possibles(list_: list, num: int):
#     new_list = []
#     for i in list_:
#         try:
#             new_list.append(i + num)
#             new_list.append(i - num)
#             new_list.append(i * num)
#             new_list.append(i ** num)
#             new_list.append(i // num)
#         except TypeError:
#             if i == None or type(i) == bool or i == '':
#                 pass
#             else:
#                 new_list.append(i * num)
#     return new_list
# list_ = [None, False, '']

# num = 5

# print(collect_all_possibles(list_, num))



""" Запросите у пользователя несколько слов и чисел, поместите их в переменную inp1 введенных через пробел, затем:

поместите эти слова в список
переберите этот список циклом и перевидете все строки в тип данных - число
все числа поместите в отдельный list_
а на возникающие исключение сгенерируйте свое исключение cо строкой:

 Данный элемент не является числом!  """

# inp1 = 'hello 5 world 6 bootcamp 7'
# list1 = inp1.split(' ')
# list_ = []
# try:
#     for i in list1:
#         num = int(i)
#         list_.append(num)
# except:
#     print('Данный элемент не является числом!')

# print(list_)

# a = input().split()
# list_ = []
# for i in a:
#     try:
#         list_.append(int(i))
#     except:
#         print("Данный элемент не является числом")

# print(list_)


# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# def func19(list_: list):
#     for i in list_:
#         for k, v in i.items():
#             print(v)


# for i in students:
#     students.sort()



# users = [
#   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#   { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
# ]
# for user in users:
#     if user['work'].startswith('IT'):
#             print(user['name'], ', скидки в магазине компьютерной техники!')

# def func15(users):
#     for user in users:
#         if user['work'].startswith('IT'):
#             print(user['name'], ', скидки в магазине компьютерной техники!')

# print(func15(users))
# def add_(a, b):
#     return a + b
# def sub_(a, b):
#     return a - b
# def div_(a, b):
#     return a / b
# def mult_(a, b):
#         return a * b

# def calc(a, b, c):
#     if c == '+':
#         res = add_(a, b)
#     elif c == '-':
#         res = sub_(a,b)
#     elif c == '/':
#         res = div_(a, b)
#     elif c == '*':
#         res = mult_(a, b)
#     return res

# print(calc(4, 5, '+'))

# def foo():
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
#     def bar():
#         global var
#         var = 'переменная bar'
        
 
#     bar()
# foo()
# print('переменная в foo: ', var)

# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     x = 'Я могу изменяться'
# print(x)
# my_func()
# print(x)

# print(globals())

# num = 3
# def mul():
#     global num
#     res = num ** 2
#     num = res

# mul()
# mul()
# mul()
# print(num)

# balance = 0
# def get_salary(amount):
#     global balance
#     balance = balance + amount

# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print(f"Вы заплатили {amount} сом за {log_name}")

# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()


# result = 0
# def pow_first(x, y):
#     global result
#     result = x ** y
#     return result
# def pow_second(z):
#     global result
#     result = result % z
#     return result

# pow_first(2, 3)
# pow_second(3)
# print(result)


# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# def age_control(a: dict):
#     for k, v in a.items():
#         if v >= 17:
#             print(f'{k}, Вы можете войти в клуб')
#         else:
#             print(f'{k}, извините, Вы не проходите по age-control')
# age_control(a)


# a = ['pipi', 'papa', 'mama']
# b = []
# def title_(a: list):
#     global b
#     for i in a:
#         b.append(i.title())
# title_(a)
# print(b)

# def count_symbols(string):
#     glasnye = 0
#     soglasnye = 0
#     symbols = 0
#     for i in string:
#         if i in ' -,.!':
#                 symbols += 1
#         elif i.isalpha():
#             letter = i.lower()
#             if letter in 'аыоэуеяиюё':
#                 glasnye += 1
#             else:
#                 soglasnye += 1
#     return f'Количество гласных: {glasnye}, согласных: {soglasnye}, остальных символов: {symbols}'

# print(count_symbols('Мурат супер!'))

# a = []
# def from0to10():
#     global a
#     for i in range(11):
#         a.append(i)

# from0to10()
# print(a)


# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# def lower_7():
#     b = []
#     global a
#     for i in a:
#         if i < 7:
#             b.append(i)
#     return b
            
# print(lower_7())


# a = input().split(',')
# print(a[0], a[-1])
# a.pop()
# a.append('Makers')
# print(a)



# import random
# numbers = random.sample(range(0, 100), k=10)
# print(sorted(numbers))


# a = input().split(' ')
# words = []
# lens = []
# for i in a:
#     words.append(i)
#     lens.append(len(i))

# print(words)
# print(lens)



# university = {
#     'программирование': 150,
#     'экономика': 98,
#     'медицина': 82
# }

# university['экономика'] = 102
# university.update({'лингвистика': 56})
# university.pop('медицина')
# summa = sum(university.values())
# print(summa)


# list_ = {1: 'a', 2: 'b', 3: 'c'}
# new = {}
# for k, v in list_.items():
#     new.update({v:k})
# print(new)

# guest_number = int(input('Vvedite kol-vo gostey: '))
# dict_ = {}

# for i in range(1, guest_number + 1):
#     guests = input('vvedite imya goastya: ')
#     dict_.update({guests:i})

# print(dict_)

# okroshka = {'картошка', 'огурцы', 'яйца', 'зелень', 'колбаса'}
# olivye = {'картошка', 'соленые огурцы', 'колбаса', 'морковь', 'яйца'}
# inter = okroshka.intersection(olivye)
# print(inter)
# print(len(inter))
# print(okroshka.difference(olivye))
# print(olivye.difference(okroshka))


# users = {
#     ('Alice', 'Python', 5),
#     ('Alice', 'JavaScript', 6),
#     ('Erzhan', 'Python', 4),
#     ('Nurlan', 'JavaScript', 8),
#     ('Meirjan', 'Python', 6)
# }
# JavaScript = set()
# Python = set()
# for i in users:
#     if 'JavaScript' in i:
#         JavaScript.add(i[0])
#     elif 'Python' in i:
#         Python.add(i[0])

# print(len(JavaScript))
# print(len(Python))
# print(JavaScript.intersection(Python))


# while True:
#     dollar = 84.8
#     valuta = input('Введите валюту(сом или доллар): ')
#     if valuta == 'доллар':
#         summa = int(input('Введите сумму, которую вы хотите перевести в доллары: '))
#         print(round(summa / dollar, 1), '$')
#     elif valuta == 'сом':
#         summa = int(input('Введите сумму, которую вы хотите перевести в сомы: '))
#         print(summa * dollar)
#     end = input('Хотите продолжить?: ')



# list_ = ['ALiya', 'Erzhan', 'Nazik', 'NUrlan', 'Meirzhan', 'Ulan']
# vowels = []
# for i in list_:
#     ele = i.lower()
#     if ele[0] in 'aeuio':
#         vowels.append(i)
# print(sorted(vowels))

# vowels = [i for i in list_ if i.lower()[0] in 'aeiou']
# print(sorted(vowels))

# a = {
#     'Sam': {'math': 95, 'literature': 88},
#     'Alice': {'math': 70, 'literature': 98}
# }
# b = {}
# for key, value in a.items():
#     for k, v in value.items():
#         b.setdefault(key, {k: v + 2})
#         b.update({key: {k: v + 2}})
# print(b)




# b = {key: {k: v + 2 for k, v in value.items()} for key, value in a.items()}
# print(b)


# a = [num for num in range(1, 11)]
# b = set(num ** 2 if num % 2 == 0 else num * 3 for num in a)
# print(b)


# try:
#     a = input()
#     b = input()
#     res = int(a) + int(b)
# except ValueError:
#     res = a + b
# print(res)


# dict_ = {
#     'ID1': 'enkasmaliev',
#     'ID2': 'sagynbaevan',
#     'ID3': 'qwertyybu'
# }
# dict_ = {v: k for k, v in dict_.items()}
# try:
#     username = input()
#     ID = dict_[username]
# #     print(ID)
# except KeyError:
#     print('Введенного юзера нет в базе данных')
# else:
#     print(f'Welcome {username}')
# finally:
#     print('Thanks')



# age = int(input())
# if age <= 0:
#     raise Exception('Your age should be bigger than 0')


# def get_info():
#     name = input('Enter your name: ')
#     surname = input('Enter your surname: ')
#     def generate_password():
#         from random import sample
#         random_num = sample(range(10), 7)
#         random_num = [str(i) for i in random_num]
#         result = name + surname + ''.join(random_num)
#         return result
#     return generate_password()

# print(get_info())


# def sum_(a, b):
#     return a + b

# def sub_(a, b):
#     return a - b

# def div_(a, b):
#     return a / b

# def mul_(a, b):
#     return a * b 

# def result(anything):
#     return anything


# def get_data(a, b, option):
    
#     dict_ = {
#         '+': sum_(a, b),
#         '-': sub_(a, b),
#         '/': div_(a, b),
#         '*': mul_(a, b)
#     }

#     something = dict_[option]
#     return result(something)

# print(get_data(34, 45, '-'))




# def make_bold(func):
#     def wrapper():
#         text = func()
#         return "\x1B[1m" + text + "\x1B[0m"
#     return wrapper

# def make_italic(func):
#     def wrapper():
#         text = func()
#         return "\x1B[3m" + text + "\x1B[0m"
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         text = func()
#         return "\u0332".join(text)
#     return wrapper

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'

# print(hello())


# def make_bold(func):
#     def wrapper():
#         text = func()
#         return "<b>" + text + "</b>"
#     return wrapper

# def make_italic(func):
#     def wrapper():
#         text = func()
#         return "<i>" + text + "</i>"
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         text = func()
#         return "<u>" + text + "</u>"
#     return wrapper

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'

# print(hello())



# def benchmark(func):
#     def wrapper():
#          import time
#          start = time.time()
#          result = func()
#          end = time.time()
#          work_time = end - start
#          print(f'Время выполнения: {work_time} секунд.')
#     return wrapper

# @benchmark 
# def fetch_webpage():
#     import requests 
#     webpage = requests.get('https://google.com')

# fetch_webpage()

# users = {
#     'cristiano': 12345678,
#     'leomessi': 13572468,
#     'mbappe10': 87654321
# }

# def validate_password(func):
#     def wrapper(username, password):
#         global users
#         try:
#             func(username, password)
#             if username not in users.keys() or password not in users.values():
#                 raise Exception
#         except Exception:
#             if username not in users.keys(): 
#                 print('Username is not defined')
#             elif password not in users.values():
#                 print('Password is invalid')
#     return wrapper

# @validate_password
# def login(username, password):
#     global users
#     if username in users.keys() and password in users.values():
#         print(f'Welcome, {username}')

# login('fjfjjf', 12345678)


# def is_admin(func):
#     def wrapper(dict_):
#         if dict_['is_admin'] == True:
#             print(f"Доступ разрешен {func(dict_)['username']}")
#         else:
#             print(f"Доступ запрещен {func(dict_)['username']}")
#     return wrapper

# @is_admin
# def get_user(dict_):
#     return dict_
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})


# users = [
#     { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
#     { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
#     { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
#     { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
#     { 'name': 'Helga', 'age': 35, 'work': 'IT-HR' }
#     ]
# def func15(users):
    

#     for i in users:
#         if i['work'].startswith('IT'):
#             print(f"{i['name']}, скидки в магазине компьютерной техники!")

# func15(users)


# def func16():
#     km = int(input())
#     fuel = int(input())
#     consumption = km / fuel
#     print(f"'На 100км было расходовано {consumption}л горючего'")

# func16()

# def func16(km, fuel):
#     consumption = fuel * 100 / km
#     print(f"'На 100км было расходовано {round(consumption)}л горючего'")

# func16(300, 30)

# def func17(list_):
#     for i in list_:
#         i['salary'] = i['salary'] + (i['overTime'] * 200)
#         i.pop('overTime')
#     return list_
# employees = [
#   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
#   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
#   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
#   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
#   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# ]


# print(func17(employees))

# def func20(list_, string):
#     new_list = []
#     for i in list_:
#         if string.lower() or string.upper() in i['title']:
#             new_list.append(i)
#     return new_list

# products = [
#     {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#     {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#     {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#      {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]
# print(func20(products, 'I'))

# def func21(list_, string):
#     new_list = []
#     for i in list_:
#         if string in i['category']:
#             new_list.append(i)
#     return new_list


# balance = 0

# def spent(target, spend, current_balance):
#     dict_ = {}
#     try:
#         if current_balance > spend:
#             current_balance = current_balance - spend
#             dict_.update({'target': target})
#             dict_.update({'spend': spend})
#             return dict_, current_balance
#         else:
#             raise Exception()
#     except Exception:
#         return 'Недостаточно средств'


# def deposit(money,  cur_balance):
#     cur_balance = cur_balance + money
#     return cur_balance
# print(spent('Product', 400, 500))


# def filter_comment(comment:str, banlist = []):

#     for i in comment:
#         if i in ",.!?":
#             raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")
#     for i in comment.split(" "):
#         if i in banlist:
#             raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")


# filter_comment('Welcome to the Internet', ['internet'])

# def filter_comment(comment:str, banlist = []):

#     for i in comment.split(" "):
#         if i.lower().rstrip(',.!?') in banlist:
#             raise ValueError("Ваш комментарий отправлен на перепроверку, так как, возможно, содержит неблагоприятный контекст")


# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]

# # def func19(list_):
    
# #     return list_['marks']

# # students.sort(key=func19)

# # print(students)

# def get_marks(list_):
#     return list_['marks']

# def func19(list_: list):
#     list_.sort(key=get_marks, reverse=True)
#     return list_

# print(func19(students))


# inp1 = input('Введите значения через пробел ')
# list_1 = inp1.split()
# list_ = [int(i) for i in list_1 if i.isdigit()]
# print(list_)

# try:
#     inp1 = input('Введите значения через пробел ')
#     list_1 = inp1.split()
#     list_ = [int(i) for i in list_1]
#     print(list_)
# except ValueError:
#     raise ValueError('Данный элемент не является числом!')

# inp1 = 'hello 5 world 6 bootcamp 7'
# list1 = inp1.split(' ')
# list_ = []
# try:
#     for i in list1:
#         num = int(i)
#         list_.append(num)
# except:
#     print('Данный элемент не является числом!')

# print(list_)

# a = input().split()
# list_ = []
# for i in a:
#     try:
#         list_.append(int(i))
#     except:
#         print("Данный элемент не является числом")

# print(list_)

# with open('ex5.txt', 'r') as file25:
#     max_ele = 0
#     for i in file25.readlines():
#         num = int(i.replace('\n', ''))
#         if num > max_ele:
#             max_ele = num
#     file25.seek(0)
#     min_ele = max_ele
#     for i in file25.readlines():
#         num = int(i.replace('\n', ''))
#         if num < min_ele:
#             min_ele = num
# print(max_ele)
# print(min_ele)

# with open('task6.txt', 'w') as file26:
#     file26.write(f'{min_ele}-{max_ele}')

list_ = list(range(-1, 26, 3))
print(list_)
