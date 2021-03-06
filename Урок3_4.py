"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func(x, y):
    """ возведение в степень с помощью оператора ** """
    if x > 0 and y < 0:
        mult_func = x ** y
        return mult_func
    else:
        print(f'x должно быть больше 0, и y - меньше 0')


print(my_func(2, -1))
print(my_func(2, 0))
print(my_func(2, -2))
print(my_func(2, -3))
print(my_func(3, -1))
print(my_func(3, -2))
print(my_func(4, -3))
print('_______')


def my_func(x, y):
    """возведение в степень без оператора **, с использованием цикла """
    if x > 0 and y < 0:
        temp_init = x
        temp_pow = 1
        for i in range(y, 0):
            temp_pow = temp_pow / temp_init
        return temp_pow
    else:
        return f'x должно быть больше 0, и y - меньше 0'


print(my_func(2, -1))
print(my_func(2, 0))
print(my_func(2, -2))
print(my_func(2, -3))
print(my_func(3, -1))
print(my_func(3, -2))
print(my_func(4, -3))
