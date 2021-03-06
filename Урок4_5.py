"""5. Реализовать формирование списка,
используя функцию range() и возможности генератора.
В список должны войти четные числа
от 100 до 1000 (включая границы).
Необходимо получить результат
вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce

even_list = [num for num in range(100, 1001, 2)]
print(f'Четные от 100 до 1000: {even_list}')

res_multiply = reduce(lambda x, y: x*y, even_list)
print(f'Произведение всех элементов: {res_multiply}')
