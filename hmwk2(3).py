# Задание 3.
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
seasons_list = ['-', 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer',
                'autumn', 'autumn', 'autumn', 'winter', ]
print(seasons_list[int(input('Введите номер месяца: '))])

seasons_dict = {'3': 'spring', '4': 'spring', '5': 'spring', '6': 'summer', '7': 'summer', '8': 'summer',
                '9': 'autumn', '10': 'autumn', '11': 'autumn', '12': 'winter', '1': 'winter', '2': 'winter'}
print(seasons_dict[input('Введите номер месяца: ')])

