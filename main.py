'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.'''
#a = [1.1, 1.2, 3.1, 5, 10.01]
'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''
n = int(input())
i = 2
while n > 1:
    while n % i == 0:
        print(i, end=' ')
        n //= i
    i += 1

'''Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.'''

numbers = [20, 20, 30, 30, 40]

def get_unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique
'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.'''
