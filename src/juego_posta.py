import pygame, sys
from settings import * 

pygame.init()


SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('juego de tiros')
SCREEN.fill(GREEN_OSCURO)


clock = pygame.time.Clock()

# personaje

rect_1 = pygame.Rect(0, 0, 100, 100) 
rect_1.center = SCREEN_CENTER
width = 100
height = 100
px = SCREEN.get_width() // 2 - width // 2
py = SCREEN.get_height() // 2 - height // 2
vel = 5

# fondo 
fondo = pygame.image.load('src/imagenes/pasto.png').convert()




# icono de juego 
icono = pygame.image.load('src/imagenes/calavera.png')
pygame.display.set_icon(icono)

# musica de fondo 
pygame.mixer.music.load('src/musica/musica_doom.mp3')
pygame.mixer.music.play(-1)

# sonido imagenes
subir_volumen = pygame.image.load('src/imagenes/subir_volumen.png')
bajar_volumen = pygame.image.load('src/imagenes/bajar_volumen.png')
maximo_volumen = pygame.image.load('src/imagenes/maximo_volumen.png')
mute_volumen = pygame.image.load('src/imagenes/mute_volumen.png')





bandera = True

continuar = True
while continuar: 
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            continuar = False
    

    SCREEN.blit(fondo, (0,0))

    # moverse 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if py - vel > 0: 
            py -= vel
          
    if keys[pygame.K_s]:
        if py + vel + height < HEIGHT: 
            py += vel 
        
    if keys[pygame.K_a]:
        if px - vel > 0: 
            px -= vel
        else: 
            bandera = not bandera

    if keys[pygame.K_d]:
        if px + vel + width < WIDTH:
            px += vel
        
        

    # audio 
    if keys[pygame.K_9] and pygame.mixer_music.get_volume() >= 0.0: 
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
        SCREEN.blit(subir_volumen, (5,5))
    
    elif keys[pygame.K_9] and pygame.mixer_music.get_volume() == 0.0: 
        SCREEN.blit(mute_volumen, (5,5))


    if keys[pygame.K_0] and pygame.mixer_music.get_volume() <= 1.0: 
        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() -0.01)
        SCREEN.blit(bajar_volumen, (5,5))

    elif keys[pygame.K_0] and pygame.mixer_music.get_volume() == 1.0: 
        SCREEN.blit(maximo_volumen, (0,0))
    

    
    elif keys[pygame.K_m]: 
        pygame.mixer.music.set_volume(0.0)
        SCREEN.blit(mute_volumen, (5,5))

       

    elif keys[pygame.K_n]: 
        pygame.mixer.music.set_volume(1.0)
        SCREEN.blit(maximo_volumen, (5,5))

        
    
    
    
    pygame.draw.rect(SCREEN, GREEN, (px, py, height, width))
    pygame.display.update()  
    


pygame.quit()   
