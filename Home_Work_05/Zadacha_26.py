# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

import os
os.system('cls')

def Powx(a1, b1):
    if b1 == 0: return 1
    if b1 == 1: return a1
    return a1 * Powx(a1, b1-1)

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
result = Powx(a, b)
print("Результат возведения в степень равен:", result)
