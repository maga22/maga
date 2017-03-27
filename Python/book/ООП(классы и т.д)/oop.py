#демонстрирует простейшие класс и объект

class Critter(object):
    '''Виртуальный питомец'''
    def talk(self):
        print('Привет , я зверюшка - экземпляр класса Critter')

crit = Critter()
crit.talk()
