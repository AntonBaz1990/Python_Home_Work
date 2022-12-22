# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве.
# и число, которое необходимо проверить - X.

# 5
# 1 2 3 4 5
# 3
# -> 1
import os
os.system('cls')

def RandomArray(n) :  
    import random
    m = []
    eagle = 0 
    for i in range(0, n):
        random_num = round(random.randint(1, n//2))
        m.append(random_num)
    return m    

def FindNum( num):
    count = 0
    i=0
    for i in array :
        if i == X:
            count += 1
    return count   

N = int(input("Введите количество элементов в массиве: "))
X = int(input("Введитеискомую цифру: "))
array = RandomArray(N)
print(array)
find_num = FindNum(X)          
print("Цифра",X , "встречается", find_num, "раз")        