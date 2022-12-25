# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
# 6 12

import os
os.system('cls')

def RandomArray(n) :  
    import random
    m = []
    eagle = 0 
    for i in range(0, n):
        random_num = round(random.randint(1, 20))
        m.append(random_num)
    return m    
num1 = int(input("Введите количество элементов первого набора: "))
num2 = int(input("Введите количество элементов второго набора: "))
array1 = RandomArray(num1)
array2 = RandomArray(num2)
print(array1)
print(array2)
setA = set(array1)
setB = set(array2)
res1 = setA & setB
print(res1)

# Альтернативная решение вывода пересечения множеств
setA.intersection(setB)
res2 = setA.intersection(setB)
print(res2)



