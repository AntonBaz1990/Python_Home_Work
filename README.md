# Домашнее задание Семинар 1

## Задача 2
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)

## Задача 4
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1 4 1
24 -> 4 16 4
60 -> 10 40 10

## Задача 6
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no

## Задача 8
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Пример:
3 2 4 -> yes
3 2 1 -> no


# Домашнее задание Семинар 2

## Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2

## Задача 12
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
 Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.

## Задача 14

Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.
5 -> 1 2 4
17 -> 1 2 4 8 16


# Домашнее задание Семинар 3

## Задача 14
Задача 16:Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N/2.
Выведите, сколько раз X встречается в массиве.
Ввод: 5
Ввод: 1
1 2 1 2 2
Вывод: 2

## Задача 18:
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
Заполните массив случайными натуральными числами от 1 до N.
Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
Ввод: 10
Ввод: 7
1 2 1 8 9 6 5 4 3 4
Вывод: 6

## Задача 20:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.

А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков.

Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
Ввод: ноутбук
Вывод: 12

# Домашнее задание Семинар 4

## Задача 22: 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа.
n - кол-во элементов первого набора.
m - кол-во элементов второго набора.
Значения генерируются случайным образом.
Input: 11 6
(значения сгенерированы случайным образом
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18)
Output: 11 6
6 12

## Задача 24:
В фермерском хозяйстве в Карелии выращивают чернику.
Она растет на круглой грядке, причем кусты высажены только по окружности.
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. 
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки.
Input: 4
(значения сгенерированы случайным образом
4 2 3 1 )
Output: 9

# Домашнее задание Семинар 5

## Задача 26:
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

## Задача 28:
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# Домашнее задание Семинар 6

##Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
.
Структура данных:
Фамилия, имя, отчество, номер телефона.
.
Пример данных:
Ivanov, Ivan, Ivanovich, +79111234567
Petrov, Petr, Petrovich, +79119876543
.
Функции справочника:
- Показать все записи
- Найти запись по вхождению частей имени
- Найти запись по телефону
- Добавить новый контакт
- Удалить контакт
- Изменить номер телефона у контакта
.
Пример работы программы:
.
При запуске программы пользователю выдается меню:

Введите номер действия:
1 - Показать все записи
2 - Найти запись по вхождению частей имени
3 - Найти запись по телефону
4 - Добавить новый контакт
5 - Удалить контакт
6 - Изменить номер телефона у контакта
7 - Выход
.
После выбора действия выполняется функция, реализующая это действие.
После завершения работы функции пользователь возвращается в меню. 

# Домашнее задание Семинар 7

## Урок 7. Python: от простого к практике
Продолжить работу над справочником автобусного парка.


# Домашняя работа 8 Семинар

## Урок 8. Python: от простого к практике
Вычислить значение выражения
Уровень 1:
    1 действие
    2 аргумента 12 + 15
Уровень 2:
    Количество действий произвольное
12 + 15 - 4
Уровень 3:
    Действия имеют приоритет
12 - 4*2 +6/3
Уровень 4 * (дополнительная задача, сдавать не обязательно)
    Действия разделяются скобками
(12 - 4) * 2 


# Домашнее задание 9 Семинар

## Урок 9. Возможна ли жизнь без PIP?
Реализовать телеграмм бота, который может здороваться с пользователем по имени и складывать числа
/hello
/sum

# Домашнее задание 10 Семинар

## Урок 10. Возможна ли жизнь без PIP? Продолжение
Прикрутить к боту новые возможности (один пункт на выбор - все реализовывать не обязательно!):
- игра в крестики-нолики
- игра в конфеты
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
- сообщать пользователю фазу луны в зависимости от даты
- сообщать пользователю, сколько дней осталось до Нового Года
- выдавать случайный афоризм/анекдот (из переменной или текстового файла)
- бот-учитель: выдавать случайное английское слово с переводом (из переменной или текстового файла)