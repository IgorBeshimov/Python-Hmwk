# Звдание 3.
# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
with open('test3.txt', 'w', encoding='utf-8') as f:
    f.writelines('Петров 250134.13\nСидоров 19135.15\nИванов 35035.45')
with open('test3.txt', 'r', encoding='utf-8') as f:
    sal =[]
    poor_fellow = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split(' ')
        if float(i[1]) < 20000:
            poor_fellow.append(i[0])
        sal.append(i[1])
    print(f'Зарплата меньше 20000 у: {poor_fellow}, а средняя зарплата по всем сотрудникам составит: '
          f'{round(sum(map(float, sal)) / len(sal))}')