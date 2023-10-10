import random
import time
import pygame

# Velocidad
serp_veloc = 15

# Tamaño Ventana
window_x = 600
window_y = 400

# Colores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Inicializamos el juego
pygame.init()

# Ventana del juego
pygame.display.set_caption("La serpiente de toda la vida")
ventana_juego = pygame.display.set_mode([window_x, window_y])

# FPS
fps = pygame.time.Clock()

# ubico a la serpiente
serp_pos = [100, 50]

# cuerpo serpiente
serp_cuerpo = [[100, 50],
               [90, 50],
               [80, 50],
               [70, 50]
               ]

# fruta
fruta_pos = [random.randrange(1, (window_x//10)) * 10,
             random.randrange(1, (window_y//10)) * 10]

fruta_spawn = True

# direccion serpiente
direccion = 'RIGHT'
cambia_dir = direccion

# score incial
score = 0


def muestra_score(opcion, color, fuente, tamano):

    score_font = pygame.font.SysFont(fuente, tamano)

    score_superficie = score_font.render('Puntaje: ' + str(score), True, color)

    score_rectan = score_superficie.get_rect()

    ventana_juego.blit(score_superficie, score_rectan)


def game_over():

    score_font = pygame.font.SysFont('Serif', 30)

    game_over_superficie = score_font.render(
        "Tu puntaje fue: " + str(score), True, red)

    game_over_rectan = game_over_superficie.get_rect()

    game_over_rectan.midtop = (window_x/2, window_y/4)

    ventana_juego.blit(game_over_superficie, game_over_rectan)
    pygame.display.flip()

    time.sleep(3)

    pygame.quit()

    quit()


while True:

    # recibir eventos del teclaado
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                cambia_dir = 'UP'
            if event.key == pygame.K_DOWN:
                cambia_dir = 'DOWN'
            if event.key == pygame.K_LEFT:
                cambia_dir = 'LEFT'
            if event.key == pygame.K_RIGHT:
                cambia_dir = 'RIGHT'

    # para que no pueda retroceder
    if cambia_dir == 'UP' and direccion != 'DOWN':
        direccion = 'UP'
    if cambia_dir == 'DOWN' and direccion != 'UP':
        direccion = 'DOWN'
    if cambia_dir == 'LEFT' and direccion != 'RIGHT':
        direccion = 'LEFT'
    if cambia_dir == 'RIGHT' and direccion != 'LEFT':
        direccion = 'RIGHT'

    # controlar la serpiente
    if direccion == 'UP':
        serp_pos[1] -= 10
    if direccion == 'DOWN':
        serp_pos[1] += 10
    if direccion == 'LEFT':
        serp_pos[0] -= 10
    if direccion == 'RIGHT':
        serp_pos[0] += 10

    # Mecanismo de crecimiento de la serpiente
    serp_cuerpo.insert(0, list(serp_pos))

    if serp_pos[0] == fruta_pos[0] and serp_pos[1] == fruta_pos[1]:
        score += 10
        fruta_spawn = False
    else:
        serp_cuerpo.pop()

    if not fruta_spawn:
        fruta_pos = [random.randrange(1, (window_x//10)) * 10,
                     random.randrange(1, (window_y//10)) * 10]

    fruta_spawn = True

    # Construir el juego en la pantalla

    ventana_juego.fill(black)

    # crear el cuerpo de la serpiente
    for pos in serp_cuerpo:
        pygame.draw.rect(ventana_juego, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))

    # crear la fruta
    pygame.draw.rect(ventana_juego, white,
                     pygame.Rect(fruta_pos[0], fruta_pos[1], 10, 10))

    # Condiciones para el fin del juego

    if serp_pos[0] < 0 or serp_pos[0] > window_x-10:
        game_over()
    if serp_pos[1] < 0 or serp_pos[1] > window_y-10:
        game_over()

    for bloque in serp_cuerpo[1:]:
        if serp_pos[0] == bloque[0] and serp_pos[1] == bloque[1]:
            game_over()

    # Mostra el score todo el tiempo
    muestra_score(1, white, 'Serif', 20)

    # refresh game screen
    pygame.display.update()

    # FPS
    fps.tick(serp_veloc)
