# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# 2 2
# 4

def sum_numbers(num1, num2):
    if num2 == 0:
        return num1
    elif num2 == 1:
        return num1 + 1
    else:
        return sum_numbers(num1, num2 - 1) +1


a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
print(sum_numbers(a, b))