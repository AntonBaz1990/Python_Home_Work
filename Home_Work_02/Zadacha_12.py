# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

sum = int(input("Введите сумму чисел: "))
proiz =  int(input("Введите произведение чисел: "))
Discrem = sum**2 - 4*proiz

if Discrem < 0 :
    print("По таким введенным числам, решения нет!")
else :
    x = (sum-int((sum**2-4*proiz)**0.5))//2
    y = (sum+int((sum**2-4*proiz)**0.5))//2
    print("Задуманные числа: ", x,"и", y)
    if x > 1000 or y > 1000: 
        print("числа вышли за максимальный диапазон!")   
