import pygame
from random import * 



WIDTH = 800
HEIGHT = 600

SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_CENTER = (SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2)


DR = 3 
UR = 9 
DL = 1 
UL = 7 

DIRECCIONES = [DR, UR, DL, UL]

YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
CYAN = (0,255,255)
MAGENTA= (255,0,255)
GREEN_OSCURO = (76, 122, 31)
CUSTOM = (157,208,230)


COLORS = [RED, YELLOW, WHITE, BLACK, BLUE, GREEN, CYAN, MAGENTA, GREEN_OSCURO]
FPS = 60 

# devolver elemento random de una lista
def get_random_element(lista:list) -> any:
    if isinstance(lista, list): 
        return lista[randrange(len(lista))]
       

    else: 
        raise ValueError('no es una lista') 

def color_random(): 
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def update_color(color, step=1):
    r, g, b = color
    r = (r + step) % 256
    g = (g + step) % 256
    b = (b + step) % 256
    return (r, g, b)



def nuevo(rect, color, dire, borde,radio) -> dict:
    nuevo = {}
    nuevo['rect'] = rect
    nuevo['color'] = color
    nuevo['dire'] = dire
    nuevo['borde'] = borde
    nuevo['radio'] = radio    
    return nuevo




def new_block(numero, block_width, block_height): 
    lista = []

    for i in range(numero): 
        i = nuevo(pygame.Rect(randint(0, WIDTH - block_width), randint(0, HEIGHT - block_height),block_width,block_height),get_random_element(COLORS), get_random_element(DIRECCIONES), 0, -1)
        lista.append(i)
    return lista 