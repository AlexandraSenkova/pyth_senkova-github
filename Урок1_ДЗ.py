# Задание 1.
# Поработайте с переменными, создайте несколько, выведите на экран.
name = 'Иван'
surname = 'Петров'
age = 10
print('Привет, %s %s!' % (name, surname))
print('Ого! тебе уже %d лет!' % age)

# Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
name = input('Введите Имя: ')
surname = input('Введите Фамилию: ')
age = int(input('Введите ваш возраст: '))
print(f'Меня зовут {name} {surname}, мне {age} лет.')

# Задание 2.
# способ 1
time = int(input('Введите время в секундах: '))
hours = int(time // 3600)
minutes = int((time - hours * 3600) / 60)
seconds = int(time % 60)
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

# способ 2 (из вебинара)
time = int(input('Введите время в секундах: '))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 3600 % 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

# Задание 3.
# способ 1: t+t*11+t*111
n = int(input('Введите число: '))
num = n + (n * 11) + (n * 111)
print(num)

# способ 2 (из вебинара)
n = input('Введите число: ')
num2 = n*2
num3 = n + n + n
num = int(n) + int(num2) + int(num3)
print(num)

# Задание 4.
# Способ 1
input_number = input('Введите целое положительное число: ')
number_length = len(input_number)
i = 0
# т.к. индекс первого элемента = 0
max_num = 0
while i < number_length:
    current_element = int(input_number[i])
    if current_element > max_num:
        max_num = current_element
    i += 1
print(max_num)

# Способ 2 (ч-з остаток от деления)
input_number = int(input('Введите целое положительное число: '))
max_num = 0
while input_number != 0:
    last_element = input_number % 10
    input_number = input_number // 10
    if last_element > max_num:
        max_num = last_element
        if max_num == 9:
            break
print(max_num)

# Задание 5.
revenue = float(input('Введите сумму выручки, руб.: '))
costs = float(input('Введите сумму издержек, руб.: '))
profit = revenue - costs
if profit > 0:
    print('Выручка больше издержек. Есть прибыль!')
    print(f'Рентабельность капитала, %%: {((profit / revenue)*100):.2f}')
    staff_count = int(input('Введите количество сотрудников:'))
    print(f'Прибыль фирмы в расчёте на одного сотрудника, руб.: {(profit / staff_count):.2f}')
elif profit == 0:
    print('Прибыль равна нулю.')
else:
    print('Издержки больше выручки. Убыток составил %d руб.!' % profit)

# Задание 6.
actual_distance = int(input('Сколько км пробежал(а) в первый день?'))
goal_distance = int(input('Сколько км нужно пробежать?'))
i = 1
while actual_distance < goal_distance:
    actual_distance *= 1.1
    i += 1
print(f'На {int(i)}-й день спортсмен достигнет результата — не менее {goal_distance} км ')
