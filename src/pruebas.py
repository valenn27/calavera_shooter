import pygame, sys
from settings import * 

pygame.init()


SCREEN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('juego de tiros')
SCREEN.fill(GREEN_OSCURO)


clock = pygame.time.Clock()

# personaje
class Jugador(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.Surface((100, 100))
        self.image.fill(GREEN)
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (SCREEN_CENTER)
        self.speed = 5
        self.gravedad = True
        self.gravedad_1 = True
        self.gravedad_2 = True
        

    def update(self):
        # Actualiza esto cada vuelta de bucle.
        if self.gravedad: 
            if self.rect.top >= 0:
                self.rect.y -= self.speed
            else: 
                self.gravedad = not self.gravedad

        else: 
            if self.rect.bottom <= HEIGHT:
                self.rect.y += self.speed
            else: 
                self.gravedad = not self.gravedad


        if self.gravedad_1: 
            if self.rect.left >= 0:
                self.rect.x -= self.speed
            else: 
                self.gravedad_1 = not self.gravedad_1

        else: 
            if self.rect.right <= WIDTH:
                self.rect.x += self.speed
            else: 
                self.gravedad_1 = not self.gravedad_1

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

sprites = pygame.sprite.Group()
jugador = Jugador()
sprites.add(jugador)
continuar = True
while continuar: 
    clock.tick(60)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            continuar = False
    

    SCREEN.blit(fondo, (0,0))


    keys = pygame.key.get_pressed()


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
       
  

        


        
    
    
    
    sprites.update()
    sprites.draw(SCREEN)  
    pygame.display.update()
    


pygame.quit()   
