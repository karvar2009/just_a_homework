import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


N = 10
color = (255, 255, 255)
class my_face:
    class skin:
        circle(screen,color="yellow", radius=150, center=[200,200])
    class eyes:
        circle(screen,color="red", radius=30, center=[140,150])
        circle(screen,color="black", radius=15, center=[140,150])
        circle(screen,color="red", radius=25, center=[260,150])
        circle(screen,color="black", radius=10, center=[260,150])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()