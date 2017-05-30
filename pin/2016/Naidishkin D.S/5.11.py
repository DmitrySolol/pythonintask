# Задача 5. Вариант 11.
# Напишите программу, которая бы при запуске случайным образом отображала
# имя одного из девяти оленей Санта Клауса.
# Naidishkin D.S. 
# 16.03.2017

print ("Данная программа случайным образом отображает имя одного из девяти оленей Санта Клауса")
import random
import string
deer = ["Dasher","Dancer","Prancer","Vixen","Comet","Cupid","Donder","Blitzen","Rudolf"]
print("\nОдного из девяти оленей Санта Клауса звали ", random.choice(deer))
input("\n\n\n\n\n\nPress Enter to exit from program...")