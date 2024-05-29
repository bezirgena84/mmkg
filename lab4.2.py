import matplotlib.pyplot as plt
import numpy as np

# Координаты вершин исходного полигона
A1 = (0, 0)
A2 = (3, -1)
A3 = (7, 1)
A4 = (10, -2)
A5 = (10, -4)
A6 = (12, -7)

# Секущие узлы
A14 = (10, -10/3)
A16 = (10, -35/6)

# Определение полигонов
P1 = np.array([A1, A14, A16, A1])
P2 = np.array([A2, A3, A4, A14, A2])
P3 = np.array([A5, A6, A16, A5])

# Визуализация
fig, ax = plt.subplots()
ax.plot(*zip(*[A1, A2, A3, A4, A5, A6, A1]), marker='o', color='black')  # Исходный полигон
ax.plot(*zip(*[A1, A14, A16, A1]), marker='o', color='blue')  # Разбиение синей линией

# Отрисовка вершин и подписей
vertices = [A1, A2, A3, A4, A5, A6, A14, A16]
labels = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', "A1/4", "A1/6"]

for vertex, label in zip(vertices, labels):
    ax.text(vertex[0], vertex[1], label, fontsize=12, ha='right')

# Отрисовка каждого из полигонов
ax.fill(*zip(*P1), alpha=0.3, color='red')
ax.fill(*zip(*P2), alpha=0.3, color='green')
ax.fill(*zip(*P3), alpha=0.3, color='yellow')

ax.set_aspect('equal')
plt.show()