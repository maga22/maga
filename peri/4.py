import random
#a = random.randint(1,10)
# b = random.randint(1,10)
# print(str(a) + '*' + str(b))
# c = int(input('Введите ответ:'))
# if c ==  a * b:
# 	print('Верно')
# else:
# 	print('Неверно')

#1
# running = True
# a = int(input('Максимум до какого числа выводить примеры?(выберите 10,50 или 100):'))
# def example():
# 	global running
# 	if a == 10:
# 		b = random.randint(1,10)
# 		c = random.randint(1,10)
# 		print(str (b) + '*' + str(c))
# 		C = int(input('Введите ответ:'))
# 		if C ==  b * c:
# 			print('Верно')
# 		else:
# 			print('Неверно')
# 		running = False
# 	if a == 50:
# 		B = random.randint(1, 50)
# 		C = random.randint(1, 50)
# 		print(str(B) + '*' + str(C))
# 		J = int(input('Введите ответ:'))
# 		if J == B * C:
# 			print('Верно')
# 		else:
# 			print('Неверно')
# 		running = False
# 	if a == 100:
# 		F = random.randint(1,100)
# 		E = random.randint(1,100)
# 		print(str(F) + '*' + str(E))
# 		M = int(input('Введите ответ:'))
# 		if M == E * F:
# 			print('Верно')
# 		else:
# 			print('Неверно')
# 		running = False
# example()
# while running:
# 	if a != 10 and 50 and 100:
# 		print("Введите одно из чисел:10,50,100")
# 	F = int(input('Максиму до какого числа выводить примеры?(выберите 10,50 или 100):'))
# 	example()
#
#
#
# #2
# A = int(input('Введите число:'))
# B = random.randint(1,10)
# print(A , '*' , B)
# C = int(input('Введите ответ:'))
# if A * B == C:
# 	print('Верно')
# else:
# 	print('Неверно')


# a = 'Амин красавчик'
# print(a[5:])
# print(a[-3:])
# print(a[-1:-4:-1])
# print(len(a))
# poem = """  Закали свои порывы,
#   Преврати порывы в сталь,
#   И лети мечтой игривой,
#   Ты в заоблачную даль!"""
# print(poem)
# print(poem.find('порывы'))
# print(poem.rfind('порывы'))
# print(poem.count('порывы'))
#
# #print(poem.upper())
# #print(poem.lower())
# #print(poem.title())
# print(poem.replace("порывы","эликсиры"))


# krasavci = ['Кадыр','Амин','Аслан']
# print(krasavci[1:])
# krasavci.append('Мага')
# print(krasavci)
# krasavci.insert(1,'Мага')
# print(krasavci)
# dop = ['Арслан','Амин']
# krasavci.extend(dop)
# print(krasavci)
# krasavci[2]=3
# print(krasavci)
# del krasavci[0]
# print(krasavci)
# krasavci.remove(3)
# print(krasavci)
# print(krasavci.pop(1))
# print(krasavci)
#
#
# str1 = '+'.join(krasavci)
# print(str1)
# print(str1.split(' '))
#
# krasavci2 = 'Камал','Гуд'
# krasavci2 = list(krasavci2)
# print(krasavci2)
# krasavci2[1] = '<3'
# print(krasavci2)
#
# krasavci3 = {1, 2, 3, 1, 5}
# krasavci4 = {1,9,3,4}
#
# # print(krasavci3)
# # print( 1 in krasavci3)
# # krasavci3.add(8)
# # print(krasavci3)
#
# print(krasavci3 & krasavci4) #пересечение
# print(krasavci3 | krasavci4) #объединение
# print(krasavci3 - krasavci4) #разность

#Простой список


a = ['Руслан','Марьям','Амин']
print(a)
a.append('Андрей')
print(a)


#Кортеж


cortej = (1,2,"Мага")
print(cortej)


#Словарь

en_ru_dict = {
    'apple':'яблоко',
    'school':'школа',
    'house':'дом'
}
print(en_ru_dict['school'])

en_ru_dict['house']='жилище'
print(en_ru_dict)
en_ru_dict['phone']='телефон'
print(en_ru_dict['phone'])


#Циклы
# a = 1
# name = 'Амин'
# while name != 'Артур':
#     print(name)
#     a += 1
#     if a == 4:
#         name = 'Артур'

# while True:
#     name = input('Угадайте имя:')
#     if name == 'Зубер':
#        a = input('Вы угадали, выйти из программы?')
#
#         if a == 'y':
#             break
#         elif a == 'n':
#             а

names = ['Кадыр','Амин',"Аслан"]
for name in names:
    print(name)

user = {'Имя':"Мага","Фамилия":"Дандамаев"}
print(user['Имя'])













