# Закрытая зверюшка
# Демонстрирует закрытые переменные и методы

class Critter(object):
    '''Виртуальный питомец'''
    def __init__(self,name,mood):
        print('появилась на свет новая зверюшка!')
        self.name = name #открытый атрибут
        self.__mood = mood
    def talk(self):
        print('Меня зовут', self.name)
        print('Сейчас я чувствую себя', self.__mood,'\n')
    def __private_method(self):
        print('Это закрытый метод.')
    def public_method(self):
        print('Это открытый метод')
        self.__private_method()

crit = Critter(name ="Бобик", mood ="прекрасно")
crit.talk()
crit.public_method()
