# Задача 6
# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

def SumElements(num):
    sum = 0
    ost = 0
    while num > 0:
        ost = num % 10
        sum += ost
        num //= 10
    return sum
        
num = int(input("Введите число: "))
num1 = num // 1000
num2 = num % 1000
sum1 = SumElements(num1)
sum2 = SumElements(num2)

if sum1 == sum2:
    print("YES")
else:
    print("NO")  


# ...........Альтернативное решение
# num = int(input("Введите число: "))
# num1 = num // 1000
# num2 = num % 1000

# sum1 = 0
# ost1 = 0
# while num1 > 0:
#     ost1 = num1 % 10
#     sum1 += ost1
#     num1 //= 10

# sum2 = 0
# ost2 = 0
# while num2 > 0:
#     ost2 = num2 % 10
#     sum2 += ost2
#     num2 //= 10

# if sum1 == sum2:
#     print("YES")
# else:
#     print("NO")
