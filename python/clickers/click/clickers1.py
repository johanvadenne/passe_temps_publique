from pynput.mouse import Controller, Button
import time
mouse = Controller()

def pressRight():
    mouse.press(Button.left)
    mouse.release(Button.left)

def pressLeft():
    mouse.press(Button.left)
    mouse.release(Button.left)


time.sleep(3)
for i in range(35):
    time.sleep(3)
    mouse.position = (16, 152)
    pressLeft()
    time.sleep(0.5)
    mouse.position = (121, 974)
    pressLeft()