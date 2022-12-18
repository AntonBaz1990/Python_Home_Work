# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

def RandomArray(n) :  
    import random
    m = []
    eagle = 0 
    for i in range(0, n):
        random_num = round(random.randint(0, 1))
        m.append(random_num)
    return m    

num = int(input("Введите количество монеток: "))
array = RandomArray(num)
print(array)

#...............................................................................
reshka = 0
i = 0
while i < len(array):
    if array[i] == 0:
        reshka += 1
    i+=1
orel = len(array) - reshka 

# for i in array:
#     if array[i] == 0 :
#         reshka += 1

# С циклом FOR программа работает через раз

orel = len(array) - reshka 
print(reshka)
print(orel)

if reshka < orel:
    print("Нужно перевернуть решек: ", reshka)
elif reshka == 0 or orel == 0:
    print("Ничего не нужно переворачивать")  
else :
    print("Нужно перевернуть орлов: ", orel)

    