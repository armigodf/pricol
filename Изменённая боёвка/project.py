import colorama
import random
import time
import os


white_color = colorama.Fore.WHITE
green_color = colorama.Fore.GREEN
red_color = colorama.Fore.RED
blue_color = colorama.Fore.BLUE


role = {'1': 'Воин', '2': 'Лучник', '3': 'Маг'}

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


def is_valid(text: str, is_role: bool = False) -> bool:
    if len(text) <= 0:
        print(f'{red_color}Ошибка ввода. Вы ввели пустую строку.{white_color}')
        return False
    elif text not in '123' and is_role:
        print(f'{red_color}Ошибка ввода. Вы ввели не правильное значение. Введите числа от 1 до 3.{white_color}')
        return False
    else:
        return True


def get_player_name() -> str:
    while True:
        player_name = input(f'{blue_color}Как зовут твоего героя?\n{white_color}')
        if is_valid(player_name):
            break
    return player_name


def get_random_name() -> str:
    from random import choice
    first_names = ['Доктор', 'Летающий', 'Светящийся', 'Профессор', 'Неимоверный', 'Мега', 'Железный', 'Голодный',
                   'Капитан', 'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Стойкий', 'Восхитительный',
                   'Непобедимый']
    second_names = ['слесарь', 'мухомор', 'пепел', 'лемур', 'шаман', 'пельмень', 'слизень', 'алхимик', 'крот', 'фикус',
                    'господин', 'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']
    return f"{choice(first_names)} {choice(second_names)}"


def apply_skill(target) -> None:
    random_int = random.randint(0, 9)
    if random_int > 6:
        skill = random.choice(list(target['характеристики']['навыки'].keys()))
        target['характеристики']['здоровье'] += target['характеристики']['навыки'][skill]

        print(f"{blue_color}{target['имя']} применяет способность {green_color}{skill}{white_color}!")


def enter_to_continue() -> None: input('Нажмите Enter, чтобы продолжить.')


def clear() -> int: return os.system('cls')  # os.system('clear') - для linux и macOS


def init_person(name: str, is_enemy: bool = False) -> dict[str, str | dict[str, int | dict]]:
    if is_enemy:
        person = {'класс': role[random.choice(list(role.keys()))]}
    else:
        while True:
            choice = input(f"{blue_color}Введите роль: 1-Воин, 2-Лучник, 3-Маг\n{white_color}")
            if is_valid(text=choice, is_role=True):
                break

        person = {'класс': role[choice]}

    person.update({'характеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(f"{blue_color}{person['имя']} - {person['класс']}, имеет характеристики: {person['характеристики']}{white_color}")
    return person


def attack_enemy(enemy1: dict[str, str | dict], enemy2: dict[str, str | dict]) -> None:
    print(f"{green_color}{enemy1['имя']}{white_color} атакует {red_color}{enemy2['имя']}{white_color}!")
    time.sleep(0.5)

    apply_skill(enemy2)

    damage: int = enemy1['характеристики']['атака'] - enemy2['характеристики']['защита']
    if damage < 0:
        damage = 1

    enemy2['характеристики']['здоровье'] -= damage
    print(
        f"{enemy1['имя']} наносит {red_color}{damage} урона{white_color} и у {enemy2['имя']} остается {green_color}{enemy2['характеристики']['здоровье']}{white_color} здоровья!"
    )


def fight_for_the_win(attacker: dict[str, str | dict], defender: dict[str, str | dict]) -> bool:
    while True:
        clear()
        time.sleep(0.5)

        if attacker['характеристики']['здоровье'] > 0:
            attack_enemy(attacker, defender)
        else:
            print(f"{red_color}{attacker['имя']} потерпел поражение!{white_color}")
            return False

        if defender['характеристики']['здоровье'] > 0:
            attack_enemy(defender, attacker)
        else:
            print(f"{green_color}{defender['имя']} потерпел поражение!{white_color}")
            return True
        enter_to_continue()


clear()

player = init_person(name=get_player_name())
enemy = init_person(name=get_random_name(), is_enemy=True)

enter_to_continue()
clear()

fight_for_the_win(player, enemy)
