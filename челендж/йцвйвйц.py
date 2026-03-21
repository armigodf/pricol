# class Cat:
#     def speak(self):
#         print('Meow')
#
#
# murzik = Cat()
# print(type(murzik))
# print(dir(murzik))


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def bring_destruction(self):
#         print(f'{self.name} что-то сломал!')
#
#
# class Dog(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#
#     def make_sueta(self):
#         print(f'{self.name} играет с диваном')
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         Animal.__init__(self, name)
#
#     def make_sueta(self):
#         print(f'{self.name} тыгыдыкает в 5 утра по лицу')
#
#
# dog = Dog('Барбос')
# cat = Cat('Елкалаз')


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         print(f'Его зовут {self.name}!')
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.get_name()
#
#
# Cat(input('Как его зовут?:'))


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         print(f'Его зовут {self.name}!')
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#         self.get_name()
#
#
# class Lion(Cat):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def play(self):
#         print(f"{self.name} играет с едой.")
#
#
# Lion1 = Lion('Лев')
# Lion1.play()

# class Animal:
#     def __init__(self, animal_type):
#         self.animal_type = animal_type
#
#     def get_type(self):
#         print(f"Это {self.animal_type}!")
#
#
# class Zoo(Animal):
#     def __init__(self, animal_type):
#         super().__init__(animal_type)
#         self.get_type()
#
#
# Zoo(input('Что за зверь: '))
#

# class Animal:
#     def __init__(self, animal_type):
#         self.animal_type = animal_type
#
#     def get_type(self):
#         print(f"Это {self.animal_type}!")
#
#
# zoo = Animal("кот")
# zoo.get_type()


# Вот тебе код для экспериментов
class Kettle:
    def turn_on(self):
        print('Чайник включился')
        self.__boil()
        self.__check_t()
        self.__beep()
        self.__turn_off()

    def __boil(self):
        print('Вода греется, пузырьки мутятся')

    def __check_t(self):
        print('Проверяется температура')

    def __beep(self):
        print('Вода нагрелась, издает звук')

    def _turn_off(self):    
        print('Чайник выключился')


chaynik = Kettle()
chaynik.turn_on()

chaynik.__boil()
chaynik._turn_off()
chaynik.__check_t()
chaynik._turn_off()
