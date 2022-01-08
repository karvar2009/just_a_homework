"""
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

    class trangle:
        def __init__(self, pos_x_tr, pos_y_tr, pos_x_tr1, pos_y_tr1, pos_x_tr2, pos_y_tr2):
            self.pos_x_tr = pos_x_tr
            self.pos_y_tr = pos_y_tr
            self.pos_x_tr_1 = pos_x_tr_1
            self.pos_y_tr_1 = pos_y_tr_1
            self.pos_x_tr_2 = pos_x_tr_2
            self.pos_y_tr_2 = pos_y_tr_2

        def print_result(self, pos_x_tr, pos_y_tr, pos_x_tr1, pos_y_tr1, pos_x_tr2, pos_y_tr2):
            print(f'pg.draw.polygon(surface, pg.Color()', end="")
            print(f', [(surface.get_width() * {self.pos_x_tr / surface.get_width()}', end="")
            print(f', surface.get_height() * {self.pos_y_tr / surface.get_height()})', end="")
            print(f', (surface.get_width() * {self.pos_x_tr_1 / surface.get_width()}', end="")
            print(f', surface.get_height() * {self.pos_y_tr_1 / surface.get_height()})', end="")
            print(f', (surface.get_width() * {self.pos_x_tr_2 / surface.get_width()}', end="")
            print(f', surface.get_height() * {self.pos_y_tr_2 / surface.get_height()})])')

        def print_trangle(self):
            pg.draw.polygon(surface, pg.Color('black'),
                            [(self.pos_x_tr, self.pos_y_tr), (self.pos_x_tr_1, self.pos_y_tr_1),
                             (self.pos_x_tr_2, self.pos_y_tr_2)])

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
                trangle1 = trangle.__init__(pos_x_tr, pos_y_tr, pos_x_tr_1, pos_y_tr_1, pos_x_tr_2, pos_y_tr_2)
                trangle1.print_result()

        trangle1.print_trangle()

        pg.display.flip()  # обновление экрана
        updater.tick(60)  # FPS игры


screen, clock = setup()
main(screen, clock)

"""


import sys
import pygame as pg
import random as r
from pygame.draw import circle, rect


def setup() -> object:
    pg.init()
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)  # окошко открывается на весь экран
    clock = pg.time.Clock()
    return screen, clock


def main(surface: object, updater: object) -> None:
    done = False
    snowflakes = []
    for i in range(500):  # рисую много снежинок
        x = r.randint(0, surface.get_width())
        y = r.randint(0, surface.get_height())
        snowflakes.append((x, y))

    while not done:
        surface.fill(pg.Color('lightblue'))
        for event in pg.event.get():
            if (event.type == pg.QUIT) or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                done = True
                sys.exit()  # правильное ЗАКРЫТИЕ окна программы

        # ground
        rect(surface, pg.Color('snow'), (0, 0.75 * surface.get_height(),
                                         surface.get_width(), 0.25 * surface.get_height()))

        # snowman
        snowman_y = 0.5 * surface.get_height()
        snowman_x = 0.3 * surface.get_width()
        rect(surface, pg.Color('red'), (snowman_x - 20, snowman_y - 50, 40, 42))
        for i in range(1, 4):
            circle(surface, pg.Color('snow'), (snowman_x, snowman_y), i * 30)
            snowman_y += i * 70

        # Cristmas Tree
        # rect(surface, pg.Color('chocolate'), (surface.get_width() * 0.60625, surface.get_height() * 0.25,
        #                                       surface.get_width() * 0.61875, surface.get_height() * 0.35))
        tree_y = surface.get_height()
        tree_x = surface.get_width()
        # rect(surface, pg.Color('chocolate'), (tree_x - 700, tree_y - 200, 50, 30))
        rect(surface, pg.Color('Black'), (surface.get_width() * 0.755859375, surface.get_height() * 0.8935185185185185,
                                   surface.get_width() * 0.018229166666666668,
                                   surface.get_height() * 0.03587962962962963))
        pg.draw.polygon(surface, pg.Color('aquamarine4'),
                        [(surface.get_width() * 0.6744791666666666, surface.get_height() * 0.8784722222222222),
                         (surface.get_width() * 0.822265625, surface.get_height() * 0.8819444444444444),
                         (surface.get_width() * 0.7604166666666666, surface.get_height() * 0.7881944444444444)])
        pg.draw.polygon(surface, pg.Color('aquamarine4'),
                        [(surface.get_width() * 0.7252604166666666, surface.get_height() * 0.7986111111111112),
                         (surface.get_width() * 0.7845052083333334, surface.get_height() * 0.7951388888888888),
                         (surface.get_width() * 0.7578125, surface.get_height() * 0.7638888888888888)])
        pg.draw.polygon(surface, pg.Color('aquamarine4'),
                        [(surface.get_width() * 0.7415364583333334, surface.get_height() * 0.7627314814814815),
                         (surface.get_width() * 0.7727864583333334, surface.get_height() * 0.7673611111111112),
                         (surface.get_width() * 0.759765625, surface.get_height() * 0.7430555555555556)])




        #po papinomu
        #     tree_polygon_1_x = (surface.get_width() * 0.5) + (surface.get_width() * 0.03 * h)
        #     tree_polygon_1_y = (surface.get_height() * 0.25) + (surface.get_height() * 0.2 * h) + (
        #                 surface.get_height() * 0.1)
        #     tree_polygon_2_x = (surface.get_width() * 0.75) + (surface.get_width() * 0.03 * w)
        #     tree_polygon_2_y = (surface.get_height() * 0.25) + (surface.get_height() * 0.2 * h) + (
        #                 surface.get_height() * 0.1)
        #     tree_polygon_3_x = surface.get_width() * 0.5
        #     tree_polygon_3_y = surface.get_height() * 0.5
        #     w -= 1

        for i in range(len(snowflakes)):
            sf = snowflakes[i]
            snowflakes[i] = (sf[0] + r.randint(-1, 1), sf[1] + r.randint(1, 3))
            circle(surface, pg.Color('snow2'), (sf[0], sf[1]), r.randint(2, 6))  # размер каждой снежинки меняется
            if sf[1] > surface.get_height():  # если y снежинки больше высоты экрана
                snowflakes[i] = (sf[0], 0)  # не трогаем x и перемещаем снежинку наверх
        pg.display.flip()  # обновление экрана
        updater.tick(60)  # FPS игры


screen, clock = setup()
main(screen, clock)
