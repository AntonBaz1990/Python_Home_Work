# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

def FuntionSquer(n) :
    i = 1
    while i <= n:   
        print(i, end=' ')
        i = i * 2
        
num = int(input("Введите число: "))
FuntionSquer(num)