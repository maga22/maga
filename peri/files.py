import pickle,shelve
# print('Открываю и закрываю файл')
# text_file = open("read_it.txt", "r")
# text_file.close()
# print('\nЧитаю файл посимвольно')
# text_file = open('read_it.txt','r')
# print(text_file.read(1))
# print(text_file.read(5))
# text_file.close()
# print('\nЧитаю файл целиком')
# text_file = open("read_it.txt", "r")
# whole_thing = text_file.read()
# print(whole_thing)
# text_file.close()
# print('\nЧитаю одну строку посимвольно')
# text_file = open("read_it.txt", "r")
# print(text_file.readline(1))
# print(text_file.readline(5))
# text_file.close()
# text_file = open("read_it.txt", "r")
# print('\nЧитаю всю строку целиком')
# print(text_file.readline())
# print(text_file.readline())
# print(text_file.readline())
# text_file.close()
# print('\nЧитаю весь файл в список')
# text_file = open("read_it.txt", "r")
# lines = text_file.readlines()
# print(lines)
# print(len(lines))
# for line in lines:
#     print(line)
# text_file.close()
# print('\nПеребираю файл построчно')
# text_file = open("read_it.txt", "r")
# for line in text_file:
#     print(line)
# text_file.close()

#print('Создаю текстовый файл методом write()')
# text_file = open('write_it.txt','w')
# a = input('Введите текст для записи:')
# text_file.write('Строка 1\n')
# text_file.write('Строка 2\n')
# text_file.write('Строка 3\n')
# text_file.write(a)
# text_file.close()
#
# print('Создаю текстовый файл методом writelines()')
# text_file = open('write_it.txt','w')
# lines = [
#     'Строка 1\n',
#     'Строка 2\n',
#     'Строка 3\n',
# ]
# text_file.writelines(lines)
# text_file.close()


print('Консервация списков')
variety = ['огурцы','помидоры','капуста']
shape = ['целые','кубиками','соломкой']
brand = ['Главпродукт','Чумак','Бондюэль']
f = open('pickles1.dat','wb')
pickle.dump(variety,f)
pickle.dump(shape,f)
pickle.dump(brand,f)
f.close()


print('\nРасконсервация  списков')
f = open('pickles1.dat','rb')
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
print(variety)
print(shape)
print(brand)
f.close()


print('\nПомещерние списков на полку')
s = shelve.open('pickles2.dat')

s['variety'] = ['огурцы','помидоры','капуста']
s['shape'] = ['целые','кубиками','соломкой']
s['brand'] = ['Главпродукт','Чумак','Бондюэль']
s.sync()


print('\nИзвлечение списков из файла полки.')

print('Торговые марки:' , s['brand'])
print('Формы:', s['shape'])
print('Виды овощей:', s['variety'])
s.close()


