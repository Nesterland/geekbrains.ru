# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
#  (зима, весна, лето, осень). Напишите решения через list и через dict.
from typing import Dict, Any, Union

number = int(input('Введите номер месяца: '))
month_dict = {1: 'Январь',
              2: 'Февраль',
              3: 'Март',
              4: 'Апрель',
              5: 'Май',
              6: 'Июнь',
              7: 'Июль',
              8: 'Август',
              9: 'Сентябрь',
              10: 'Октябрь',
              11: 'Ноябрь',
              12: 'Декабрь'}
for key in month_dict.keys():#  проходимся по ключам
    if key == number: # сравниваем ключь с вводимым номером
        print(f' Вы ввели номер соотвтствующий месяцу: {month_dict[key]}') # выводим значение ключа

mounth_list = list(month_dict.values())
for i in range(len(mounth_list)):
    if i == number - 1: #  так как интекс начинается с 0 то и от вводимого значения отнимаем 1, чтобы войти в индекс
        print(f'В списке так же будет месяц: {mounth_list[i]}')




