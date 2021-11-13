import pygame
from pygame.draw import *


pygame.init()

SCREEN = (400, 400)
SCREEN_COLOR = "white"

SCREEN1 = SCREEN[0]
SCREEN2 = SCREEN[1]
FPS = 30
screen = pygame.display.set_mode(SCREEN)

N = 10
color = (255, 255, 255)
rect(screen, SCREEN_COLOR, [0, 0, SCREEN1, SCREEN2])


class my_face:
    def skin(self):
        circle(screen, color="yellow", radius=150, center=[200, 200])

    def eyes(self):
        circle(screen, color="red", radius=30, center=[140, 150])
        circle(screen, color="black", radius=15, center=[140, 150])
        circle(screen, color="red", radius=25, center=[260, 150])
        circle(screen, color="black", radius=10, center=[260, 150])

    def brows(self):
        line(screen, "black", [90, 60], [190, 140], 10)
        line(screen, "black", [200, 140], [300, 90], 10)

    def mouth(self):
        ellipse(screen, "black", [110, 200, 180, 120])
        ellipse(screen, "yellow", [110, 220, 180, 120])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    f = my_face()
    f.skin()
    f.eyes()
    f.brows()
    f.mouth()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
