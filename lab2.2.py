import numpy as np
import matplotlib.pyplot as plt
import math

# Установим параметры для визуализации
plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams['figure.dpi'] = 100

# Поворот на угол -π/6 вокруг точки (2, -1)
theta1 = -math.pi / 6
R1 = np.array([
    [math.cos(theta1), -math.sin(theta1), 0],
    [math.sin(theta1), math.cos(theta1), 0],
    [0, 0, 1]
])
T1 = np.array([
    [1, 0, -2],
    [0, 1, 1],
    [0, 0, 1]
])
T1_inv = np.linalg.inv(T1)

# Поворот на угол +π/6 вокруг точки (1, -2)
theta2 = math.pi / 6
R2 = np.array([
    [math.cos(theta2), -math.sin(theta2), 0],
    [math.sin(theta2), math.cos(theta2), 0],
    [0, 0, 1]
])
T2 = np.array([
    [1, 0, -1],
    [0, 1, 2],
    [0, 0, 1]
])
T2_inv = np.linalg.inv(T2)

# Полное преобразование
A = T2 @ R2 @ T2_inv @ T1 @ R1 @ T1_inv
print("Матрица аффинного преобразования A:")
print(A)

def plot_transformation(A, points, label):
    transformed_points = np.dot(A, np.vstack((points.T, np.ones((1, points.shape[0])))))
    plt.plot(points[:, 0], points[:, 1], 'bo-', label=f'{label} (исходные)')
    plt.plot(transformed_points[0, :], transformed_points[1, :], 'ro-', label=f'{label} (преобразованные)')

# Исходные точки
points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
])

# Визуализируем исходные и преобразованные точки
plt.figure()
plot_transformation(A, points, 'Квадрат')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Аффинное преобразование")
plt.show()