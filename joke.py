import os
import keyboard
import random
import pygame
from pygame.draw import *
import time
pygame.init()
#
# os.system("taskkill chrome")
# os.system("taskkill taskmgr")
# keyboard.add_hotkey("alt + f4", lambda: print('это не выход!'), suppress=True)
# keyboard.add_hotkey("alt + tab", lambda: print('не уйдёшь!'), suppress=True)
# keyboard.add_hotkey("Ctrl + Shift + Esc", lambda: print('не-а )))'), suppress=True)
# keyboard.add_hotkey("Alt +Esc", lambda: print('не так просто'), suppress=True)
# keyboard.add_hotkey("Ctrl +Esc", lambda: print('не так просто'), suppress=True)
# keyboard.add_hotkey("f1", lambda: print('Я твоя помошь'), suppress=True)
#
#
# def random_id(length):
#     number = '0123456789'
#     alpha = 'abcdefghijklmnopqrstuvwxyz'
#     idshnik = 'joke_'
#     for i in range(0, length, 2):
#         idshnik += random.choice(number)
#         idshnik += random.choice(alpha)
#     return idshnik
#
#
# def fold(col):
#     for i in range(col):
#         na = random_id(50)
#         os.mkdir("C:\Windows\System32\\"+na)
#
#
#
for i in range(3):
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
        class skin:
            circle(screen, color="yellow", radius=150, center=[200, 200])
        class eyes:
            circle(screen, color="red", radius=30, center=[140, 150])
            circle(screen, color="black", radius=15, center=[140, 150])
            circle(screen, color="red", radius=25, center=[260, 150])
            circle(screen, color="black", radius=10, center=[260, 150])
        class brows:
            line(screen, "black", [90, 60], [190, 140], 10)
            line(screen, "black", [200, 140], [300, 90], 10)
        class mouth:
            ellipse(screen, "black", [110, 200, 180, 120])
            ellipse(screen, "yellow", [110, 220, 180, 120])
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
    pygame.quit()
    time.sleep(20)
