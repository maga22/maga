#виртуальный питомец, о котором пользователь может заботиться


class Critter(object):
    '''Виртуальный питомец'''
    def __init__(self,name,hunger,boredom):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'прекрасно'
        elif 5<=unhappiness<=10:
            m = 'неплохо'
        elif 11<=unhappiness<=15:
            m = 'не сказать чтобы хорошо'
        else:
            m = 'ужасно'
        return m


    def talk(self):
        print('Меня зовут', self.name,'я чувствую себя', self.mood)
        self.__pass_time


    def eat(self,food=4):
        print('Мрр.Спасибо!')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time


    def play(self,fun=4):
        print('Уиии!')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time


def main():
    crit_name = input("Как вы назовете свою зверюшку?")
    crit = Critter(crit_name,16,16)

    choice = None

    while choice != 0:
        print \
        ('''
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        ''')
        choice = input('Ваш выбор:')
        print()
        #выход
        if choice == '0':
            print('До свидания')
        #беседа со зверюшкой
        elif choice == '1':
            crit.talk()
        #кормление зверюшки
        elif choice == '2':
            crit.eat()
        #игра со зверюшкой
        elif choice == '3':
            crit.play()
        #непонятный пользовательский воод
        else:
            print('Извините, в меню нет пункта ',choice)

main()
