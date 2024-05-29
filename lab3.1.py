import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Исходные точки тетраэдра
vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Грани тетраэдра
faces = [
    [vertices[0], vertices[1], vertices[2]],
    [vertices[0], vertices[1], vertices[3]],
    [vertices[0], vertices[2], vertices[3]],
    [vertices[1], vertices[2], vertices[3]]
]

# Углы поворота
alpha = np.pi / 3
beta = -np.pi / 6
gamma = 0

# Матрица поворота вокруг оси Ox
R_x = np.array([
    [1, 0, 0],
    [0, np.cos(alpha), -np.sin(alpha)],
    [0, np.sin(alpha), np.cos(alpha)]
])

# Матрица поворота вокруг оси Oy
R_y = np.array([
    [np.cos(beta), 0, np.sin(beta)],
    [0, 1, 0],
    [-np.sin(beta), 0, np.cos(beta)]
])

# Матрица поворота вокруг оси Oz
R_z = np.array([
    [np.cos(gamma), -np.sin(gamma), 0],
    [np.sin(gamma), np.cos(gamma), 0],
    [0, 0, 1]
])

# Общая матрица поворота
R = R_x @ R_y @ R_z

# Применение матрицы поворота к вершинам тетраэдра
rotated_vertices = vertices @ R.T

# Поворотные грани тетраэдра
rotated_faces = [
    [rotated_vertices[0], rotated_vertices[1], rotated_vertices[2]],
    [rotated_vertices[0], rotated_vertices[1], rotated_vertices[3]],
    [rotated_vertices[0], rotated_vertices[2], rotated_vertices[3]],
    [rotated_vertices[1], rotated_vertices[2], rotated_vertices[3]]
]

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax_rotated = fig.add_subplot(122, projection='3d')

# Исходный тетраэдр
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
ax.set_title('Исходный тетраэдр')

# Повернутый тетраэдр
ax_rotated.add_collection3d(Poly3DCollection(rotated_faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))
ax_rotated.set_title('Повернутый тетраэдр')

# Настройка осей
for axis in [ax, ax_rotated]:
    axis.set_xlabel('X')
    axis.set_ylabel('Y')
    axis.set_zlabel('Z')
    axis.set_xlim([0, 1])
    axis.set_ylim([0, 1])
    axis.set_zlim([0, 1])

plt.show()