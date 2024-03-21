# Practica-Gymnasium

Para el desarrollo de esta práctica he incluido las siguientes implementaciones:

1. Movernos de un punto A a un punto B
2. Movernos con las teclas de dirección
   - Explicación del código
    - Vídeos demostración
3. Juego de recoger todos los puntos
   - Explicación del código
    - Videos demostración
4. Juego de esquivar a los enemigos
   - Explicación del código
    - Videos demostración
5. Implementación algoritmo BFS
   - Explicación del código
    - Videos demostración
6. Creación de mapas
   - Mapa sin obstáculos
    - Mapa con obstáculos
    - Laberinto
    - Mapa de puntos
    - Mapa de enemigos

## Movernos de un punto A a un punto B
Para poder llevar a cabo este scrip he seguido el script de ejemplo dado por el enunciado de la práctica. De esta manera se va de esquina a esquina en el mapa ``mapa2.csv''.

```
python
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

```

