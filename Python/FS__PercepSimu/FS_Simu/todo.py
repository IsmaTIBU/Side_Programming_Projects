from vpython import canvas, box, vector, sphere, color, cylinder, label, button, rate

# Configurar dos lienzos: uno para la vista cenital y otro para el punto de vista del bloque
cenital = canvas(width=647, height=400, background=color.gray(0.8), align="left")
pov = canvas(width=646, height=400, background=color.gray(0.8), align="right")

# Variables globales
animating = False
position_initiated = False

# Crear el bloque en ambas vistas
bloque_cenital = box(canvas=cenital, pos=vector(0, -0.25, 0), size=vector(1, 0.5, 1), color=vector(0.2, 0.5, 0.8))
bloque_pov = box(canvas=pov, pos=vector(0, -0.25, 0), size=vector(1, 0.5, 1), color=vector(0.2, 0.5, 0.8))

# Crear planos en ambas vistas
plano_cenital = box(canvas=cenital, pos=vector(0, -0.5, 0), size=vector(20, 0.01, 10), color=color.white)
plano_pov = box(canvas=pov, pos=vector(0, -0.5, 0), size=vector(20, 0.01, 10), color=color.white)

# Crear etiquetas
pos_label_cenital = label(canvas=cenital, pos=bloque_cenital.pos + vector(0, 1.5, 0), text="X=0.00, Z=0.00", box=False, line=False)
pos_label_pov = label(canvas=pov, pos=pov.camera.pos + vector(0.5, 1, 0), text="X=0.00, Z=0.00", box=False, line=False)

# Crear un disco rojo que se "meta" en la cara del bloque donde se encuentra la cámara del POV
disco_pov = cylinder(canvas=pov, pos=bloque_pov.pos + vector(0.48, 0, 0), axis=vector(-0.02, 0, 0), radius=0.1, color=color.red)

# Crear cuadrícula
def crear_cuadricula(canvas):
    step = 1
    grid_size_x = int(plano_cenital.size.x / 2)
    grid_size_z = int(plano_cenital.size.z / 2)

    for x in range(-grid_size_x, grid_size_x + 1, step):
        cylinder(canvas=canvas, pos=vector(x, -0.49, -grid_size_z), axis=vector(0, 0, 2 * grid_size_z), radius=0.01, color=color.black)
    for z in range(-grid_size_z, grid_size_z + 1, step):
        cylinder(canvas=canvas, pos=vector(-grid_size_x, -0.49, z), axis=vector(2 * grid_size_x, 0, 0), radius=0.01, color=color.black)

crear_cuadricula(cenital)
crear_cuadricula(pov)

# Crear esferas
def generar_esferas(canvas):
    x_start = 0
    x_end = 9
    step = 1

    for x in range(int(x_start / step), int(x_end / step) + 1):
        x_pos = x * step
        sphere(canvas=canvas, pos=vector(x_pos, -0.3, -1), radius=0.2, color=color.red)
        sphere(canvas=canvas, pos=vector(x_pos, -0.3, 1), radius=0.2, color=color.yellow)

generar_esferas(cenital)
generar_esferas(pov)

# Actualizar etiquetas y disco
def actualizar_elementos():
    # Actualizar la etiqueta cenital para mostrar X y Z
    pos_label_cenital.text = f"X={bloque_cenital.pos.x:.2f}, Z={bloque_cenital.pos.z:.2f}"
    pos_label_cenital.pos = bloque_cenital.pos + vector(0, 1.5, 0)

    # Fijar la etiqueta del POV para que siempre esté un poco elevada respecto a la cámara
    pos_label_pov.pos = pov.camera.pos + vector(0.5, 1.2, 0)
    pos_label_pov.text = f"X={bloque_pov.pos.x:.2f}, Z={bloque_pov.pos.z:.2f}"

    # Actualizar la posición del disco para que se "meta" en la cara del bloque
    disco_pov.pos = bloque_pov.pos + vector(0.48, 0, 0)

# Botón de inicio
def initiate():
    global position_initiated
    bloque_cenital.pos = vector(0, -0.25, 0)
    bloque_pov.pos = vector(0, -0.25, 0)
    cenital.camera.pos = vector(0, 9, 0)
    cenital.camera.axis = vector(0, -1, 0)
    pov.camera.pos = bloque_pov.pos + vector(0.5, 0, 0)
    pov.camera.axis = vector(1, 0, 0)
    position_initiated = True
    actualizar_elementos()

# Animación
def animar():
    global animating, position_initiated
    if not position_initiated:
        print("Primero debes iniciar la posición del cubo usando el botón 'Initiate'.")
        return
    if animating:
        return

    animating = True
    for t in range(600):
        rate(30)
        bloque_cenital.pos.x += 0.01
        bloque_pov.pos.x += 0.01
        cenital.camera.pos = vector(bloque_cenital.pos.x, 9, 0)
        pov.camera.pos = bloque_pov.pos + vector(0.5, 0, 0)
        actualizar_elementos()
    animating = False

# Botones
button(canvas=pov, text="Initiate", bind=initiate)
button(canvas=pov, text="Animate", bind=animar)

# Evitar cierre automático
while True:
    rate(300)
