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


# fuentes
consolas = pygame.font.match_font('consolas')
sans_serif = pygame.font.match_font('MS Reference Sans Serif')

# sistema de puntuacion 
puntuacion = 0 
puntuacion_maxima = 0


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
ROJO_ROSADO = ((210, 56, 56, 1))




COLORS = [RED, YELLOW, WHITE, BLACK, BLUE, GREEN, CYAN, MAGENTA, GREEN_OSCURO]
FPS = 60 

# devolver elemento random de una lista
def get_random_element(lista:list) -> any:
    if isinstance(lista, list): 
        return lista[randrange(len(lista))]
       

    else: 
        raise ValueError('no es una lista') 




def detectar_colisiones(rect_1, rect_2) -> bool: 
    if  punto_en_rectangulo(rect_1.topleft, rect_2) or \
        punto_en_rectangulo(rect_1.topright, rect_2) or \
        punto_en_rectangulo(rect_1.bottomleft, rect_2) or \
        punto_en_rectangulo(rect_1.bottomright, rect_2) or \
        punto_en_rectangulo(rect_2.topleft, rect_1) or \
        punto_en_rectangulo(rect_2.topright, rect_1) or \
        punto_en_rectangulo(rect_2.bottomleft, rect_1) or \
        punto_en_rectangulo(rect_2.bottomright, rect_1):
            return True
    
    else: 
        return False



def distancia_entre_punto(punto_1:tuple[int,int], punto_2:tuple[int,int]) -> float:
    base = punto_1[0] - punto_2[0]
    altura = punto_1[1] - punto_2[1]
    return (base ** 2 + altura ** 2) ** 0.5


def detectar_colision_circulo(rect_1, rect_2) -> bool:
    r1 = rect_1.width // 2
    r2 = rect_2.height // 2
    distancia = distancia_entre_punto(rect_1.center, rect_2.center)
    return distancia <= r1 + r2
    


def punto_en_rectangulo(punto, rect) -> bool:  
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom
      