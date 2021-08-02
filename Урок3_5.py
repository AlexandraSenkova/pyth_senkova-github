"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел
к полученной ранее сумме и после этого завершить программу.
"""


def calc_func(my_string):
    my_string_num = my_string.split()
    sum_init = 0
    if '!' not in my_string_num:
        for i in range(0, (len(my_string_num))):
            sum_init = sum_init + int(my_string_num[i])
        return sum_init, True
    elif my_string_num.index('!') > 0:
        for el in range(0, (my_string_num.index('!'))):
            sum_init = sum_init + int(my_string_num[el])
        return sum_init, False
    else:
        return sum_init, False


continue_flag = True
calc_sum = 0
while continue_flag:
    my_string = input('Введите числа через пробел. Cимвол: ! завершит программу: ')
    calc_sum_curr, continue_flag = calc_func(my_string)
    calc_sum += calc_sum_curr
    print('Промежуточная сумма: ', calc_sum)
print('Результирующая сумма: ', calc_sum)

