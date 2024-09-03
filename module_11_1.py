
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = x
# Квадратичная зависимость
y2 = [i**2 for i in x]
# Построение графиков
plt.figure(figsize=(9, 9))
plt.subplot(5, 1, 1)
plt.plot(x, y1)               # построение графика
plt.title("работа с библиотеками matplotlib и numpy ") # заголовок
plt.ylabel("y1 = x", fontsize=10) # ось ординат
plt.grid(True)                # включение отображение сетки
plt.subplot(5, 1, 2)
plt.plot(x, y2)               # построение графика
plt.xlabel("x", fontsize=10)  # ось абсцисс
plt.ylabel("y2 = x^2", fontsize=10) # ось ординат
plt.grid(True)                # включение отображение сетки
#fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
#plt.grid()
plt.subplot(5, 1, 3)

plt.plot(x, x**3, label='кубическая')  # Plot some data on the Axes.
plt.plot(x, x**2, label='парабола')  # Plot more data on the Axes...
plt.plot(x, 1000*np.sinc(x), label='1000*sin(x)')  # ... and some more.
#plt.title("Зависимости:  y = x, y = x^2 ,100*sin(x)")
plt.xlabel('x label')  # Add an x-label to the Axes.
plt.ylabel('три графика')  # Add a y-label to the Axes.
plt.legend()
plt.subplot(5, 1, 4)

fruits = ["apple", "peach", "orange", "bannana", "melon"]
counts = [34, 25, 43, 31, 17]
plt.grid(True)
plt.ylabel('диаграмма')
plt.bar(fruits, counts)
plt.legend()

plt.subplot(5, 1, 5)
ax = np.linspace(0, 1, 5)
ay = np.linspace(0, 2, 5)
xg, yg = np.meshgrid(ax, ay)
plt.ylabel("матрица", fontsize=10)
plt.plot(xg, yg, color="r", marker="*",  linestyle="none")
plt.legend()
plt.grid(True)# Add a legend.
plt.show()






