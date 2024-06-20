import pygame
from random import * 
from settings import * 

pygame.init()


SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('primer juego')

clock = pygame.time.Clock()

# block_width = 100
# block_height = 100 

# blocks = [{'rect': pygame.Rect(randint(0, WIDTH - block_width), randint(0, HEIGHT - block_height),block_width,block_height), 'color': get_random_element(COLORS), 'dire': get_random_element(DIRECCIONES), 'borde': 0, 'radio': -1},
# {'rect': pygame.Rect(randint(0, WIDTH - block_width), randint(0, HEIGHT - block_height),block_width,block_height), 'color': get_random_element(COLORS), 'dire': get_random_element(DIRECCIONES), 'borde': 0, 'radio': -1},
# {'rect': pygame.Rect(randint(0, WIDTH - block_width), randint(0, HEIGHT - block_height),block_width,block_height), 'color': get_random_element(COLORS), 'dire': get_random_element(DIRECCIONES), 'borde': 0, 'radio': -1}, ]


blocks = new_block(10,100,100)


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

    for block in blocks: 
    # actualizar elementos 

        if block['dire'] == DR: 
            block['rect'].x += speed
            block['rect'].y += speed 


        elif block['dire'] == DL: 
            block['rect'].x -= speed
            block['rect'].y += speed 

        elif block['dire'] == UL: 
            block['rect'].x -= speed
            block['rect'].y -= speed 

        elif block['dire'] == UR: 
            block['rect'].x += speed
            block['rect'].y -= speed 


        # actualizar direccion 
        if block['rect'].right >= WIDTH:
            if block['dire'] == DR: 
                block['dire'] = DL 
                block['color'] = color_random()
                block['borde'] = randint(0,10)
                
            else: 
                block['dire'] = UL 
                block['color'] = color_random()
                block['borde'] = randint(0,10)
                




        elif block['rect'].left <= 0: 
            if block['dire'] == DL: 
                block['dire'] = DR 
                block['color'] = color_random()
                block['borde'] = randint(0,10)


            else:
                block['dire'] = UR
                block['color'] = color_random()
                block['borde'] = randint(0,10)



        elif block['rect'].bottom >= HEIGHT: 
            if block['dire'] == DR:
                block['dire'] = UR
                block['color'] = color_random()
                block['borde'] = randint(0,10)


            else: 
                block['dire'] = UL
                block['color'] = color_random()
                block['borde'] = randint(0,10)



        elif block['rect'].top <= 0: 
            if block['dire'] == UR:
                block['dire'] = DR
                block['color'] = color_random()
                block['borde'] = randint(0,10)
                block['radio'] = randint(-1,50)



            else: 
                block['dire'] = DL
                block['color'] = color_random()
                block['borde'] = randint(0,10)
                block['radio'] = randint(-1,50)

    


    SCREEN.fill(CUSTOM)

    for block in blocks: 
        pygame.draw.rect(SCREEN, block['color'], block['rect'], block['borde'], block['radio'])




    # if gravedad: 
    #     if rect_1.top >= 'rect':
    #         rect_1['rect'] -= speed
    #     else: 
    #         gravedad = not gravedad
   
    # else: 
    #     if rect_1.bottom <= HEIGHT:
    #         rect_1['rect'] += speed
    #     else: 
    #         gravedad = not gravedad


    # if gravedad_1: 
    #     if rect_1.left >= 'rect':
    #         rect_1['rect'] -= speed
    #     else: 
    #         gravedad_1 = not gravedad_1
   
    # else: 
    #     if rect_1['rect'] <= WIDTH:
    #         rect_1['rect'] += speed
    #     else: 
    #         gravedad_1 = not gravedad_1



    
    # if gravedad_2: 
    #     if rect_2.left >= 'rect':
    #         rect_2['rect'] -= speed
    #     else: 
    #         gravedad_2 = not gravedad_2
   
    # else: 
    #     if rect_2['rect'] <= WIDTH:
    #         rect_2['rect'] += speed
    #     else: 
    #         gravedad_2 = not gravedad_2
    
    


    

    # rect_2 = pygame.draw.ellipse(SCREEN, RED, ('rect','rect',200,100))
    # pygame.draw.'rect'(SCREEN, YELLOW, rect_2, 3)


    # rect_3 = pygame.draw.circle(SCREEN, MAGENTA, SCREEN_CENTER, 75, 3 )
   

    # rect_4 = pygame.draw.line(SCREEN, BLACK,rect_2.center, rect_3.center,  3)
    # pygame.draw.'rect'(SCREEN, WHITE, rect_4, 3)


    # rect_5 = pygame.draw.polygon(SCREEN, BLUE, [(50,20),(400,200) ,(300, 500)], 3)
    # pygame.draw.'rect'(SCREEN, BLACK, rect_5, 3)
    

    pygame.display.flip()

pygame.quit()   