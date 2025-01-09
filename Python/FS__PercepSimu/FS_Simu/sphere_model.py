from vpython import sphere, vector, color, canvas, button, rate, box, cylinder

# Configurar la escena
scene = canvas(width=800, height=600, background=color.gray(0.8), title="Simulación: Esfera Roja")
plano_cenital = box(canvas=scene, pos=vector(0, -0.5, 0), size=vector(20, 0.01, 10), color=color.white)

# Crear la esfera roja
esfera = sphere(pos=vector(0, -0.3, 0), radius=0.2, color=color.red)

# Variables de control
animando = False
pos_inicial = vector(1, -0.25, 0)  # Posición inicial de la cámara

# Crear cuadrícula
def crear_cuadricula(canvas):
    step = 1
    grid_size_x = int(plano_cenital.size.x / 2)
    grid_size_z = int(plano_cenital.size.z / 2)

    for x in range(-grid_size_x, grid_size_x + 1, step):
        cylinder(canvas=canvas, pos=vector(x, -0.49, -grid_size_z), axis=vector(0, 0, 2 * grid_size_z), radius=0.01, color=color.black)
    for z in range(-grid_size_z, grid_size_z + 1, step):
        cylinder(canvas=canvas, pos=vector(-grid_size_x, -0.49, z), axis=vector(2 * grid_size_x, 0, 0), radius=0.01, color=color.black)

crear_cuadricula(scene)

# Función para iniciar/resetear la posición
def initiate():
    global animando
    animando = False
    scene.camera.pos = pos_inicial  # Restablecer la posición inicial de la cámara
    scene.camera.axis = vector(-1, 0, 0)  # Mantener la cámara mirando paralelo al plano

# Función para animar la rotación, alejamiento y acercamiento de la cámara
def animar():
    global animando
    if animando:  # Si ya está animando, no iniciar otra animación
        return
    animando = True
    while animando:  # Animar hasta que se presione "Initiate"
        rate(100)

        # Rotar la cámara
        scene.camera.pos = scene.camera.pos.rotate(angle=0.1, axis=vector(0, 1, 0))
        # Mantener la cámara siempre paralela al plano
        scene.camera.axis = vector(-scene.camera.pos.x, 0, -scene.camera.pos.z).norm()

        # Alejarse de la esfera
        for _ in range(300):  # Más pasos para suavizar
            rate(120)  # Velocidad controlada
            scene.camera.pos = vector(scene.camera.pos.x * 1.005, -0.25, scene.camera.pos.z * 1.005)

        # Acercarse a la posición inicial
        for _ in range(300):  # Más pasos para suavizar
            rate(120)  # Velocidad controlada
            scene.camera.pos = vector(scene.camera.pos.x * 0.995, -0.25, scene.camera.pos.z * 0.995)

# Botones para controlar la animación
button(text="Initiate", bind=initiate)  # Botón para reiniciar
button(text="Animate", bind=animar)    # Botón para animar

# Evitar cierre automático
while True:
    rate(100)
