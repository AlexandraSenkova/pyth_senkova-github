"""5.	Создать (программно) текстовый файл,
записать в него программно набор чисел,
разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и
выводить её на экран."""


with open('file5_5', 'w') as file_w:
    input_numbers = input('Введите числа: ')
    print(input_numbers, file=file_w)

with open('file5_5') as file_r:
    content = file_r.read().rstrip().split()
    numbers = [int(number) for number in content if number.isdigit()]
    print(sum(numbers))
