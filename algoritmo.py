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

import math

import math

def Angulo3Puntos(centro_x, centro_y, punto_inicio_angulo_x, punto_inicio_angulo_y, punto2_x, punto2_y):
    """
    Esta función encuentra el ángulo entre 3 puntos: el central, punto 1 y punto 2
    Argumentos:
        centro_x (any) => x del centro_x

        centro_y (any) => y del centro_y

        punto_inicio_angulo_x (any) => x del punto de inicio del ángulo

        punto_inicio_angulo_y (any) => y del punto de inicio del ángulo

        punto2_x (any) => x del punto2_x

        punto2_y (any) => y del punto2_y
    Devuelve:
        float: Ángulo entre los 3 puntos en grados, dentro del rango de 0 a 365 grados
    """
    # Calcula los vectores desde el centro al punto
    vector1 = [punto_inicio_angulo_x - centro_x, punto_inicio_angulo_y - centro_y]
    vector2 = [punto2_x - centro_x, punto2_y - centro_y]
    
    # https://stackoverflow.com/a/21484228

    # Calcula el ángulo utilizando la función atan2 y lo convierte a grados
    angulo_rad = math.atan2(vector2[1], vector2[0]) - math.atan2(vector1[1], vector1[0])
    angulo_deg = math.degrees(angulo_rad)
    
    # Asegura que el ángulo esté dentro del rango de 0 a 365 grados
    if angulo_deg < 0:
        angulo_deg = angulo_deg + 365
    
    return angulo_deg



#Funcion del algoritmo
def AlgoritmoDelPuntoMedio(centro_x, centro_y, radio, punto_inicio_angulo_x, punto_inicio_angulo_y, angulo_final):
    radio = int(radio)

    x = 0
    y = radio
    p = 5/4 - radio

    while y >= x:

        #Primer octante:

        if Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_y+y, centro_ventana_x+x) <= angulo_final and Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_y+y, centro_ventana_x+x) >= 0:
            pygame.draw.rect(screen, ROJO, pygame.Rect(centro_ventana_y+y, centro_ventana_x+x, 1, 1), 1)

            

        #Copiamos el resultado en los 7 octantes restantes como indica esta imagen: https://www.includehelp.com/computer-graphics/Images/Bresenhams-Circle-Drawing-Algorithm.jpg
        #Segundo octante:
        if Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_x+x, centro_ventana_y+y) <= angulo_final and Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_x+x, centro_ventana_y+y) >= 0:
            pygame.draw.rect(screen, VERDE, pygame.Rect(centro_ventana_x+x, centro_ventana_y+y, 1, 1), 1)

        #Tercero octante:
        if Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_x+x, centro_ventana_y-y) <= angulo_final and Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_x+x, centro_ventana_y-y) >= 0:
            pygame.draw.rect(screen, NARANJA, pygame.Rect(centro_ventana_x+x, centro_ventana_y-y, 1, 1), 1)

        #Cuarto octante:
        if Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_y+y, centro_ventana_x-x) <= angulo_final and Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_y+y, centro_ventana_x-x) >= 0:
            pygame.draw.rect(screen, ROSA, pygame.Rect(centro_ventana_y+y, centro_ventana_x-x, 1, 1), 1)

        #Quinto octante:
        if Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_y-y, centro_ventana_x-x) <= angulo_final and Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_y-y, centro_ventana_x-x) >= 0:
            pygame.draw.rect(screen, CYAN, pygame.Rect(centro_ventana_y-y, centro_ventana_x-x, 1, 1), 1)

        #Sexto octante:
        if Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_x-x, centro_ventana_y-y) <= angulo_final and Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_x-x, centro_ventana_y-y) >= 0:
            pygame.draw.rect(screen, MORADO, pygame.Rect(centro_ventana_x-x, centro_ventana_y-y, 1, 1), 1)

        #Septimo octante:
        if Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_x-x, centro_ventana_y+y) <= angulo_final and Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_x-x, centro_ventana_y+y) >= 0:
            pygame.draw.rect(screen, AMARILLO, pygame.Rect(centro_ventana_x-x, centro_ventana_y+y, 1, 1), 1)

        #Octavo octante:
        if Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_y-y, centro_ventana_x+x) <= angulo_final and Angulo3Puntos(centro_ventana_x, centro_ventana_y, punto_inicio_angulo_x, punto_inicio_angulo_y, centro_ventana_y-y, centro_ventana_x+x) >= 0:
            pygame.draw.rect(screen, MARON_PERU, pygame.Rect(centro_ventana_y-y, centro_ventana_x+x, 1, 1), 1)

        pygame.time.wait(100)
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
    
    #Ejecutamos el algo
    AlgoritmoDelPuntoMedio(centro_x, centro_y, radio/2, centro_ventana_x, centro_ventana_y-radio, 180)


    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(fps)
