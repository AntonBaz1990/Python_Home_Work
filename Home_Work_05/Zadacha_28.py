# Задача 28:Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

import os
os.system('cls')

def Sum(a, b):
    if b == 0:
        return a
    else:
        if b > 0:
            return Sum(a + 1, b - 1)
        else:
            return Sum(a - 1, b + 1)
a = int(input("Введите число А: "))
b = int(input("Введите число B: "))
result = Sum(a, b)               
print("Сумма двух чисел: ",result)
