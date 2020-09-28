# Задание 5.
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент: '))
for i in range(len(my_list)):
    if new_el == my_list[i]:
        my_list.insert(i + 1, new_el)
        break
    elif new_el > my_list[0]:
        my_list.insert(0 + 1, new_el)
        break
    elif new_el < my_list[-1]:
        my_list.append(new_el)
        break
    elif my_list[i] > new_el and my_list[i+1] < new_el:
        my_list.insert(i+1, new_el)
print(my_list)
