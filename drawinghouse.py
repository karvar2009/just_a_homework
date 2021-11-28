import pygame
from pygame.draw import *
from random import randint

colors = {
    'yellow': (255, 224, 18),
    'red': (255, 18, 18),
    'roof tiles 1': (255, 18, 18),
    'roof tiles 2': (255, 6, 18),
    'roof tiles 3': (255, 6, 6),
    'roof tiles 4': (255, 18, 6),
    'roof tiles 5': (220, 18, 18),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'baby-blue': (141, 241, 255),
    'green': (57, 191, 62),
}
pygame.init()

SCREEN = (400, 400)
SCREEN_COLOR = colors['baby-blue']
SCREEN1 = SCREEN[0]
SCREEN2 = SCREEN[1]
FPS = 30
screen = pygame.display.set_mode(SCREEN)
N = 10


def roof_tiles(x, y):
    x5 = x + 5
    y3 = y + 3
    rect(screen, roof_tiles[f'roof tiles {randint(1, 5)}'], [x, y, x5, y3])



rect(screen, SCREEN_COLOR, [0, 0, SCREEN1, SCREEN2])
rect(screen, colors['green'], [0, 250, SCREEN1, 400])
rect(screen, colors['yellow'], [140, 150, 130, 140])
polygon(screen, colors['red'], [[130, 150], [205, 100], [280, 150]])
rect(screen, colors['white'], [190, 180, 30, 50])
circle(screen, colors['white'], (70, 50), 20)
circle(screen, colors['white'], (90, 50), 20)
circle(screen, colors['white'], (100, 75), 20)
circle(screen, colors['white'], (125, 95), 20)
circle(screen, colors['white'], (145, 115), 20)
pygame.display.update()
finished = False
clock = pygame.time.Clock()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
