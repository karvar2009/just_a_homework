import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


N = 10
color = (255, 255, 255)
rect(screen, "white", [0,0,400,400])
class my_face:
    class skin:
        circle(screen,color="yellow", radius=150, center=[200,200])
    class eyes:
        circle(screen,color="red", radius=30, center=[140,150])
        circle(screen,color="black", radius=15, center=[140,150])
        circle(screen,color="red", radius=25, center=[260,150])
        circle(screen,color="black", radius=10, center=[260,150])
    class brows:
        line(screen, "black", [90, 60], [190, 140], 10)
        line(screen, "black", [200, 140], [300, 90], 10)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()