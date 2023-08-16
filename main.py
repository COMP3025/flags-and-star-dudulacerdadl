import math
import sys

import pygame
from pygame.locals import QUIT


# Função para calcular as coordenadas dos pontos da estrela
def draw_star(screen, position, size, angle, color="white"):
    inner_size = size / 2.5
    angle += 55
    points = []
    for i in range(5 * 2):
        radius = size if i % 2 == 0 else inner_size
        x = position[0] + radius * math.cos(math.radians(i * 360 / (5 * 2) + angle))
        y = position[1] + radius * math.sin(math.radians(i * 360 / (5 * 2) + angle))
        points.append((x, y))
    return pygame.draw.polygon(screen, color, points)


pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bandeira do Brasil')

while True:
    pygame.draw.rect(screen, (000, 156, 59), pygame.Rect(0, 25, 250, 150))
    pygame.draw.polygon(screen, (255, 223, 000), [(125, 35), (240, 100),
                                                  (125, 165), (10, 100)])
    pygame.draw.circle(screen, (000, 39, 118), (125, 100), 45)
    pygame.draw.arc(screen, (255, 255, 255), (0, 85, 300, 300), 1.4, 2.1, 15)
    pygame.draw.ellipse(screen, (255, 223, 000), [73, 48, 105, 105], 10)

    position = (width // 2, height // 2)
    size = 50
    angle = 0
    star = draw_star(screen, position, size, angle)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
