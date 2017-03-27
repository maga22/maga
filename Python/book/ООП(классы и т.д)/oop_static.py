#демонстрирует атрибуты класса и статические методы


class  Critter(object):
    '''Виртуальный питомец'''
    total = 0
    @staticmethod
    def status():
        print('Всего зверюшек сейчас:', Critter.total)
    def __init__(self,name):
        print('Появилась на свет новая зверюшка')
        self.name = name
        Critter.total += 1

#основная часть
print('Нахожу значение атрибуту класса Critter.total:', Critter.total)
print('Создаю зверюшек')
crit1 = Critter('первая')
crit2 = Critter('вторая')
crit3 = Critter('третья')
Critter.status()
print('\nОбращаюсь к атрибуту класса через объект:',crit1.total)
