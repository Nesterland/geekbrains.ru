# задание 1_2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time_user = int(input('ведите время в секундах: '))
cas = time_user // 3600
min = (time_user - cas * 3600) // 60
sek = time_user % 60
print(f'Часы: {cas} Минуты: {min} Секунды: {sek}')