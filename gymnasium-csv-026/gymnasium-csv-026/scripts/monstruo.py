#!/usr/bin/env python

import gymnasium as gym
import gymnasium_csv
import numpy as np
import time
import keyboard

"""
# Coordinate Systems for `.csv` and `print(numpy)`

X points down (rows); Y points right (columns); Z would point outwards.

*--> Y (columns)
|
v
X (rows)
"""
UP = 0
UP_RIGHT = 1
RIGHT = 2
DOWN_RIGHT = 3
DOWN = 4
DOWN_LEFT = 5
LEFT = 6
UP_LEFT = 7

SIM_PERIOD_MS = 500.0

def on_key_pressed(event):
    print(f"Pulsada la tecla: {event.name}")
    if event.name == 'flecha arriba':
        return UP
    elif event.name == 'flecha abajo':
        return DOWN
    elif event.name == 'flecha izquierda':
        return LEFT
    elif event.name == 'flecha derecha':
        return RIGHT
    else:
        print("Tecla no válida. Solo se permiten las teclas de flecha.")
        return -1



env = gym.make('gymnasium_csv-v0',
                render_mode='human',  # "human", "text", None
                inFileStr='../assets/monstruo_1.csv',
                initX=6,
                initY=1,
                goalX=6,
                goalY=22)
observation, info = env.reset()
print("observation: "+str(observation)+", info: "+str(info))
env.render()
time.sleep(0.5)

validation = True
count = 1
while validation:
    count += 1
    if count > 3:
        count = 1
    # Esperar a que se pulse una tecla
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:  # Verificar si es un evento de pulsación de tecla
        move = event.name  # Obtener el nombre de la tecla pulsada
        if move == 'esc':
            validation = False
            break
        move = on_key_pressed(event)  # Convertir el nombre de la tecla en un movimiento
        if move == -1:
            print("Tecla no válida. Solo se permiten las teclas de flecha.")
            continue
        else:
            observation, reward, terminated, truncated, info = env.step(move)
            env.render()
            env = gym.make('gymnasium_csv-v0',
                render_mode='human',  # "human", "text", None
                inFileStr='../assets/monstruo_'+str(count)+'.csv',
                initX=observation[0],
                initY=observation[1],
                goalX=6,
                goalY=22)
            observation, info = env.reset()
            print("observation: " + str(observation)+", reward: " + str(reward) + ", terminated: " +
                    str(terminated) + ", truncated: " + str(truncated) + ", info: " + str(info))
            if terminated:
                print("¡Has llegado a la meta y has conseguido todos los puntos!")
                validation = False # Salir del bucle después de obtener una pulsación de tecla
            #time.sleep(SIM_PERIOD_MS/1000.0)

