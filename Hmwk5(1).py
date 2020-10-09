# Задание 1.
# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_func = open('test.txt', 'w')
branch = input('Введите текст \n')
while branch:
    my_func.writelines(branch)
    branch = input('Введите текст \n')
    if not branch:
        break
