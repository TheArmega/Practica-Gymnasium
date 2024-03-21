#!/usr/bin/env python

# Importa las bibliotecas necesarias
import gymnasium as gym
import gymnasium_csv
import numpy as np
import time

# Define el sistema de coordenadas para el archivo CSV y numpy
"""
Coordinate Systems for `.csv` and `print(numpy)`

X points down (rows); Y points right (columns); Z would point outwards.

*--> Y (columns)
|
v
X (rows)
"""

# Define constantes para las direcciones de movimiento
UP = 0
UP_RIGHT = 1
RIGHT = 2
DOWN_RIGHT = 3
DOWN = 4
DOWN_LEFT = 5
LEFT = 6
UP_LEFT = 7

# Define el período de simulación en milisegundos
SIM_PERIOD_MS = 500.0

# Crea el entorno especificando el nombre, modo de renderizado, archivo CSV y posiciones inicial y final
env = gym.make('gymnasium_csv-v0',
                render_mode='human',  # "human", "text", None
                inFileStr='../assets/map2.csv',
                initX=1,
                initY=1,
                goalX=8,
                goalY=16)

# Inicializa el entorno y obtiene la observación inicial y la información del entorno
observation, info = env.reset()
print("observation: "+str(observation)+", info: "+str(info))
env.render()
time.sleep(0.5)

# Define una serie de movimientos predefinidos
moves = [DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, DOWN_RIGHT, RIGHT, RIGHT]

# Itera sobre los movimientos y ejecuta cada uno en el entorno
for i in moves:
        observation, reward, terminated, truncated, info = env.step(i)
        env.render()
        # Imprime la observación, la recompensa y otros detalles del paso
        print("observation: " + str(observation)+", reward: " + str(reward) + ", terminated: " +
                str(terminated) + ", truncated: " + str(truncated) + ", info: " + str(info))
        time.sleep(SIM_PERIOD_MS/1000.0)  # Espera para simular el paso del tiempo
