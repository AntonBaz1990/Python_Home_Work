# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6
import os
os.system('cls')

import os
os.system('cls')

def RandomArray(n) :  
    import random
    m = []
    eagle = 0 
    for i in range(0, n):
        random_num = round(random.randint(1, n))
        m.append(random_num)
    return m  

def nearElement (array=[]):
    min = array[0]
    difference = abs(X - min)
    for i in array:
        max  = abs(X - i)
        if difference > max :
            min = i
            difference = max 
    return min

N = int(input("Введите количество элементов в массиве: "))
X = int(input("Введите число X: "))
array = RandomArray(N)
print(array)
min_number = nearElement(array)
print("Ближайший элемент к", X, "является: ", min_number)
