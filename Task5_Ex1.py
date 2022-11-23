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


number_of_rounds = int(input('Введите количество бросков '))

first_player = {
    "name": new_player_name(),
    "score": 0
}

second_player = {
    "name": new_player_name(),
    "score": 0
}

for i in range(0, number_of_rounds, 1):
    first_player["score"] += throw_dice(first_player["name"])
    print()
    second_player["score"] += throw_dice(second_player["name"])
    print()

print('Сумма очков игрока', first_player["name"], first_player["score"])
print('Сумма очков игрока', second_player["name"], second_player["score"])
print(game_result(first_player, second_player))