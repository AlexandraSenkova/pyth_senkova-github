"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def id_func(**kwargs):
    return f"Имя: {kwargs['name']}, Фамилия: {kwargs['surname']}, " \
           f"Год рождения: {kwargs['b_year']}, Город проживания: {kwargs['cur_city']}, " \
           f"Email: {kwargs['email']}, Контактный телефон: {kwargs['cell']}"


print(id_func(name='Петя', surname='Иванов', b_year=2018, cur_city='Москва',
              email='v.ivanov@mail.net', cell=88888888888))


print(id_func(
               name=input('enter name: '),
               surname=input('enter surname: '),
               b_year=int(input('enter birth year: ')),
               cur_city=input('enter current city: '),
               email=input('enter email:'),
               cell=int(input('enter cell number: '))))
