import math
import random
# age = 16
# name = 'Maga'
# print('Возраст {0} : {1} лет'.format(name,age))

#Цикл while:

# number = 23
# running = True
# while running:
# 	guess = int(input("Введите число:"))
# 	if guess == number:
# 		print('Вы угадали')
# 		running = False #конец цикла
# 	elif guess < number:
# 		print('Загадонное число больше, попробуйте снова')
# 	else:
# 		print('Загадонное число меньше, попробуйте снова')
# else:
# 	print('Цикл закончен')

#Цикл for:
# for a in range(1,10):
# 	print(a)
# else:
# 	print("Цикл закончен")

#Оператор break:
# while True:
# 	s = input("Введите предложение:")
# 	if s=='выход':
# 		break
# 	print("Длина строки", len(s))
# print('Конец цикла')

#Оператор continue:
# while True:
# 	a = input("Введите предложение:")
# 	if a == 'выход':
# 		break
# 	if len(a) < 3:
# 		print('Строка слишком короткая')
# 		continue
# 	print("Строка достаточной длины")

#Функции
# def sayHello():
# 	print('Hello,world')
# sayHello()

#Параметры функций
# def printMax(a, b):
# 	if a > b:
# 		print(a, 'максимально')
# 	elif a == b:
# 		print(a, 'равно', b)
# 	else:
# 		print(b, 'максимально')
# printMax(3, 4) # прямая передача значений
# x = 5
# y = 7
# printMax(x, y) # передача переменных в качестве аргументов

#Значения аргументов по умолчанию
# def say(message, times = 1):
#     print(message * times)
# say('Бла ')

# #Ключевые аргументы
# def func(a, b=5, c=10):
#     print('a равно', a, ', b равно', b, ', а c равно', c)
# func(3, 7)
# func(25, c=24)
# func(c=50, a=100)



#Оператор return

# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'Числа равны.'
#     else:
#         return y
# print(maximum(4, 3))


#Строки документации
#def printMax(x,y):
#     '''Выведет максимальное из двух чисел
# Тест документации'''
#
#     if x > y:
#         print(x,'наибольшее')
#     else:
#         print(y,'наибольшее')
# printMax(3,5)
# print(printMax.__doc__)




#Модуль sys
# import sys
# print('Аргументы командной строки:')
# for i in sys.argv:
#     print(i)
# print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')

####Задачи для практики
#def arithmetic(x,y,z='+'):
#     z = input('Приюавить(+), отнять(-),умножить(*),разделить(/)?:')
#     if z == '+':
#         print(y + x)
#     elif z == '-':
#         print(y - x)
#     elif z == '*':
#         print(y * x)
#     elif z == '/':
#         print(y / x)
#     else:
#         print('Неизвестная операция')
# arithmetic(2,3)

# year = int(input('Введите год:'))
# if year % 400 == 0:
#     print(True)
# else:
#     print(False)



# a = int(input('Введите сторону квадрата:'))
# x = a*a
# y = 4 * a
# z = a * math.sqrt(2)
# print(x,y,z)

#a=int(input('Введите номер номер месяца:'))
# if a == 12:
#     print('Зима')
# elif a == 1:
#     print('Зима')
# elif a == 2:
#     print('Зима')
# elif a == 3:
#     print('Весна')
# elif a == 4:
#     print('Весна')
# elif a == 5:
#     print('Весна')
# elif a == 6:
#     print('Лето')
# elif a == 7:
#     print('Лето')
# elif a == 8:
#     print('Лето')
# elif a == 9:
#     print('Осень')
# elif a == 10:
#     print('Осень')
# elif a == 11:
#     print('Осень')
# else:
#     print('От 1 до 12')

# a = int(input('Сколько денег вы хотите вложить?:'))
# years = int(input('На какой срок?(в годах):'))
# def bank(a,years):
#     c = years * 10
#     b = (a / 100)* c
#     print(a + b)
# bank(a,years)


