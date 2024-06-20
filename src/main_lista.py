import pygame
from settings import * 

pygame.init()


SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('primer juego')

clock = pygame.time.Clock()



block = [pygame.Rect(300, 250, 100, 100), RED, DL]

block_2 = pygame.Rect(240, 120, 100, 100)
block_color_2 = RED
block_dir_2 = DR

rect = 0 
color = 1 
dire = 2 

SCREEN.fill((CUSTOM))
 
continuar = True
speed = 5
gravedad = True
gravedad_1 = True
gravedad_2 = True


while continuar: 
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            continuar = False 


    # actualizar elementos 

    if block[dire] == DR: 
        block[rect].x += speed
        block[rect].y += speed 


    elif block[dire] == DL: 
        block[rect].x -= speed
        block[rect].y += speed 

    elif block[dire] == UL: 
        block[rect].x -= speed
        block[rect].y -= speed 

    elif block[dire] == UR: 
        block[rect].x += speed
        block[rect].y -= speed 


    # actualizar direccion 
    if block[rect].right >= WIDTH:
        if block[dire] == DR: 
            block[dire] = DL 
        else: 
            block[dire] = UL 


    elif block[rect].left <= rect: 
        if block[dire] == DL: 
            block[dire] = DR 
        else:
            block[dire] = UR

    elif block[rect].bottom >= HEIGHT: 
        if block[dire] == DR:
            block[dire] = UR
        else: 
            block[dire] = UL

    elif block[rect].top <= rect: 
        if block[dire] == UR:
            block[dire] = DR
        else: 
            block[dire] = DL





    SCREEN.fill(CUSTOM)
    pygame.draw.rect(SCREEN, block[color], block[rect])




    # if gravedad: 
    #     if rect_1.top >= rect:
    #         rect_1[rect] -= speed
    #     else: 
    #         gravedad = not gravedad
   
    # else: 
    #     if rect_1.bottom <= HEIGHT:
    #         rect_1[rect] += speed
    #     else: 
    #         gravedad = not gravedad


    # if gravedad_1: 
    #     if rect_1.left >= rect:
    #         rect_1[rect] -= speed
    #     else: 
    #         gravedad_1 = not gravedad_1
   
    # else: 
    #     if rect_1[rect] <= WIDTH:
    #         rect_1[rect] += speed
    #     else: 
    #         gravedad_1 = not gravedad_1



    
    # if gravedad_2: 
    #     if rect_2.left >= rect:
    #         rect_2[rect] -= speed
    #     else: 
    #         gravedad_2 = not gravedad_2
   
    # else: 
    #     if rect_2[rect] <= WIDTH:
    #         rect_2[rect] += speed
    #     else: 
    #         gravedad_2 = not gravedad_2
    
    


    

    # rect_2 = pygame.draw.ellipse(SCREEN, RED, (rect,rect,200,100))
    # pygame.draw.rect(SCREEN, YELLOW, rect_2, 3)


    # rect_3 = pygame.draw.circle(SCREEN, MAGENTA, SCREEN_CENTER, 75, 3 )
   

    # rect_4 = pygame.draw.line(SCREEN, BLACK,rect_2.center, rect_3.center,  3)
    # pygame.draw.rect(SCREEN, WHITE, rect_4, 3)


    # rect_5 = pygame.draw.polygon(SCREEN, BLUE, [(50,20),(400,200) ,(300, 500)], 3)
    # pygame.draw.rect(SCREEN, BLACK, rect_5, 3)
    

    pygame.display.flip()

pygame.quit()   