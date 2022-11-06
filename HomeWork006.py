# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.

n = 0
while n < 1:
    n = int(input('Введите положительное число: '))
lst = [(1 + 1 / i) ** i for i in range(1, n + 1)]
result = 0
for i in range(len(lst)):
    result += lst[i]
print(round(result, 2))



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = 0
while n < 1:
    n = int(input('Введите положительное число: '))
lst = [i for i in range(1, n + 1)]
for i in range(1, len(lst)):
    lst[i] *= lst[i-1]
print(lst)


# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

lst = [1, 4, -3, 6, 0, -5, 5, 22, -1, 9]
lst = [lst[i] for i in range (len(lst)) if i % 2]
sum = 0
for i in range(len(lst)):
    sum += lst[i]
print(lst, sum)


# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

n = 0
while n < 1:
    n = int(input('Введите положительное число: '))
lst = [i for i in range(1, n + 1)]
result = [lst[i] * lst[-i-1] for i in range(int(len(lst)/2 + 1))]
print(lst)
print(result)
