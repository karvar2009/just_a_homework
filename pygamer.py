import pygame as pg
from pygame.draw import *

pg.init()

SCREEN = (400, 400)
SCREEN_COLOR = "white"

SCREEN1 = SCREEN[0]
SCREEN2 = SCREEN[1]
FPS = 30
screen = pg.display.set_mode(SCREEN)

N = 10
color = (255, 255, 255)
rect(screen, SCREEN_COLOR, [0, 0, SCREEN1, SCREEN2])

# rect(screen, 'blue', [50, 100, 250, 200])
# circle(screen, 'gray', [125, 125], 20)
# circle(screen, 'red', [125, 125], 20, 2)

x1, y1, x2, y2 = 30, 30, 300, 200

rect(screen, 'blue', [x1, y1, x2 - x1, y2 - y1], 3)
height = (x2 - x1) // 10
step = x1 + height

for d in range(10):
    line(screen, 'cyan', [step, y1], [step, y2])
    step += height

polygon(screen, 'red', [[100,90],[200, 350],[120, 70]])

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
