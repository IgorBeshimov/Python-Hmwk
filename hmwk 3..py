# Задание 3.
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
number = input('Введите любое число: ')
formula1 = int(number + number)
formula2 = int(number + number + number)
sum = int(number) + formula1 + formula2
print(sum)