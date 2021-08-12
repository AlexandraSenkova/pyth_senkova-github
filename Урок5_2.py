"""2.	Создать текстовый файл (не программно),
сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке."""


with open('file5_2.txt') as my_text_file:
    content = my_text_file.readlines()
    print('Количество строк:', len(content))
    for el in range(0, len(content)):
        word_num = len(content[el].split())
        print(f'Строка {el+1} состоит из {word_num} слов')
