# задача №7 м8
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы больше количество баллов за меньшее кол-во попыток

print("Программа случайным оброзом загадывает название одного из семи холмов, но которых была построенна Москва, а игрок должен его угадать")
print("Чем быстрее вы угадаете, тем боьше баллов за игру получите")

import random as r

b = 10000
x = ['Боровицкий', 'Введенская горка', 'Таганский', 'Трехгорка', 'Ваганьковский', 'Сретенский', 'Тверской']

while True:
    n = input("Назовите один из холмов на которых была построенна Москва: ")
    if n != (r.choice(x)):
        print("Вы не угадали!!!")
        print("Правильный ответ был - ", (r.choice(x)))
        print("-1000 баллов")
        print("Попробуй еще раз.")
        b = b - 1000

    else:
        print("Вы угадали!")
        print("Вам зачисленно", b, "баллов")
        break

end = input("\nНажмите Enter для выхода")