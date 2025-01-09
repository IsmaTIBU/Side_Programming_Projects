from vpython import box, vector, scene, button, rate, color, cylinder, label, sphere

# Configurar la escena
scene.width = 800  # Ancho de la ventana
scene.height = 600  # Alto de la ventana
scene.background = vector(0.8, 0.8, 0.8)  # Color de fondo (gris claro)
scene.title = "Simulación: Bloque en Movimiento con Cámara Dinámica"  # Título de la ventana

# Crear el bloque
bloque = box(pos=vector(0, 0, 0), size=vector(1, 0.5, 1), color=vector(0.2, 0.5, 0.8))

# Crear un plano como referencia
plano = box(pos=vector(0, -0.5, 0), size=vector(20, 0.01, 10), color=color.white, opacity=1)

# Crear una etiqueta para mostrar la posición del cubo
pos_label = label(pos=bloque.pos + vector(0, 1.5, 0), text="X=0.00, Y=0.00", box=False, height=12, color=color.black, line=False)

# Crear una cuadrícula
def crear_cuadricula():
    step = 1  # Espaciado entre líneas de la cuadrícula
    grid_size_x = int(plano.size.x / 2)  # Límite en el eje X
    grid_size_z = int(plano.size.z / 2)  # Límite en el eje Z

    # Líneas paralelas al eje Z
    for x in range(-grid_size_x, grid_size_x + 1, step):
        cylinder(pos=vector(x, -0.49, -grid_size_z), axis=vector(0, 0, 2 * grid_size_z), radius=0.01, color=color.black)

    # Líneas paralelas al eje X
    for z in range(-grid_size_z, grid_size_z + 1, step):
        cylinder(pos=vector(-grid_size_x, -0.49, z), axis=vector(2 * grid_size_x, 0, 0), radius=0.01, color=color.black)

# Llamar a la función para dibujar la cuadrícula
crear_cuadricula()

# Configurar la cámara para una vista inicial
scene.camera.pos = vector(0, 9, 0)  # Posición inicial de la cámara
scene.camera.axis = bloque.pos - scene.camera.pos  # La cámara mira al bloque

# Variables para controlar la animación
animating = False
position_initiated = False

# Crear las esferas antes de la animación
def generar_esferas():
    """Generar esferas rojas (izquierda) y amarillas (derecha) a lo largo del trayecto."""
    x_start = 1
    x_end = 9  # Largo del trayecto (ajustar según el movimiento del cubo)
    step = 1  # Separación entre esferas en x
    for x in range(int(x_start / step), int(x_end / step)):
        x_pos = x * step
        sphere(pos=vector(x_pos, 0, -1), radius=0.2, color=color.red)  # Esfera roja a la izquierda
        sphere(pos=vector(x_pos, 0, 1), radius=0.2, color=color.yellow)  # Esfera amarilla a la derecha

generar_esferas()
def actualizar_posicion():
    """Actualiza la etiqueta con la posición del cubo y la coloca junto a este."""
    pos_label.text = f"X={bloque.pos.x:.2f}, Y={bloque.pos.y:.2f}"
    pos_label.pos = bloque.pos + vector(0, 1.5, 0)  # Coloca la etiqueta justo encima del cubo

def initiate():
    """Coloca el cubo en la posición inicial deseada y genera las esferas."""
    global position_initiated
    bloque.pos = vector(0, 0, 0)  # Cambia esta posición inicial si lo deseas
    position_initiated = True
    scene.camera.pos = vector(bloque.pos.x, 9, 0)  # Ajustar la cámara a la posición inicial
    scene.camera.axis = bloque.pos - scene.camera.pos  # Mantener la cámara mirando al cubo
    generar_esferas()  # Generar las esferas antes de iniciar la animación
    actualizar_posicion()  # Actualizar la etiqueta con la posición inicial

def animar():
    """Función para animar el movimiento del cubo."""
    global animating, position_initiated
    if not position_initiated:
        print("Primero debes iniciar la posición del cubo usando el botón 'Initiate'.")
        return
    animating = True
    for t in range(600):  # 600 pasos de simulación
        rate(30)  # Controla la velocidad de la simulación (30 fps)
        bloque.pos.x += 0.01  # Movimiento hacia adelante en el eje X

        # Actualizar la posición de la cámara y la etiqueta para que sigan al cubo
        scene.camera.pos = vector(bloque.pos.x, 9, 0)
        scene.camera.axis = bloque.pos - scene.camera.pos  # Mantener la cámara mirando al cubo
        actualizar_posicion()  # Actualizar la etiqueta con la nueva posición del cubo

    animating = False  # Termina la animación


# Agregar botones para iniciar la posición y animar
button(text="Initiate", bind=lambda: initiate())
button(text="Animate", bind=lambda: animar())

# Evitar que la ventana se cierre automáticamente
while True:
    rate(300)
