# Боевая система к игре
import json
import random
import time
import os


def clear(): return os.system('cls')


clear()

delay = 2

role = {
    '1': 'Воин',
    '2': 'Лучник',
    '3': 'Маг'
}

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


def init_person(name: str, is_enemy: bool = False) -> dict:
    if is_enemy:
        person = {'Класс': role[random.choice(list(role.keys()))]}
    else:
        person = {'Класс': role[input('Введите роль: 1-Воин, 2-Лучник, 3-Маг\n')]}
    
    person.update({'характеристики': classes[person['Класс']]})
    person.update({'имя': name})

    print(f"{person['имя']} - {person['Класс']}, имеет характеристики: {person['характеристики']}")
    return person


def attack(enemy1: dict, enemy2: dict) -> None:
    print(f"{enemy1['имя']} атакует {enemy2['имя']}!")
    time.sleep(delay)
    apply_skill = random.randint(0, 9)
    if apply_skill > 6:
        skill = random.choice(list(enemy2['характеристики']['навыки'].keys()))
        enemy2['характеристики']['здоровье'] += enemy2['характеристики']['навыки'][skill]

        print(f"{enemy2['имя']} применяет способность {skill}!")

    damage = enemy1['характеристики']['атака'] - enemy2['характеристики']['защита']
    if damage < 0:
        damage = 1

    enemy2['характеристики']['здоровье'] -= damage
    print(f"{enemy1['имя']} наносит {damage} урона и у {enemy2['имя']} остается {enemy2['характеристики']['здоровье']} здоровья!")


def battle(attacker: dict, target: dict) -> bool:
    while True:
        time.sleep(delay)
        clear()

        if attacker['характеристики']['здоровье'] > 0:
            attack(attacker, target)
        else:
            print(f"{attacker['имя']} потерпел поражение!")
            return False

        if target['характеристики']['здоровье'] > 0:
            attack(target, attacker)
        else:
            print(f"{target['имя']} потерпел поражение!")
            return True
        proceed()


def proceed(): input('Нажмите Enter, чтобы продолжить.')


enemy_names = ['Гена лысый', 'Василий butterfly', 'Дракон', 'Укроп', 'Роман', 'Дарт', 'Ваас']
player = init_person(name=input('Как зовут твоего героя?\n'))
enemy = init_person(
    name=random.choice(enemy_names),
    is_enemy=True
)
proceed()
clear()

try:
    with open("LOG.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Фаил потерян и старый результат потерян")

data = {}

if player["имя"] not in data:
    data.update({player["имя"]:{
        "победы": 0,
        "Поражения": 0
    }})
if battle(player, enemy):
    data[player["имя"]]["победы"] = data[player["имя"]]["победы"] + 1
    data[enemy["имя"]]["Поражение"] = data[enemy["имя"]]["Поражение"] + 1
else:
    data[player["имя"]]["Поражение"] = data[player["имя"]]["Поражение"] + 1
    data[enemy["имя"]]["победа"] = data[enemy["имя"]]["победа"] + 1

with open("LOG.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)
