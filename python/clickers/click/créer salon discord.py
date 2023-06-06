from pynput.mouse import Controller, Button
import time
import pyautogui
mouse = Controller()

nom = [
    "jeuxvideo",
    "p-nintendo",
    "gameblog",
    "factornews",
    "jeuxonline",
    "hdnumerique",
    "allocine",
    "avcesar",
    "premiere",
    "ecranlarge",
    "journaldujapon"
]


def press():
    mouse.press(Button.left)
    mouse.release(Button.left)

for i in nom:
    time.sleep(1)
    mouse.position = (2206, 530)
    pyautogui.scroll(2000)
    time.sleep(1)
    press()
    time.sleep(0.5)
    for j in i:
        pyautogui.press(j)
    
    time.sleep(0.1)
    pyautogui.press('enter')