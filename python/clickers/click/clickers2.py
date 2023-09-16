from pynput.mouse import Controller, Button
import time
mouse = Controller()

def pressRight():
    mouse.press(Button.right)
    mouse.release(Button.right)

def pressLeft():
    mouse.press(Button.left)
    mouse.release(Button.left)


for i in range(23):
    time.sleep(0.5)
    mouse.position = (1142, 753)
    pressLeft()
    time.sleep(0.5)
    mouse.position = (1078, 734)
    pressLeft()