# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a , b, c):
    if a <= b or a <= c:
        return b + c
    elif b <= a or b <= c:
        return a + c
    else:
        return a + b

print(f'Cумма двух наибольших чисел = {my_func(int(input("Введите значение a ")), int(input("Введите значение b ")), int(input("Введите значение c ")))}')
