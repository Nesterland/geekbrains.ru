#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
namber_user = str(input('Введите число от 1 до 9:' ))
n_1 = namber_user + namber_user
n_2 = namber_user + namber_user + namber_user
print(int(namber_user) +  int(n_1) + int(n_2))