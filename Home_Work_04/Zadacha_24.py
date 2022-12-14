# Задача 24:В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )
# Output: 9
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

def Yagoda (a =[] ):
    max = 0
    for i in range(num):
        cursum = sum(a[i:i+3])
        if cursum > max:
            max = cursum
    if a[0] + a[-1] + a[-2] > max:
        max = a[0] + a[-1] + a[-2]
    if a[0] + a[1] + a[-1] > max:
        max = a[0] + a[1] + a[-1]
    return max   

num = int(input("Введите количество кустов: "))
array = RandomArray(num)
print(array)
maxsum = Yagoda(array)
print("Максимальное количество ягод, собираемое за один заход: ", maxsum)
