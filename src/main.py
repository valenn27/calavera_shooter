from modulos import *

def guardar_puntuaciones(puntuacion: int) -> None:
    """
    guarda el puntaje del jugador en un archivo CSV, manteniendo solo los 5 puntajes más altos.

    Args:
        puntuacion (int): el puntaje del jugador.

    Returns:
        None
    """
    file_exists = os.path.isfile("ranking_puntuaciones.csv")
    puntajes = []

    if file_exists:
        puntajes = cargar_puntuaciones()

    if len(puntajes) < 5:
        puntajes.append(puntuacion)
    else:
        puntuaciones_altas = int(puntajes[0])
        if puntuacion > puntuaciones_altas:
            puntajes.insert(0, puntuacion)
            puntajes = puntajes[:5]


    with open("ranking_puntuaciones.csv", "w") as archivo:
        archivo.write("puntaje\n")
        for i in puntajes:
            archivo.write(f'{i}\n')


def cargar_puntuaciones() -> list:
    """
    carga los puntajes desde un archivo CSV y devuelve los 5 puntajes más altos.

    Returns:
        list: retorna una lista con los puntajes.
    """
    puntajes = []
    if os.path.isfile('ranking_puntuaciones.csv'):
        with open('ranking_puntuaciones.csv', 'r') as archivo: 
            lineas = archivo.readlines()
            for linea in lineas[1:]:
                puntajes.append(linea.strip())


                
    return ordenar_puntaje(puntajes)


scores = cargar_puntuaciones()


# ---------------------------------- PUNTAJE ------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# --------------------------------- COLISIONES -----------------------------------------------------------------------------------
poder_dios = False
poder_tiro = False
tiempo_poder_inicio = 0 


def colisiones() -> None:
    """Manejar las colisiones entre el jugador, las balas, los enemigos, los poderes. y maneja el puntaje"""
    global puntuacion, game_over, puntuacion_maxima, poder_dios, poder_tiro, tiempo_poder_inicio
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
                poder_dios = True
                tiempo_poder_inicio = pygame.time.get_ticks()
                poderes_copia.append(poder)
            



            elif poder['tipo'] == 'tiro':
                jugador['cadencia'] = 20
                poder_tiro = True
                tiempo_poder_inicio = pygame.time.get_ticks()
                poderes_copia.append(poder)



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

    if poder_dios:
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_poder_inicio <= 10000:
            mostrar_texto(SCREEN, sans_serif, 'invencibilidad activada', WHITE, 20,670,550)
        else:
            poder_dios = False
            jugador['invencible'] = False
    
    if poder_tiro:
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_poder_inicio <= 10000:
            mostrar_texto(SCREEN, sans_serif, 'disparo rapido activado', WHITE, 20,670,580)
        else:
            poder_tiro = False
            jugador['cadencia'] = 150



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
                guardar_puntuaciones(puntuacion)


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if  game_over:
                        musica_fondo.play(-1)
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
                        musica_fondo.play(-1)
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




                    
    except pygame.error as e:
        print(f"error al procesar eventos")

    

    if menu_inicio:

        pygame.mixer.music.stop()
        pygame.mixer.stop()
        guardar_puntuaciones(puntuacion)





        SCREEN.fill(GREEN_OSCURO)
        mostrar_texto(SCREEN, sans_serif, "CALAVERA SHOOTER", WHITE, 40, 400, 100)
        
    
        imagen_start = pygame.transform.scale(imagenes['start'], (300,150))
        imagen_salir = pygame.transform.scale(imagenes['salir'], (400,200))
        boton_start = dibujar_boton_imagen(SCREEN, 255,200, imagen_start)
        boton_salir = dibujar_boton_imagen(SCREEN, 200,350, imagen_salir)

        if scores: 
            mostrar_texto(SCREEN, sans_serif, 'ranking de puntuaciones', WHITE, 15, 700,420)
            y = 450
            posicion = 1
            for i in scores:
                mostrar_texto(SCREEN, sans_serif, f"{posicion}. {i}", WHITE, 15, 700, y)
                y += 30
                posicion += 1
               

    
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
            guardar_puntuaciones(puntuacion)



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


