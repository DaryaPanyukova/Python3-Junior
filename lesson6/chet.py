from random import randint
n=5
prav=0
for i in range(n):
    while True:
        otvet=int(input(" введите чет(2) или нечет(1) "))
        if otvet!=1 and otvet!=2:
            print(" Попробуйте еще раз! Нужно ввести 1 или 2")
        else:
            break

    n_comp=randint(1,2)

    if otvet==n_comp:
        print("Число, загаданное компьютером ", n_comp, ". вы угадали")
        prav+=1
    else:
        print("вы проиграли ")
if prav>n//2:
    print("вы выиграли")
else:
    print("вы проиграли")
    
