# Practica-Gymnasium

Para el desarrollo de esta práctica he incluido las siguientes implementaciones:

1. Movernos de un punto A a un punto B
2. Implementación algoritmo BFS
   - Explicación del código
    - Videos demostración
3. Movernos con las teclas de dirección
   - Explicación del código
    - Vídeos demostración
4. Juego de recoger todos los puntos
   - Explicación del código
    - Videos demostración
5. Juego de esquivar a los enemigos
   - Explicación del código
    - Videos demostración
6. Creación de mapas
   - Mapa sin obstáculos
    - Mapa con obstáculos
    - Laberinto
    - Mapa de puntos
    - Mapa de enemigos

## Movernos de un punto A a un punto B
### Código
Para poder llevar a cabo este scrip he seguido el script de ejemplo dado por el enunciado de la práctica. De esta manera se va de esquina a esquina en el mapa ``mapa2.csv''.

```python
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
### Videos



https://github.com/TheArmega/Practica-Gymnasium/assets/38068010/a0e82cb7-4b5f-4341-9a92-bac113f8a8e2


## Implementacion del algoritmo BFS
Mediante la implementación del algoritmo BFS consigo que se vaya de un punto A a un punto B por el camino más corto. Este algoritmo toma como 0 el coste de cada nodo que va visitando y tiene en cuenta los obstáculos.

### Código
El algoritmo se compone de las siguientes funciones:
`is_valid_move`
```python
# Función para verificar si un movimiento es válido en la matriz
def is_valid_move(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0
```

`get_direction`
```python
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
```

`bfs`
```python
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
```

`csv_to_matrix`
```python
# Función para convertir un archivo CSV en una matriz
def csv_to_matrix(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matrix.append([int(cell) for cell in row])
    return matrix
```

`addDirection`
```python
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
```

### Videos


https://github.com/TheArmega/Practica-Gymnasium/assets/38068010/ec0913ab-e5f0-4ee2-aca9-fc50d9427e20



https://github.com/TheArmega/Practica-Gymnasium/assets/38068010/4bcd67d6-8590-4268-8528-e4c0d9675b11



## Movernos con las teclas de dirección
En este scrip lo que hago es habilitar el movimiento del punto por el mapa con las teclas de dirección, habilitando así la navegación interactiva.

### Código
`on_key_pressed`
```python
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
```

`bucle while principal`
```python
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
```
### Videos



https://github.com/TheArmega/Practica-Gymnasium/assets/38068010/e131825d-d5af-4192-9fb8-95a6fdef6f0f



## Juego de recoger todos los puntos
He creado un script que permite manejar el punto con las teclas de direcciones. El objetivo es recoger todos los puntos amarillos del mapa y luego ir a la meta. Hasta que no hayamos recogido todos los puntos amarillos no podremos llegar a la meta.
### Código
Se han tenido que añadir los siguiente elementos en `grid_world`:
```python
if self.inFile[iX][iY] == 4:
   if (iX, iY) == tuple(self._agent_location):
      pygame.draw.rect(canvas, (0, 0, 0),  # Negro si el robot está en el punto 4
                     pygame.Rect(self.cellWidth*iY, self.cellHeight*iX, self.cellWidth, self.cellHeight))
   else:
      pygame.draw.rect(canvas, COLOR_POINT,
                     pygame.Rect(self.cellWidth*iY, self.cellHeight*iX, self.cellWidth, self.cellHeight))
```
```python
elif candidate_state_tag == 4:  # point
   self.inFile[candidate_state[0]][candidate_state[1]] = 0  # Cambiar el punto 4 a 0
   self._agent_location = candidate_state
   reward = 10.0
   terminated = False
```
### Videos




https://github.com/TheArmega/Practica-Gymnasium/assets/38068010/b45f0b81-3f37-498a-a15d-da7fe5f3b738




## Juego de esquivar a los enemigos
En este script he creado un juego en el que hay que manejar el punto con las flechas de dirección para llegar al punto final esquivando a los enemigos, señalados con puntos azules.
### Código
Se han tenido que añadir los siguiente elementos en `grid_world`:
```python
if self.inFile[iX][ºiY] == 5:
   pygame.draw.rect(canvas, COLOR_MONSTER,
                   pygame.Rect(self.cellWidth*iY, self.celHeight*iX, self.cellWidth, self.cellHeight))
```
```python
elif candidate_state_tag == 5:  # monster
   reward = -10.0
   terminated = True
   print("¡Te encontraste con un monstruo! ¡Perdiste!")
```
### Videos


https://github.com/TheArmega/Practica-Gymnasium/assets/38068010/9ed1dfe9-aed5-42c7-9d62-4f08566c4185

