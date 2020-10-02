# Задание 2.
# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите email: ')
number = input('Введите номер телефона: ')


def my_func(name, surname, birth, city, email, number):
    return ' '.join([name, surname, birth, city, email, number])


print(surname, name, birth, city, email, number)
