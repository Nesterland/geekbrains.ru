# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

dat_int = 12
dat_float = 5.6
dat_str = "Строка"
dat_list = ['i', '8']
dat_tuple = ('d', '8')
dat_dict = {'city': 'Chishinau', 'country': 'Moldova'}

data_list = [dat_dict, dat_float, dat_int, dat_list, dat_tuple, dat_str]
for i in data_list:
    print(f'Данные: {i} -- определен класс: {type(i)}')