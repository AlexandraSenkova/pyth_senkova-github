"""7. Реализовать генератор с помощью функции с ключевым словом
yield, создающим очередное значение.
При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом:
for el in fact(n).
Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n.
Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24."""

from functools import reduce
from itertools import count


def fact(n):
    res_fact = 1
    for i in count(1):
        if i <= n:
            res_fact = res_fact * i
            # reduce(lambda x, y: x*y, range(1, i+1))
            yield res_fact
        else:
            break


for el in fact(int(input('Введите число: '))):
    print(el)
