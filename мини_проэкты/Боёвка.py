import random
import os
import time


clear = lambda: os.system('cls')

role = {
    '1': 'Воин',
    '2': 'Лучник',
    '3': 'Маг'
}

classes = {
    'Воин': {
        'здоровье': 100,
        'атака': 50,
        'защита': 40,
        'навыки': {
            'щит': 20
        }
    },
    'Лучник': {
        'здоровье': 70,
        'атака': 80,
        'защита': 25,
        'навыки': {
            'убежать': 10
        }
    },
    'Маг': {
        'здоровье': 50,
        'атака': 90,
        'защита': 15,
        'навыки': {
            'магический щит': 45,
            'лечение': 20
        }
    }
}


def init_person(name: str, is_enemy: bool = False) -> dict[str, str | dict[str, int | dict]]:
    if is_enemy:
        person = {'класс': role[random.choice(list(role.keys()))]}
    else:
        while True:
            choice = input("Введите роль: 1-Воин, 2-Лучник, 3-Маг\n")
            if is_valid(text=choice, is_role=True):
                break

        person = {'класс': role[choice]}

    person.update({'характеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(f"{person['имя']} - {person['класс']}, имеет характеристики: {person['характеристики']}")
    return person


def is_valid(text: str, is_role: bool = False) -> bool:
    if len(text) == 0:
        print('Ошибка ввода. Вы ввели пустую строку.')
        return False
    elif text not in '123' and is_role == True:
        print('Ошибка ввода. Вы ввели не правильное значение. Введите числа от 1 до 3.')
        return False
    else:
        return True


def get_player_name() -> str:
    while True:
        player_name = input(f'Как зовут твоего героя?\n')
        if is_valid(player_name):
            break
    return player_name


def get_random_name() -> str:
    first = ['Доктор', 'Летающий', 'подлый', 'Профессор', 'Скучный', 'Мега', 'Железный', 'Голодный', 'Капитан',
             'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Просто', 'гениальный', 'Восхитительный',
             'Непобедимый', 'самостоятельный ']
    second = ['слесарь', 'шепард' 'мухомор', 'пепел', 'лемур', 'шаман', 'мэис', 'пельмень', 'прайс', 'слизень',
              'алхимик', 'крот', 'фикус', 'кролик', 'гоуст', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ', 'соуп']

    first_second = random.choice(first) + ' ' + random.choice(second)

    return first_second


def apply_skill(enemy) -> None:
    rand = random.randint(0, 9)
    if rand > 6:
        skill = random.choice(list(enemy['характеристики']['навыки'].keys()))  # Выбирает случайный навык
        enemy['характеристики']['здоровье'] += enemy['характеристики']['навыки'][skill]
        print(
            f"{enemy['имя']} применяет способность {skill}!")


def enter() -> None: input("*Нажмите Enter, чтобы продолжить*")


def attack_enemy(enemy1: dict[str, str | dict], enemy2: dict[str, str | dict]) -> None:
    print(f"{enemy1['имя']} атакует {enemy2['имя']}")
    time.sleep(2)

    damage = enemy1['характеристики']['атака'] - enemy2['характеристики']['защита']
    if damage < 0:
        damage = 1

    enemy2['характеристики']['здоровье'] -= damage
    print(f"{enemy1['имя']} наносит {damage} урона и у {enemy2['имя']} остаётся {enemy2['характеристики']['здоровье']} здоровья!")


def aggressive_fight(attacker: dict[str, str | dict], defender: dict[str, str | dict]) -> bool:
    while True:
        time.sleep(2)
        clear()

        if attacker['характеристики']['здоровье'] > 0:
            attack_enemy(attacker, defender)
        else:
            print(f"{attacker['имя']} выйграл!!")
            return False

        if defender['характеристики']['здоровье'] > 0:
            attack_enemy(defender, attacker)
        else:
            print(f"{defender['имя']} проиграл!!")
            return True


clear()

player = init_person(get_player_name())
enemy = init_person(get_random_name(), True)

enter()


# attack_enemy(player, enemy)
aggressive_fight(player, enemy)
