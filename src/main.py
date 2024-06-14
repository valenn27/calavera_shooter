import pygame
from settings import * 

pygame.init()


SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('primer juego')



SCREEN.fill((CUSTOM))

contador = 0 
continuar = True

while continuar: 
    print(contador)
    contador += 1 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            continuar = False 


    pygame.display.flip()

pygame.quit()   