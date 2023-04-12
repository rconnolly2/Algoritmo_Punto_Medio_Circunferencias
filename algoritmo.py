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

def Angulo3Puntos(centro_x, centro_y, punto_inicio_angulo_x, punto_inicio_angulo_y, punto2_x, punto2_y):
    """
    Esta funcion encuentra el angulo entre 3 puntos: el central, punto 1 y 2
    Argumentos:
        centro_x (any) => x de centro_x

        centro_y (any) => y de centro_y

        punto_inicio_angulo_x (any) => x del punto de inicio del angulo

        punto_inicio_angulo_y (any) => y del punto de inicio del angulo

        punto2_x (any) => x de punto2_x

        punto2_y (any) => y de punto2_y
    Devuelve:
        float: Angulo entre los 3 puntos en grados
    """
    # Calcula los vectores desde el centro al punto
    vector1 = [punto_inicio_angulo_x - centro_x, punto_inicio_angulo_y - centro_y]
    vector2 = [punto2_x - centro_x, punto2_y - centro_y]
    
    # Calcula el producto escalar ("es como la similitud entre los 2 vectores")
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    # Calcula la longitud de los vectores
    longitudvector1 = math.sqrt(vector1[0]**2 + vector1[1]**2)
    longitudvector2 = math.sqrt(vector2[0]**2 + vector2[1]**2)
    
    # Calcula el angulo utilizando la funcion arc cosine y lo devuelve en grados
    #https://mathsathome.com/angle-between-two-vectors/#Angle_Between_Two_Vectors_Formula
    #Formula θ = arccos((A · B) / (|A| * |B|))
    #A*B son El producto escalar ("La similitud en 2 vectores")
    #|A| * |B| son las longitudes de cada vector
    angulo = math.degrees(math.acos(dot_product / (longitudvector1 * longitudvector2)))
    
    return angulo

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
            pygame.time.wait(50)
            

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
    

    AlgoritmoDelPuntoMedio(centro_x, centro_y, radio, centro_ventana_x, centro_ventana_y-radio, 100)


    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(fps)
