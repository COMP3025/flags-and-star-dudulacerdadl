import math
import sys

import pygame
from pygame.locals import QUIT


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
pygame.display.set_caption('Bandeira de Comores')

while True:
    pygame.draw.rect(screen, "yellow", pygame.Rect(0, 0, 400, 50))
    pygame.draw.rect(screen, "white", pygame.Rect(0, 50, 400, 50))
    pygame.draw.rect(screen, "red", pygame.Rect(0, 100, 400, 50))
    pygame.draw.rect(screen, "blue", pygame.Rect(0, 150, 400, 50))
    pygame.draw.polygon(screen, "green", [(0, 0), (200, 100), (0, 200)])
    pygame.draw.circle(screen, "white", (65, 100), 55)
    pygame.draw.circle(screen, "green", (80, 100), 50)

    angle = 0
    star = draw_star(screen, (77, 60), 10, angle)
    star = draw_star(screen, (77, 85), 10, angle)
    star = draw_star(screen, (77, 110), 10, angle)
    star = draw_star(screen, (77, 135), 10, angle)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
