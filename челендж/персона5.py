class Person():
    classes = {
        'Воин': {
            'здоровье': 100,
            'атака': 30,
            'защита': 25,
            'навыки': {
                'щит': 10
            }
        },
        'Лучник': {
            'здоровье': 50,
            'атака': 40,
            'защита': 20,
            'навыки': {
                'убежать': 10
            }
        },
        'Маг': {
            'здоровье': 30,
            'атака': 50,
            'защита': 15,
            'навыки': {
                'магический щит': 10,
                'лечение': 5
            }
        }
    }

    def __init__(self, name, person_classes, is_enemy, is_alive):
        self.name = name
        self.person_classes = self.classes[person_classes]
        self.is_enemy = is_enemy
        self.is_alive = True
        self.health = self.person_classes["здоровье"]
        self.atk = self.person_classes["атака"]
        self.defend = self.person_classes["защита"]
        self.skills = self.person_classes["навыки"]
        self.inv = ["лютня", "Лук из древесины магического дерева", "грибная похлёбка"]


player = Person(name="Ахилес", person_classes="Лучник", is_enemy=False, is_alive=True)
enemy = Person(name="Ахарон", person_classes="Воин", is_enemy=True, is_alive=True)

