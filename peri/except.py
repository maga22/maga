#try:
#     num = float(input('Введите число:'))
# except:
#     print('Похоже, это не число')


# try:
#     num = float(input('Введите число:'))
# except ValueError:
#     print('Это не число')

# for value in (None,'Привет'):
#     try:
#         print('Пытаюсь преобразовать в число:', value , '-->' ,end=' ')
#         print(float(value))
#     except (TypeError,ValueError):
#         print('Это не число')


try:
    num = float(input('\nВведите число:'))
except ValueError as e:
    print('Это не число, интепретатор как бы говорит нам:', e)
else:
    print(num)