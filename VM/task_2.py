# Постройте на одном графике две кривые y(x) для функции двух переменной y(k,x)=cos(k∙x),
# взяв для одной кривой значение k=1, а для другой – любое другое k, не равное 1.



import matplotlib

import numpy as np
import matplotlib.pyplot as plt
r_1 = input('Введите значение коэффициента R для второго графика: ')
r_1 = int(r_1)
y = lambda x: np.cos(x * 1)
y_1 = lambda x: np.cos(x * r_1)
fig = plt.subplots()
x = np.linspace(-3, 3,100)
plt.plot(x, y(x))
plt.plot(x, y_1(x))
plt.show()
