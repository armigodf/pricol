class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def greeting(self):
        print(f"Привет, меня зовут {self.name}. Я в {self.grade} классе.")


class School:
    def __init__(self, name):
        self.name = name

    def school_greeting(self):
        print(f"Добро пожаловать в {self.name}!")
        student1 = Student(name="Иван", age=12, grade=6)
        student1.greeting()


school = School(name="Школу №15")
school.school_greeting()
