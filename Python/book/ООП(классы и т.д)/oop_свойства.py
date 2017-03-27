class Critter(object):
    '''Виртуальный питомец'''
    def __init__(self,name):
        print('Появилась на свет новая зверюшка')
        self.__name = name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,new_name):
        if new_name == '':
            print('Имя не может быть пустой строкой')
        else:
            self.__name = new_name
            print('Имя успешно изменено')

    def talk(self):
        print('Привет, моя имя', self.name)


crit = Critter('Бобик')
crit.talk()

crit.name = 'Мурзик'
print('Теперь имя зверюшки ',crit.name)

crit.name = ''
