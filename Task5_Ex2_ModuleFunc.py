from random import randint
import time

def new_player_name():
    player_name = input('Введите имя игрока ')
    return player_name

def throw_dice(player_name):
    print('Кубик бросает', player_name)
    time.sleep(1)
    score = randint(1, 6)
    print('Выпало:', score)
    return score

def game_result(first_player, second_player):
    if first_player["score"] > second_player["score"]:
        return 'Выиграл ' + first_player["name"]
    elif first_player["score"] < second_player["score"]:
        return 'Выиграл ' + second_player["name"]
    else:
        return 'Ничья'
