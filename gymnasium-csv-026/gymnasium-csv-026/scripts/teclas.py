import gymnasium as gym
import gymnasium_csv
import numpy as np
import time
import keyboard  # Librería para la gestión de la entrada del teclado

# Constantes que representan las direcciones de movimiento
UP = 0
UP_RIGHT = 1
RIGHT = 2
DOWN_RIGHT = 3
DOWN = 4
DOWN_LEFT = 5
LEFT = 6
UP_LEFT = 7

# Período de simulación en milisegundos
SIM_PERIOD_MS = 500.0

# Función que se ejecuta cuando se presiona una tecla
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

# Crear el entorno Gym
env = gym.make('gymnasium_csv-v0',
                render_mode='human',  # Modo de renderizado ("human", "text", None)
                inFileStr='../assets/map2.csv',  # Ruta del archivo CSV que define el mapa
                initX=1,  # Posición inicial X del agente
                initY=1,  # Posición inicial Y del agente
                goalX=8,  # Posición objetivo X
                goalY=16)  # Posición objetivo Y
observation, info = env.reset()  # Inicializar el entorno y obtener la observación inicial e información del entorno
print("observation: "+str(observation)+", info: "+str(info))
env.render()  # Renderizar el entorno
time.sleep(0.5)

validation = True
while validation:
    # Esperar a que se pulse una tecla
    event = keyboard.read_event()  # Leer el evento del teclado
    if event.event_type == keyboard.KEY_DOWN:  # Verificar si es un evento de pulsación de tecla
        move = event.name  # Obtener el nombre de la tecla pulsada
        if move == 'esc':  # Verificar si se ha presionado la tecla 'esc' para salir
            validation = False
            break
        move = on_key_pressed(event)  # Convertir el nombre de la tecla en un movimiento
        if move == -1:  # Verificar si el movimiento es inválido
            print("Tecla no válida. Solo se permiten las teclas de flecha.")
            continue
        else:
            # Ejecutar el movimiento en el entorno
            observation, reward, terminated, truncated, info = env.step(move)
            env.render()  # Renderizar el entorno después del movimiento
            if terminated:  # Verificar si se ha terminado la simulación
                print("¡Has llegado a la meta!")
                validation = False  # Salir del bucle después de obtener una pulsación de tecla
            time.sleep(SIM_PERIOD_MS/1000.0)  # Esperar para simular el paso del tiempo
