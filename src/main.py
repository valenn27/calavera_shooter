from modulos import *



def cargar_puntuacion_maxima() -> None: 
    """
    Carga la puntuación máxima desde un archivo JSON y la almacena en la variable global 'puntuacion_maxima'.
    Si el archivo no existe, inicializa 'puntuacion_maxima' en 0

    """
    global puntuacion_maxima
    ruta_archivo = 'puntuacion_maxima.json'
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r') as archivo:
            data = json.load(archivo)
            puntuacion_maxima = data['puntuacion_maxima']
    else:
        puntuacion_maxima = 0

def guardar_puntuacion_maxima() -> None:
    """Guarda la puntuación máxima en un archivo JSON desde la variable global 'puntuacion_maxima'. """
    global puntuacion_maxima
    ruta_archivo = 'puntuacion_maxima.json'
    with open(ruta_archivo, 'w') as archivo:
        json.dump({'puntuacion_maxima': puntuacion_maxima}, archivo)

cargar_puntuacion_maxima()




# ---------------------------------- PUNTAJE ------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# --------------------------------- COLISIONES -----------------------------------------------------------------------------------


def colisiones() -> None:
    """Manejar las colisiones entre el jugador, las balas, los enemigos, los poderes. y maneja el puntaje"""
    global puntuacion, game_over, puntuacion_maxima
    balas_copia = []
    enemigos_copia = []
    poderes_copia = []

    for enemigo in enemigos:
        if detectar_colision_circulo(jugador['rect'], enemigo['rect']) and not jugador['invencible']:
            jugador['vida'] -= 1
            enemigo['vida'] -= 10
            minecraf_sonido.play()

            if jugador['vida'] <= 0 and jugador['cantidad_vidas'] == 3:

                    jugador['vida'] = 100
                    jugador['rect'].center = (400, 500)
                    jugador['cantidad_vidas'] -= 1


            if jugador['cantidad_vidas'] == 2:
                if jugador['vida'] <= 0:

                    jugador['vida'] = 100
                    jugador['rect'].center = (400, 500)
                    jugador['cantidad_vidas'] -= 1

            if jugador['cantidad_vidas'] == 1:
                if jugador['vida'] <= 0:

                    jugador['vida'] = 100
                    jugador['rect'].center = (400, 500)
                    jugador['cantidad_vidas'] -= 1

            if jugador['cantidad_vidas'] == 0:
                game_over = True


            if enemigo['vida'] <= 0:
                    enemigos_copia.append(enemigo)



    for bala in balas:
        for enemigo in enemigos:
            if detectar_colision_circulo(bala['rect'], enemigo['rect']):
                enemigo['vida'] -= 40
                puntuacion += 100
                impacto.play()
                if enemigo['vida'] <= 0:
                    enemigos_copia.append(enemigo)
                if bala not in balas_copia:
                    balas_copia.append(bala)



    for poder in poderes:
        if detectar_colision_circulo(jugador['rect'], poder['rect']):
            if poder['tipo'] == 'dios':
                jugador['invencible'] = True
                poderes_copia.append(poder)
                pygame.time.set_timer(pygame.USEREVENT + 1, 10000)



            elif poder['tipo'] == 'tiro':
                jugador['cadencia'] = 20
                poderes_copia.append(poder)
                pygame.time.set_timer(pygame.USEREVENT + 2, 10000)


            if poder not in poderes_copia:
                poderes_copia.append(poder)


    for bala in balas_copia:
        if bala in balas:
            balas.remove(bala)

    for enemigo in enemigos_copia:
        if enemigo in enemigos:
            enemigos.remove(enemigo)

    for poder in poderes_copia:
        if poder in poderes:
            poderes.remove(poder)


    if puntuacion > puntuacion_maxima:
        puntuacion_maxima = puntuacion
    

# --------------------------------- COLISIONES -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
# --------------------------------- FLUJO DEL PROGRAMA -----------------------------------------------------------------------------------


clock = pygame.time.Clock()

ejecucion = True
game_over = False
menu_inicio = True
muteado = False


pygame.time.set_timer(pygame.USEREVENT + 3, 40000)



while ejecucion:
    clock.tick(FPS)


    try:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecucion = False
                guardar_puntuacion_maxima()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if  game_over:
                        pygame.mixer.music.play(-1)
                        jugador['vida'] = 100
                        jugador['cantidad_vidas'] = 3
                        jugador['rect'].center = (400, 500)
                        puntuacion = 0
                        game_over = False
                        menu_inicio= False
                        pygame.time.set_timer(pygame.USEREVENT + 3, 40000)



                if not menu_inicio and not game_over:
                    if event.key == pygame.K_p:
                        pausa_juego(pygame.K_p)
                        

                if event.key == pygame.K_ESCAPE:
                    if menu_inicio:
                        ejecucion = False
                    else:
                        menu_inicio = True
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_inicio: 
                    if boton_start.collidepoint(event.pos):
                        pygame.mixer.music.play(-1)
                        jugador['vida'] = 100
                        jugador['cantidad_vidas'] = 3
                        jugador['rect'].center = (400, 500)
                        puntuacion = 0 
                        game_over = False
                        menu_inicio= False
                        pygame.time.set_timer(pygame.USEREVENT + 3, 40000)
            
                    elif boton_salir.collidepoint(event.pos): 
                        ejecucion = False
                


            if event.type == pygame.USEREVENT + 3:

                poder_random = randrange(0, 2)
                if poder_random == 0:
                    poder = crear_poder_dios()
                elif poder_random == 1:
                    poder = crear_poder_tiro()

                poderes.append(poder)

            if event.type == pygame.USEREVENT + 1:
                jugador['invencible'] = False


            elif event.type == pygame.USEREVENT + 2:
                jugador['cadencia'] = 150
    except pygame.error as e:
        print(f"error al procesar eventos")

    

    if menu_inicio:
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        guardar_puntuacion_maxima()



        SCREEN.fill(GREEN_OSCURO)
        mostrar_texto(SCREEN, sans_serif, "CALAVERA SHOOTER", WHITE, 40, 400, 100)
        
    
        imagen_start = pygame.transform.scale(pygame.image.load('src/imagenes/start.png'), (300,150))
        imagen_salir = pygame.transform.scale(pygame.image.load('src/imagenes/salir.png'), (400,200))
        boton_start = dibujar_boton_imagen(SCREEN, 255,200, imagen_start)
        boton_salir = dibujar_boton_imagen(SCREEN, 200,350, imagen_salir)

   

    
    if not menu_inicio:
        try:

            SCREEN.blit(fondo, (0, 0))

            teclas = pygame.key.get_pressed()

            # audio
            if teclas[pygame.K_9] and pygame.mixer_music.get_volume() >= 0.0:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
                muteado = False
                SCREEN.blit(subir_volumen, (740, 550))

        

            if teclas[pygame.K_0] and pygame.mixer_music.get_volume() <= 1.0:
                pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
                muteado = False
                SCREEN.blit(bajar_volumen, (740, 550))

            

            elif teclas[pygame.K_m]:
                pygame.mixer.music.set_volume(0.0)
                muteado = True
                SCREEN.blit(mute_volumen, (740, 550))

                

            elif teclas[pygame.K_n]:
                pygame.mixer.music.set_volume(1.0)
                muteado = False
                SCREEN.blit(maximo_volumen, (740, 550))

            if muteado: 
                SCREEN.blit(mute_volumen, (740, 550))

            if not enemigos:
                for _ in range(randrange(0, 10)):
                    crear_enemigo()


        
            actualizar_jugador()
            actualizar_enemigos()
            actualizar_balas()
            colisiones()

            for enemigo in enemigos:
                SCREEN.blit(enemigo['image'], enemigo['rect'])


            for bala in balas:
                SCREEN.blit(bala['image'], bala['rect'])

            for poder in poderes:
                SCREEN.blit(poder['image'], poder['rect'])


            SCREEN.blit(jugador['image'], jugador['rect'])


            mostrar_texto(SCREEN, sans_serif, f'Score: {puntuacion}', WHITE, 30, 150, 570)
            mostrar_texto(SCREEN, sans_serif, f'High Score: {puntuacion_maxima}', WHITE, 20, 700, 20)
            mostrar_texto(SCREEN, sans_serif, f'vidas: {jugador["cantidad_vidas"]}', WHITE, 30, 400, 20)

            barra_vida(SCREEN, 5, 5, jugador['vida'])

        except AttributeError as e:
            print(f"error al acceder a atributos")
            
        except TypeError as e:
            print(f"error de tipo")

        except ValueError as e:
            print(f"error de valor")

        except pygame.error as e:
            print(f"error de Pygame")



        if game_over:
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            guardar_puntuacion_maxima()

            for enemigo in enemigos[:]:
                enemigos.remove(enemigo)

            for poder in poderes[:]:
                poderes.remove(poder)



            SCREEN.fill(RED)
            mostrar_texto(SCREEN, sans_serif, "GAME OVER", WHITE, 40, 400, 250)
            mostrar_texto(SCREEN, sans_serif, f'Score: {puntuacion}', WHITE, 40, 400, 300)
            mostrar_texto(SCREEN, sans_serif, f'High Score: {puntuacion_maxima}', WHITE, 40, 400, 350)
            mostrar_texto(SCREEN, sans_serif, "Presiona R para reiniciar", WHITE, 40, 400, 450)
            mostrar_texto(SCREEN, sans_serif, "Presiona ESCAPE para volver al menu", WHITE, 35, 400, 500)



  

    pygame.display.flip()

pygame.quit()


