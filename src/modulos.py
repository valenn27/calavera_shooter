import pygame, json, os
from settings import * 
from sys import *
from random import randrange


pygame.init()
try: 
    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('calavera shooter')
except pygame.error as e: 
    print(f'error al iniciar el programa')
    

def cargar_configuracion_desde_json(ruta_archivo: str) -> dict: 
    """
    carga la configuración desde un archivo JSON.

    Args:
        ruta_archivo (str): ruta del archivo JSON que contiene la configuración.

    Returns:
        dict: configuración cargada desde el archivo JSON, representada como un diccionario.
    """
    with open(ruta_archivo, 'r') as archivo:
        configuracion = json.load(archivo)
    return configuracion


configuracion = cargar_configuracion_desde_json('src/config.json')

imagenes = {}
sonidos = {}

for elemento in configuracion:
    if elemento['tipo'] == 'imagen':
        imagenes[elemento['nombre']] = pygame.image.load(elemento['ruta'])
    elif elemento['tipo'] == 'sonido':
        sonidos[elemento['nombre']] = pygame.mixer.Sound(elemento['ruta'])


# fondo
try: 
    fondo = imagenes['fondo']
except pygame.error as e: 
    print(f'error al cargar el fondo')


# icono de juego
try: 
    icono = imagenes['icono']
    pygame.display.set_icon(icono)
except pygame.error as e: 
    print(f'error al cargar el icono')


# musica de fondo
try: 
    musica_fondo = sonidos['musica_fondo']
    musica_fondo.play(-1)
    musica_fondo.set_volume(0.3)
except pygame.error as e: 
    print(f'error al cargar la musica')



# sonidos
try: 
    impacto = sonidos['impacto']
    gun_sound1 = sonidos['gun_sound1']
    gun_sound1.set_volume(0.2)
    minecraf_sonido = sonidos['minecraf_sonido']
    minecraf_sonido.set_volume(0.4)
except pygame.error as e: 
    print(f'error al cargar los sonidos')


# imagenes para el audio
try:
    subir_volumen = imagenes['subir_volumen']
    bajar_volumen = imagenes['bajar_volumen']
    maximo_volumen = imagenes['maximo_volumen']
    mute_volumen = imagenes['mute_volumen']
except pygame.error as e: 
    print(f'error al cargar las imagenes')




def mostrar_texto(pantalla:pygame.display, fuente:str, texto:str, color:tuple[int,int,int], dimensiones:int, x:int, y:int) -> None:
    """mostrar texto en pantalla

    Args:
        pantalla (pygame.display): pega en la pantalla el texto
        fuente (str): toma un tipo de fuente de texto
        texto (str): recibe una cadena de caracteres
        color (tuple[int,int,int]): recibe una tupla (en este caso para mostrar un color)
        dimensiones (int): recibe un entero para el tamanio del texto
        x (int): recibe un entero para poner en la posicion x de la pantalla
        y (int): recibe un entero para poner en la posicion y de la pantalla
    """
    tipo_letra = pygame.font.Font(fuente, dimensiones)
    superficie = tipo_letra.render(texto, True, color)
    rectangulo = superficie.get_rect(center=(x, y))
    pantalla.blit(superficie, rectangulo)



def barra_vida(pantalla:pygame.display, x:int, y:int, vida:int) -> None:
    """mostrar la barra de vida

    Args:
        pantalla (pygame.display): pega en la pantalla un rectangulo
        x (int): recibe un entero para poner en la posicion x de la pantalla
        y (int): recibe un entero para poner en la posicion y de la pantalla
        vida (int): recibe un entero que es en este caso la key vida del jugador
    """
    height = 200
    width = 25
    barra_vida = int((vida / 100) * height)
    borde = pygame.Rect(x, y, height, width)
    rectangulo = pygame.Rect(x, y, barra_vida, width)
    pygame.draw.rect(pantalla, GREEN, borde, 3)
    pygame.draw.rect(pantalla, GREEN, rectangulo)


# Inicialización de jugador
jugador = {
    'image': pygame.Surface((50, 50)),
    'rect': None,
    'vida': 100,
    'cantidad_vidas': 3,
    'velocidad_x': 0,
    'velocidad_y': 0,
    'cadencia': 150,
    'ultimo_tiro': pygame.time.get_ticks(),
    'invencible': False
}
jugador['image'] = pygame.transform.scale(imagenes['personaje'], (80,80))
jugador['rect'] = jugador['image'].get_rect(center=(400, 500))



# Listas de elementos
enemigos = []
balas = []
poderes = []

def crear_enemigo() -> None:
    """crear un nuevo enemigo y añadirlo a la lista de enemigos."""
    enemigo = {
        'image': pygame.Surface((70, 70)),
        'rect': None,
        'velocidad_x': randrange(1, 8),
        'velocidad_y': randrange(1, 8),
        'vida': 100,
        'dire': get_random_element(DIRECCIONES)
    }
    enemigo['image'] = pygame.transform.scale(pygame.image.load('src/imagenes/calavera.png'), (70,70))
    enemigo['rect'] = enemigo['image'].get_rect()
    enemigo['rect'].x = randrange(WIDTH - enemigo['rect'].width)
    enemigo['rect'].y = randrange(HEIGHT - enemigo['rect'].width)

    enemigos.append(enemigo)



def crear_bala(x:int, y:int, mouse_x:int, mouse_y:int) -> None:
    """crear una nueva bala y añadirla a la lista de balas.

    Args:
        x (int): posición x inicial de la bala.
        y (int): posición y inicial de la bala.
        mouse_x (int): Posición x del mouse en el momento de disparar.
        mouse_y (int): Posición y del mouse en el momento de disparar.
    """
    bala = {
        'image': pygame.Surface((10, 10)),
        'rect': None,
        'velocidad_x': (mouse_x - x) / 5,
        'velocidad_y': (mouse_y - y) / 5
    }

    pygame.draw.circle(bala['image'], WHITE, (5,5), 5)
    bala['image'].set_colorkey(BLACK)
    bala['rect'] = bala['image'].get_rect(center=(x, y))
    balas.append(bala)


def crear_poder_dios() -> dict:
    """crear un poder de invencibilidad.

    Returns:
        dict: retorna un diccionario con la información del poder.
    """
    poder = {
        'image': pygame.Surface((50, 50)),
        'rect': None,
        'tipo': 'dios'
    }
    poder['image'] = pygame.transform.scale(imagenes['escudo'], (50,50))
    poder['rect'] = poder['image'].get_rect()
    poder['rect'].x = randrange(WIDTH - poder['rect'].width)
    poder['rect'].y = randrange(HEIGHT - poder['rect'].width)

    return poder


def crear_poder_tiro() -> dict:
    """crear un poder de disparo rápido.

    Returns:
        dict: retorna un diccionario con la información del poder.
    """
    poder = {
        'image': pygame.Surface((70, 70)),
        'rect': None,
        'tipo': 'tiro'
    }
    poder['image'] = pygame.transform.scale(imagenes['bala_rapida'], (70,70))
    poder['rect'] = poder['image'].get_rect()
    poder['rect'].x = randrange(WIDTH - poder['rect'].width)
    poder['rect'].y = randrange(HEIGHT - poder['rect'].width)

    return poder




def actualizar_jugador() -> None:
    """actualizar la posición y acciones del jugador"""
    teclas = pygame.key.get_pressed()
    jugador['velocidad_x'] = 0
    jugador['velocidad_y'] = 0

    if teclas[pygame.K_a]:
        jugador['velocidad_x'] = -7
    if teclas[pygame.K_d]:
        jugador['velocidad_x'] = 7
    if teclas[pygame.K_w]:
        jugador['velocidad_y'] = -7
    if teclas[pygame.K_s]:
        jugador['velocidad_y'] = 7

    if pygame.mouse.get_pressed()[0]:
        tiempo_exacto = pygame.time.get_ticks()
        if tiempo_exacto - jugador['ultimo_tiro'] > jugador['cadencia']:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            crear_bala(jugador['rect'].centerx, jugador['rect'].centery, mouse_x, mouse_y)
            jugador['ultimo_tiro'] = tiempo_exacto
            gun_sound1.play()




    jugador['rect'].x += jugador['velocidad_x']
    jugador['rect'].y += jugador['velocidad_y']


    if jugador['rect'].left <= 0:
        jugador['rect'].left = 0

    if jugador['rect'].right >= WIDTH:
        jugador['rect'].right = WIDTH

    if jugador['rect'].top <= 0:
        jugador['rect'].top = 0

    if jugador['rect'].bottom >= HEIGHT:
        jugador['rect'].bottom = HEIGHT



def actualizar_enemigos() -> None:
    """actualizar la posición y acciones de los enemigos"""
    for enemigo in enemigos:


        if enemigo['dire'] == DR:
            enemigo['rect'].x += enemigo['velocidad_x']
            enemigo['rect'].y += enemigo['velocidad_y']


        elif enemigo['dire'] == DL:
            enemigo['rect'].x -= enemigo['velocidad_x']
            enemigo['rect'].y += enemigo['velocidad_y']

        elif enemigo['dire'] == UL:
            enemigo['rect'].x -= enemigo['velocidad_x']
            enemigo['rect'].y -= enemigo['velocidad_y']

        elif enemigo['dire'] == UR:
            enemigo['rect'].x += enemigo['velocidad_x']
            enemigo['rect'].y -= enemigo['velocidad_y']



        if enemigo['rect'].left <= 0:
            enemigo['rect'].right = WIDTH
            enemigo['rect'].y = randrange(HEIGHT - enemigo['rect'].height)

        elif enemigo['rect'].right >= WIDTH:
            enemigo['rect'].left = 0
            enemigo['rect'].y = randrange(HEIGHT - enemigo['rect'].height)

        elif enemigo['rect'].top <= 0:
            enemigo['rect'].bottom = HEIGHT
            enemigo['rect'].x = randrange(WIDTH - enemigo['rect'].width)

        elif enemigo['rect'].bottom >= HEIGHT:
            enemigo['rect'].top = 0
            enemigo['rect'].x = randrange(WIDTH - enemigo['rect'].width)



def actualizar_balas() -> None:
    """actualizar la posición y acciones de las balas"""
    for bala in balas[:]:
        bala['rect'].x += bala['velocidad_x']
        bala['rect'].y += bala['velocidad_y']



        if bala['rect'].bottom < 0 or bala['rect'].top > HEIGHT or bala['rect'].left < 0 or bala['rect'].right > WIDTH:
            balas.remove(bala)
    

def pausa_juego(tecla:int) -> None:
    """pausa el juego

    Args:
        tecla (int): recibe una tecla que al ser presionada, pausa el juego
    """
    
    pygame.mixer.music.pause()
    continuar = True

    while continuar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == tecla:
                    continuar = False
                    pygame.mixer.music.unpause()
             


        mostrar_texto(SCREEN, sans_serif, "PAUSA", WHITE, 40, 400, 300)
        pygame.display.flip()


def dibujar_boton_imagen(pantalla, x:int, y:int, image:pygame.image) -> pygame.Rect: 
    boton_rect = image.get_rect()
    boton_rect.x = x
    boton_rect.y = y
    pantalla.blit(image, boton_rect)

    return boton_rect


def swap_lista(lista:list, i:int, j:int):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux  


def ordenar_puntaje(puntuacion:list) -> list:
    """
    ordena los puntajes de manera descendente.

    Args:
        puntuacion (list): La lista de puntajes.

    Returns:
        list: retorna la lista de puntajes ordenada.
    """
    for i in range(len(puntuacion)):
        for j in range(i + 1, len(puntuacion)):
            if int(puntuacion[i]) < int(puntuacion[j]):
                swap_lista(puntuacion, i, j)

    return puntuacion[:5]