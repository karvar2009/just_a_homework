import sys
import pygame as pg
import random as r

import pygame.key
from pygame.draw import circle, rect

pygame.init()




def setup() -> object:
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)  # окошко открывается на весь экран
    clock = pg.time.Clock()
    return screen, clock


def main(surface: object, updater: object) -> None:
    trangle_is_here = False
    done = False
    trangle_cord = 0
    while not done:
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        # print(Mouse_x, " ", Mouse_y)
        surface.fill(pg.Color('white'))
        for event in pg.event.get():
            is_rect = False
            if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                done = True
                sys.exit()
                # правильное ЗАКРЫТИЕ окна программы 70
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos_x, pos_y = pygame.mouse.get_pos()
                # pos_y = Mouse_y
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos_x1, pos_y1 = pygame.mouse.get_pos()
                rect(surface, pg.Color('Black'), (pos_x, pos_y, pos_x1 - pos_x, pos_y1 - pos_y))
                print(
                    f'rect(surface, pg.Color(), (surface.get_width() * {pos_x / surface.get_width()}, surface.get_height() * {pos_y / surface.get_height()}, surface.get_width() * {(pos_x1 - pos_x) / surface.get_width()}, surface.get_height() * {(pos_y1 - pos_y) / surface.get_height()}))')
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3 and trangle_cord == 0:
                pos_x_tr, pos_y_tr = pygame.mouse.get_pos()
                trangle_cord = 1
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3 and trangle_cord == 1:
                pos_x_tr_1, pos_y_tr_1 = pygame.mouse.get_pos()
                trangle_cord = 2
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3 and trangle_cord == 2:
                pos_x_tr_2, pos_y_tr_2 = pygame.mouse.get_pos()
                trangle_cord = 0
                pg.draw.polygon(surface, pg.Color('black'),
                                [(pos_x_tr, pos_y_tr), (pos_x_tr_1, pos_y_tr_1), (pos_x_tr_2, pos_y_tr_2)])
                print(f'pg.draw.polygon(surface, pg.Color()',end="")
                print(f', [(surface.get_width() * {pos_x_tr / surface.get_width()}',end="")
                print(f', surface.get_height() * {pos_y_tr / surface.get_height()})', end="")
                print(f', (surface.get_width() * {pos_x_tr_1 / surface.get_width()}',end="")
                print(f', surface.get_height() * {pos_y_tr_1 / surface.get_height()})', end="")
                print(f', (surface.get_width() * {pos_x_tr_2 / surface.get_width()}', end="")
                print(f', surface.get_height() * {pos_y_tr_2 / surface.get_height()})])')





        pg.display.flip()  # обновление экрана
        updater.tick(60)  # FPS игры


screen, clock = setup()
main(screen, clock)
