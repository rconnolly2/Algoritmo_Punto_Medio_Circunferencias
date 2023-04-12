import pygame
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER_POINT = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
STARTING_POINT_COLOR = (255, 0, 0)
MOVING_POINT_COLOR = (0, 0, 255)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Angle Calculation')
clock = pygame.time.Clock()

# Initial point positions
starting_point = (CENTER_POINT[0] - 100, CENTER_POINT[1])
moving_point = list(starting_point)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Update moving point position based on mouse movement
    mouse_x, mouse_y = pygame.mouse.get_pos()
    moving_point[0] = mouse_x
    moving_point[1] = mouse_y

    # Clear screen
    screen.fill((255, 255, 255))

    # Draw center point
    pygame.draw.circle(screen, (0, 0, 0), CENTER_POINT, 5)

    # Draw starting point
    pygame.draw.circle(screen, STARTING_POINT_COLOR, starting_point, 5)

    # Draw moving point
    pygame.draw.circle(screen, MOVING_POINT_COLOR, moving_point, 5)

    # Calculate angle between the three points
    dx1 = starting_point[0] - CENTER_POINT[0]
    dy1 = starting_point[1] - CENTER_POINT[1]
    dx2 = moving_point[0] - CENTER_POINT[0]
    dy2 = moving_point[1] - CENTER_POINT[1]
    angle1 = math.degrees(math.atan2(dy1, dx1))
    angle2 = math.degrees(math.atan2(dy2, dx2))
    angle = angle2 - angle1
    if angle < 0:
        angle = angle + 365

    # Draw angle text
    font = pygame.font.SysFont(None, 36)
    angle_text = font.render(f'Angle: {angle:.2f}', True, (0, 0, 0))
    screen.blit(angle_text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)
