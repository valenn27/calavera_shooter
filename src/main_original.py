import pygame
from settings import * 

pygame.init()


SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('primer juego')

clock = pygame.time.Clock()


block = pygame.Rect(300, 250, 100, 100)
block_color = RED
block_dir = DR


block_2 = pygame.Rect(240, 120, 100, 100)
block_color_2 = RED
block_dir_2 = DR



rect_2 = pygame.Rect(0, 0, 200, 100)
rect_2.center = SCREEN_CENTER

SCREEN.fill((CUSTOM))

contador = 0 
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

    if block_dir == DR: 
        block.x += speed
        block.y += speed 


    elif block_dir == DL: 
        block.x -= speed
        block.y += speed 

    elif block_dir == UL: 
        block.x -= speed
        block.y -= speed 

    elif block_dir == UR: 
        block.x += speed
        block.y -= speed 


    # actualizar direccion 
    if block.right >= WIDTH:
        if block_dir == DR: 
            block_dir = DL 
        else: 
            block_dir = UL 


    elif block.left <= 0: 
        if block_dir == DL: 
            block_dir = DR 
        else:
            block_dir = UR

    elif block.bottom >= HEIGHT: 
        if block_dir == DR:
            block_dir = UR
        else: 
            block_dir = UL

    elif block.top <= 0: 
        if block_dir == UR:
            block_dir = DR
        else: 
            block_dir = DL





    SCREEN.fill(CUSTOM)
    pygame.draw.rect(SCREEN, block_color, block)




    # if gravedad: 
    #     if rect_1.top >= 0:
    #         rect_1.y -= speed
    #     else: 
    #         gravedad = not gravedad
   
    # else: 
    #     if rect_1.bottom <= HEIGHT:
    #         rect_1.y += speed
    #     else: 
    #         gravedad = not gravedad


    # if gravedad_1: 
    #     if rect_1.left >= 0:
    #         rect_1.x -= speed
    #     else: 
    #         gravedad_1 = not gravedad_1
   
    # else: 
    #     if rect_1.right <= WIDTH:
    #         rect_1.x += speed
    #     else: 
    #         gravedad_1 = not gravedad_1



    
    # if gravedad_2: 
    #     if rect_2.left >= 0:
    #         rect_2.x -= speed
    #     else: 
    #         gravedad_2 = not gravedad_2
   
    # else: 
    #     if rect_2.right <= WIDTH:
    #         rect_2.x += speed
    #     else: 
    #         gravedad_2 = not gravedad_2
    
    


    

    # rect_2 = pygame.draw.ellipse(SCREEN, RED, (0,0,200,100))
    # pygame.draw.rect(SCREEN, YELLOW, rect_2, 3)


    # rect_3 = pygame.draw.circle(SCREEN, MAGENTA, SCREEN_CENTER, 75, 3 )
   

    # rect_4 = pygame.draw.line(SCREEN, BLACK,rect_2.center, rect_3.center,  3)
    # pygame.draw.rect(SCREEN, WHITE, rect_4, 3)


    # rect_5 = pygame.draw.polygon(SCREEN, BLUE, [(50,20),(400,200) ,(300, 500)], 3)
    # pygame.draw.rect(SCREEN, BLACK, rect_5, 3)
    

    pygame.display.flip()

pygame.quit()   