#IMPORTACIONES
import pygame
from pygame import mixer

# Esto es para poder reiniciar el programa
import os
import sys

from Personaje import Personaje # Clase del jugador
from moviepy.editor import VideoFileClip # Voy a usar esta librería para poder reproducir la intro del principio



def play_intro_video(video_path, screen):
    # Cargar y reproducir el video
    clip = VideoFileClip(video_path)
    clip.preview(fullscreen=False)

# Código principal
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Ruta del video
video_path = "assets/video/intro.mp4"

# Reproducir el video
play_intro_video(video_path, screen)

# Iniciar el juego después de que termine el video
pygame.quit()

        

mixer.init()
pygame.mixer.init()

pygame.init()

# Cargar el sonido corto (diálogo o sonido de inicio)
inicio_sound = pygame.mixer.Sound("assets/audio/audio-inicio.mp3")  # Ruta de tu archivo de sonido corto

# Reproducir el diálogo inicial
inicio_sound.play()

# Cargar la música de fondo
pygame.mixer.music.load("assets/audio/musica-fondo.mp3")  # Ruta de tu archivo de música


# Reproducir la música en bucle (-1 significa bucle infinito)
pygame.mixer.music.play(-1)


# Creo la ventana principal
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mortal Elecciones")

# Set framerate
clock = pygame.time.Clock()
FPS = 60

# IMAGENES
bg_image = pygame.image.load("assets/images/background/obelisco2.jpg").convert_alpha()
milei_normal = "assets/images/milei/milei-normal.png"
milei_ataque = "assets/images/milei/milei-ataque.png"
massa_normal = "assets/images/massa/massa-normal.png"
massa_ataque = "assets/images/massa/massa-ataque.png"

# Game Over imagen
game_over_milei = pygame.image.load("assets/images/milei/milei-win.png").convert_alpha()  # Ruta de la imagen
game_over_massa = pygame.image.load("assets/images/massa/massa-win.png").convert_alpha()  # Ruta de la imagen


# SONIDOS
motosierra_fx = pygame.mixer.Sound("assets/audio/motosierra.mp3")
motosierra_fx.set_volume(0.5)
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(2)

# Cargar el sonido de Game Over
game_over_sound = pygame.mixer.Sound("assets/audio/gameover.mp3")  # Ruta de tu archivo de sonido


# Dibujo el background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

# Creo a massa y milei
jugadorMilei = Personaje(1, 200, 310, False, milei_normal, milei_ataque, motosierra_fx)
jugadorMassa = Personaje(2, 700, 310, True, massa_normal, massa_ataque, magic_fx)


# Barra de vida
def draw_health_bar(health, Personaje_rect):
    ratio = health / 100
    bar_width = 100  # Ajusta el ancho de la barra
    bar_height = 10  # Ajusta el alto de la barra
    x = Personaje_rect.centerx - bar_width // 2  # Centrar la barra sobre el personaje
    y = Personaje_rect.top - 20  # Colocar un poco encima del personaje
    
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, bar_width + 4, bar_height + 4))  # Bordes blancos
    pygame.draw.rect(screen, RED, (x, y, bar_width, bar_height))  # Fondo rojo
    pygame.draw.rect(screen, YELLOW, (x, y, bar_width * ratio, bar_height))  # Proporción amarilla




# BUCLE QUE MANTIENE CORRIENDO EL JUEGO!
run = True
while run:
    clock.tick(FPS)

    # Draw background
    draw_bg()

    # Move and update Personajes
    jugadorMilei.move(SCREEN_WIDTH, SCREEN_HEIGHT, jugadorMassa, False)
    jugadorMassa.move(SCREEN_WIDTH, SCREEN_HEIGHT, jugadorMilei, False)
    jugadorMilei.update()
    jugadorMassa.update()

    # Draw Personajes
    jugadorMilei.draw(screen)
    jugadorMassa.draw(screen)

    # Dibujar barras de vida sobre cada luchador
    draw_health_bar(jugadorMilei.health, jugadorMilei.rect)
    draw_health_bar(jugadorMassa.health, jugadorMassa.rect)


     # Comprobar si alguno de los jugadores murió
    if jugadorMilei.health <= 0:
        jugadorMilei.alive = False
        jugadorMassa.alive = False  # Detener ambos jugadores
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over, Massa gana", True, (98, 202, 252))  # Texto rojo para "Game Over"
        screen.blit(text, (100, 50))  # Mostrar el texto en el centro de la pantalla
        screen.blit(game_over_massa, (300, 200)) # Imagen gana massa
        game_over_sound.play()  # Reproducir el sonido de Game Over
        game_over_sound.stop()

    if jugadorMassa.health <= 0:
        jugadorMilei.alive = False
        jugadorMassa.alive = False  # Detener ambos jugadores
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over, Milei gana", True, (98, 202, 252))  # Texto rojo para "Game Over"
        screen.blit(text, (100, 50))  # Mostrar el texto en el centro de la pantalla
        screen.blit(game_over_milei, (300, 200)) # Imagen gana milei
        game_over_sound.play()  # Reproducir el sonido de Game Over
        game_over_sound.stop()


     # Detectar presion de la tecla ENTER para reiniciar el juego
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
         # Usamos os.execv() para reiniciar el programa
        os.execv(sys.executable, ['python'] + sys.argv)


    # Con esto vamos a cerrarlo de la X al detectar un evento de tipo QUIT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
