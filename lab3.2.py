import numpy as np
import matplotlib.pyplot as plt

# Вектор проектирования
s = np.array([-1, 1, -1])

# Матрицы проекций
P = np.array([
    [0, 0, 0],
    [1, 1, 0],
    [-1, 0, 1]
])

F = np.array([
    [1, 0, -1],
    [0, 1, 1],
    [0, 0, 0]
])

H = np.array([
    [1, 1, 0],
    [0, 0, 0],
    [0, 1, 1]
])

# Определим фигуру для проектирования (например, куб)
fig = np.array([
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, 1],
    [1, -1, -1],
    [-1, 1, 1],
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, -1, -1]
])

# Функция для визуализации
def plot_projection(ax, projected_fig, title):
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.scatter(projected_fig[:, 0], projected_fig[:, 1], c='r')
    for i in range(len(projected_fig)):
        for j in range(i+1, len(projected_fig)):
            ax.plot([projected_fig[i, 0], projected_fig[j, 0]], [projected_fig[i, 1], projected_fig[j, 1]], 'b')

# Проекции
fig_P = fig.dot(P.T)
fig_F = fig.dot(F.T)
fig_H = fig.dot(H.T)

# Визуализация
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

plot_projection(axs[0], fig_P, 'Profile Projection')
plot_projection(axs[1], fig_F, 'Frontal Projection')
plot_projection(axs[2], fig_H, 'Horizontal Projection')

plt.tight_layout()
plt.show()