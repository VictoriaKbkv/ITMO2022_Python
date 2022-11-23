from random import randint
import time

number_of_rounds = int(input('Введите количество бросков '))

#Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')

total_score1 = 0
total_score2 = 0

for i in range(0, number_of_rounds, 1):
    #Моделирование бросания кубика первым играющим
    print('Кубик бросает', igrok1)
    time.sleep(1)
    n1 = randint(1, 6)
    print('Выпало:', n1)
    total_score1 = total_score1 + n1
    #Моделирование бросания кубика вторым играющим
    print('Кубик бросает', igrok2)
    time.sleep(1)
    n2 = randint(1, 6)
    total_score2 = total_score2 + n2
    print('Выпало:', n2)

print('Сумма очков игрока', igrok1, total_score1)
print('Сумма очков игрока', igrok2, total_score2)

#Определение результата (3 возможных варианта)
if total_score1 > total_score2:
    print('Выиграл', igrok1)
elif total_score1 < total_score2:
    print('Выиграл', igrok2)
else:
    print('Ничья')