# class Airplane:
#     engines = int(input("сколько нужно двигателей? "))
#     seats = int(input("Сколько нужно сидячих мест? "))
#
#
# plane = Airplane()
# print(plane.engines)
# print(plane.seats)

# class Car:
#     def __init__(self, color, brand, speed):
#         self.color = color
#         self.brand = brand
#         self.speed = speed
#         print("автомобиль готов")
#
#
# car1 = Car(color="красный", brand="Niva", speed="142 км/ч")

class Ship:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def go_swimming(self):
        print(f"{self.name} отправился в плаванье.")

    def how_many_people(self):
        print(f"На борту корабля '{self.name}' находится {self.people} человек")

    def stop_ship(self, time):
        print(f"Корабль {self.name} кинул якорь на {time} часов.")


ship1 = Ship(name="Варяг", people=124)

ship1.how_many_people()
ship1.go_swimming()
ship1.stop_ship(time=12)
