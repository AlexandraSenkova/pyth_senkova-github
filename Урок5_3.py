"""3.	Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов
(не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32"""


sum = 0


with open('file5_3.txt') as file:
    lines = file.readlines()
    for line in lines:
        surname, salary = line.split()
        sum += int(salary)
        if int(salary) < 20000:
            print(f'{surname} с окладом менее 20 000')

    print(f"Cредний оклад составляет: {sum/len(lines)}")
