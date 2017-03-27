#зверюшка с атрибутом
#Демонстрирует создание атрибутов объекта и доступ к ним

class Critter(object):
    '''Виртуальная зверюшка'''
    def __init__(self,name):
        print('Появилась на свет новая зверюшка')
        self.name = name
    def __str__(self):
        rep = 'Объект класса Critter \n'
        rep += 'имя:'+ self.name + '\n'
        return rep
    def talk(self):
        print('Привет, я зверюшка - экземпляр класса Critter, мое имя:'+self.name)
namef = input('Введите имя:')
crit1 = Critter(namef)
crit1.talk()
#print(crit1) #вывод объекта crit1 на экран
#print(crit1.name) #непосредственный жоступ к атрибуту crit1.name

crit2 = Critter('Мурзик')
crit2.talk()
