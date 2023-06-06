from pynput.mouse import Controller, Button
import time
mouse = Controller()

def pressRight():
    mouse.press(Button.left)
    mouse.release(Button.left)

def pressLeft():
    mouse.press(Button.left)
    mouse.release(Button.left)


for i in range(3000):
    time.sleep(5)
    mouse.position = (1899, 547)
    pressLeft()