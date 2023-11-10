from pynput.mouse import Controller, Button
import time
import pyautogui
import pyperclip
mouse = Controller()

nom = [
    "📊-logiciel",
    "⚙-test",
    "📟-web",
]


def press():
    mouse.press(Button.left)
    mouse.release(Button.left)

for i in nom:
    time.sleep(0.5)
    mouse.position = (342, 453)
    pyautogui.scroll(2000)
    time.sleep(1)
    press()
    time.sleep(0.5)
    pyperclip.copy(i)