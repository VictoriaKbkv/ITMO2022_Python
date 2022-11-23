import Task5_Ex2_ModuleFunc as dice

number_of_rounds = int(input('Введите количество бросков '))

first_player = {
    "name": dice.new_player_name(),
    "score": 0
}

second_player = {
    "name": dice.new_player_name(),
    "score": 0
}

for i in range(0, number_of_rounds, 1):
    first_player["score"] += dice.throw_dice(first_player["name"])
    print()
    second_player["score"] += dice.throw_dice(second_player["name"])
    print()

print('Сумма очков игрока', first_player["name"], first_player["score"])
print('Сумма очков игрока', second_player["name"], second_player["score"])
print(dice.game_result(first_player, second_player))