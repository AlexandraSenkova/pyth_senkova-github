"""4.	Создать (не программно) текстовый файл
со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и
считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


my_dict = {"One": "Один",
           "Two": "Два",
           "Three": "Три",
           "Four": "Четыре",
           "Five": "Пять",
           "Six": "Шесть",
           "Seven": "Семь",
           "Eight": "Восемь",
           "Nine": "Девять",
           "Ten": "Десять"}

with open('file5_4.txt') as file_r, open('file5_4_1.txt', 'w') as file_w:
    for line in file_r.readlines():
        num_eng_name, num = line.rstrip().split(' - ')
        file_w.write(f'{my_dict[num_eng_name]} — {num}\n')

#
