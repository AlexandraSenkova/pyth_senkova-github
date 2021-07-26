# 1.

i = 0
my_list = ['сегодня', 31, {'мес': 'янв'}, 2021, 'года', {'день_нед': 'пятница'}, 'Погода', 'хорошая', -10, True,
           'градусов', 'ниже', 0, 'Выпадет', 'снег:', 0.7, 'ежемесячной', 'нормы']
for my_list[i] in my_list:
    print(type(my_list[i]))
    i += 1


# 2.

my_list = list(input('Заполните список значениями: '))
i = 0
b = len(my_list)
if len(my_list) % 2 == 0:
    for elements in range(1, b, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
    print(my_list)
else:
    for elements in range(1, b - 1, 2):
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
    print(my_list)

# 3.

# через dict
my_cal = {
    1: 'Jan', 2: 'Feb', 3: 'Mar',
    4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep',
    10: 'Oct', 11: 'Nov', 12: 'Dec'
    }
month_num = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if month_num in my_cal.keys():
    print(my_cal.get(month_num))
else:
    print('Число не должно быть менее 1 или более 12! Введите еще раз: ')

# через list
my_cal = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# print(type(my_cal))
try:
    print(my_cal[(int(input('Введите месяц в виде целого числа от 1 до 12: '))-1)])
except Exception as e:
    # т.к. возможно неск. типов ошибок: IndexError or ValueError
    print('Число не должно быть менее 1 или более 12!', type(e))

# через tuple
my_cal = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
# print(type(my_cal))
try:
    print(my_cal[(int(input('Введите месяц в виде целого числа от 1 до 12: '))-1)])
except Exception as e:
    # т.к. возможно неск. типов ошибок: IndexError or ValueError
    print('Число не должно быть менее 1 или более 12! Введите еще раз: ', type(e))


# 4.
i = 0
my_string = input('Введите строку из нескольких слов, разделённых пробелами: ')
# print(type(my_string.split(' ')))
for el in my_string.split(' '):
    if len(el) <= 10:
        print(i + 1, el)
        i += 1
    else:
        print(i + 1, el[:10])
        i += 1

# 5.
# Способ 1
my_list = [7, 5, 3, 3, 2, int(input('Введите новый элемент рейтинга: '))]
print(sorted(my_list, reverse=True))
# Способ 2
my_list = [7, 5, 3, 3, 2]
new_el = (int(input('Введите новый элемент рейтинга: ')))
i = 0
for my_list[i] in my_list:
    if new_el == my_list[i]:
        my_list.insert(i + my_list.count(new_el), new_el)
        print(my_list)
        break

    elif my_list[i] < new_el < my_list[i - 1]:
        my_list.insert(i - 1, new_el)
        print(my_list)
        break

    elif new_el > my_list[0]:
        my_list.insert(0, new_el)
        print(my_list)
        break

    elif new_el < my_list[-1]:
        my_list.append(new_el)
        print(my_list)
        break

    else:
        i += 1
