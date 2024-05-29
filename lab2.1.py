import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаем векторы
a1 = np.array([2, 1, 0])
a2 = np.array([0, 1, 2])
a3 = np.array([1, 0, 0])
b = np.array([1, -2, 2])

# Составляем матрицу из векторов
A = np.column_stack((a1, a2, a3))
B = np.column_stack((b, [0, 0, 0], [0, 0, 0]))

# Находим матрицу оператора
A_inv = np.linalg.inv(A)
phi_matrix = A_inv @ B

print("Матрица оператора φ:")
print(phi_matrix)

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Плоскость
xx, yy = np.meshgrid(range(-10, 11), range(-10, 11))
zz = 2 * yy - xx
ax.plot_surface(xx, yy, zz, alpha=0.5, rstride=100, cstride=100)

# Прямая
t = np.linspace(-10, 10, 100)
x_line = t
y_line = -2 * t
z_line = 2 * t
ax.plot(x_line, y_line, z_line, color='r', label='Прямая ∆: x=y/-2=z/2')

# Настройка графика
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()