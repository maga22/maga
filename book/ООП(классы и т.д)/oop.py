#просто зверюшка
#демонстрирует простейшие класс и объект

class Critter(object) :
    '''Виртуальный питомец'''
    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")

#основная часть
crit = Critter()
crit.talk()
