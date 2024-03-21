#!/usr/bin/env python
from collections import deque

import gymnasium as gym
import gymnasium_csv

import time
import csv

"""
# Coordinate Systems for `.csv` and `print(numpy)`

X points down (rows); Y points right (columns); Z would point outwards.

*--> Y (columns)
|
v
X (rows)
"""

# Definición de las constantes de dirección
UP = 0
UP_RIGHT = 1
RIGHT = 2
DOWN_RIGHT = 3
DOWN = 4
DOWN_LEFT = 5
LEFT = 6
UP_LEFT = 7

SIM_PERIOD_MS = 500.0


# Función para verificar si un movimiento es válido en la matriz
def is_valid_move(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0

# Función para obtener la dirección de movimiento entre dos puntos
def get_direction(parent, current, next):
    direction_map = {
        (-1, 0): "Arriba",
        (1, 0): "Abajo",
        (0, -1): "Izquierda",
        (0, 1): "Derecha",
        (-1, -1): "Arriba-Izquierda",
        (-1, 1): "Arriba-Derecha",
        (1, -1): "Abajo-Izquierda",
        (1, 1): "Abajo-Derecha"
    }
    dr = next[0] - current[0]
    dc = next[1] - current[1]
    return direction_map[(dr, dc)]

# Implementación del algoritmo BFS (Breadth-First Search)
def bfs(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])
    visited = set()
    parent = {}
    queue = deque([(start[0], start[1])])
    visited.add(start)

    while queue:
        row, col = queue.popleft()

        if (row, col) == end:
            path = []
            while (row, col) != start:
                path.append((row, col))
                row, col = parent[(row, col)]
            path.append(start)
            path.reverse()
            return path

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(grid, new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                parent[(new_row, new_col)] = (row, col)
                queue.append((new_row, new_col))

    return []

# Función para convertir un archivo CSV en una matriz
def csv_to_matrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append([int(cell) for cell in row])
    return matrix

# Función para mapear las direcciones a las constantes definidas
def addDirection(direction, directions):
    direction_map = {
        "Arriba": UP,
        "Abajo": DOWN,
        "Izquierda": LEFT,
        "Derecha": RIGHT,
        "Arriba-Izquierda": UP_LEFT,
        "Arriba-Derecha": UP_RIGHT,
        "Abajo-Izquierda": DOWN_LEFT,
        "Abajo-Derecha": DOWN_RIGHT
    }
    
    if direction in direction_map:
        directions.append(direction_map[direction])

# Ruta al archivo CSV que define la matriz del entorno
file_path = '../assets/map2.csv'  # Cambia 'data.csv' por la ruta de tu archivo CSV
matrix = csv_to_matrix(file_path)

start = (1, 1)
goal = (8, 16)
directions = []

# Encuentra el camino utilizando BFS
path = bfs(matrix, start, goal)
if path:
    print("Camino encontrado:")
    for i in range(len(path) - 1):
        current = path[i]
        next = path[i + 1]
        direction = get_direction(path, current, next)
        print(f"Ir {direction} desde {current} a {next}")
        addDirection(direction, directions)
    print(f"Moviéndome a {goal}")
else:
    print("No se encontró un camino válido.")

# Configuración del entorno de Gym
env = gym.make('gymnasium_csv-v0',
                render_mode='human',  # "human", "text", None
                inFileStr='../assets/map2.csv',
                initX=1,
                initY=1,
                goalX=8,
                goalY=16)
observation, info = env.reset()
print("observation: "+str(observation)+", info: "+str(info))
env.render()
time.sleep(0.5)

# Ejecución de los movimientos en el entorno de Gym
for i in directions:
        observation, reward, terminated, truncated, info = env.step(i)
        env.render()
        print("observation: " + str(observation)+", reward: " + str(reward) + ", terminated: " +
                str(terminated) + ", truncated: " + str(truncated) + ", info: " + str(info))
        time.sleep(SIM_PERIOD_MS/1000.0)
