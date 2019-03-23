from random import randint
import time
igrok1=input("Введите имя игрока 1 ")
igrok2=input("Введите имя игрока 2")
print("Кубик бросает",igrok1)
time.sleep(3)
n1=randint(1,6)
print("Выпало ", n1)
print("Кубик бросает",igrok2)
time.sleep(3)
n2=randint(1,6)
print("Выпало ", n2)
if n1>n2:
      print("Выиграл игрок 1")
elif n2>n1:
      print("Выиграл игрок 2")
else:
     print("Ничья") 
