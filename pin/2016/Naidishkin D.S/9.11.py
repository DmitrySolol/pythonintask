﻿# Задача 9. Вариант 11.
# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, 
# есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". 
# Вслед за тем игрок должен попробовать отгадать слово.
# Naidishkin D.S. 
# 22.04.2017

print ("""Программа случайным образом загадывает слово и сообщает количество букв в нём.
Вы должны угадать его.
\n\t\t\tП Р А В И Л А
\t\t==============================
Тебе даётся пять попыток узнать есть ли какая-либо буква в слове.
Программа тебе сообщит, есть ли введённая тобой буква слове или её нет.
\t\t==============================
\t\t\tУдачной игры!""")
import random
WORDS =("машина", "анаграмма", "игра", "пользователь", "ответчик", "барометр")
word = random.choice(WORDS)


print("Букв в слове:", len(word)) 	
for i in range(5):
	answer = input("Ваш вариант: ")
	if (answer.lower() == word.lower()):
		print("Да")
		break
	else:
		print("Нет")
print("Игра закончена. Нажмите Enter чтобы выйти.")	
input()