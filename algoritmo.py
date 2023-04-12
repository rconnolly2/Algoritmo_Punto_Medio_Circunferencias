#Este algoritmo se usa para encontrar los puntos de un circulo o angulo 
#https://en.wikipedia.org/wiki/Midpoint_circle_algorithm

import pygame
import math
import time

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ancho_ventana = 500
alto_ventana = 500
titulo_ventana = "Algoritmo del punto medio para circunferencias"
BLANCO = (255, 255, 255)
ROJO = (183, 3, 3) # Color del que estamos calculando
# Estos colores son copiados del rojo
VERDE = (124, 252, 0)
NARANJA = (255, 165, 0)
ROSA = (255, 105, 180)
CYAN = (0, 255, 255)
MORADO = (218, 112, 214)
AMARILLO = (255, 255, 0)
MARON_PERU = (205, 133, 63)

#Centro de la ventana:
centro_ventana_x = int(ancho_ventana/2)
centro_ventana_y = int(alto_ventana/2)

# Configuración del reloj para mantener 60 FPS
clock = pygame.time.Clock()
fps = 60

# Crear la ventana
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption(titulo_ventana)

#Funcion del algoritmo
def AlgoritmoDelPuntoMedio(centro_x, centro_y, radio, angulo_inicio, angulo_final):
    radio = int(radio)

    x = 0
    y = radio
    p = 5/4 - radio

    while y >= x:

        #Primer octante:
        pygame.draw.rect(screen, ROJO, pygame.Rect(centro_ventana_y+y, centro_ventana_x+x, 1, 1), 1)
        pygame.time.wait(50)
        pygame.display.flip()

        #Copiamos el resultado en los 7 octantes restantes como indica esta imagen: https://www.includehelp.com/computer-graphics/Images/Bresenhams-Circle-Drawing-Algorithm.jpg
        #Segundo octante:
        pygame.draw.rect(screen, VERDE, pygame.Rect(centro_ventana_x+x, centro_ventana_y+y, 1, 1), 1)

        #Tercero octante:
        pygame.draw.rect(screen, NARANJA, pygame.Rect(centro_ventana_x+x, centro_ventana_y-y, 1, 1), 1)

        #Cuarto octante:
        pygame.draw.rect(screen, ROSA, pygame.Rect(centro_ventana_y+y, centro_ventana_x-x, 1, 1), 1)

        #Quinto octante:
        pygame.draw.rect(screen, CYAN, pygame.Rect(centro_ventana_y-y, centro_ventana_x-x, 1, 1), 1)

        #Sexto octante:
        pygame.draw.rect(screen, MORADO, pygame.Rect(centro_ventana_x-x, centro_ventana_y-y, 1, 1), 1)

        #Septimo octante:
        pygame.draw.rect(screen, AMARILLO, pygame.Rect(centro_ventana_x-x, centro_ventana_y+y, 1, 1), 1)

        #Octavo octante:
        pygame.draw.rect(screen, MARON_PERU, pygame.Rect(centro_ventana_y-y, centro_ventana_x+x, 1, 1), 1)

        pygame.display.flip()
        x = x + 1

        if p <= 0:
            p = p + x*2 + 1
        else:
            y = y - 1
            p = p + x*2 - y*2 + 1


radio = int(ancho_ventana / 2)
centro_x = ancho_ventana // 2
centro_y = alto_ventana // 2
x = 0
y = radio
# Bucle principal del juego
while True:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Limpiar la pantalla con el color de fondo
    screen.fill(BLANCO)

    # Dibujar la circunferencia utilizando el algoritmo del punto medio
    

    AlgoritmoDelPuntoMedio(centro_x, centro_y, radio, 0, 60)


    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(fps)
