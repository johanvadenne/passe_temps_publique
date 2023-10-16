from pynput.mouse import Controller, Button
import time
mouse = Controller()

def pressRight():
    mouse.press(Button.left)
    mouse.release(Button.left)

def pressLeft():
    mouse.press(Button.left)
    mouse.release(Button.left)


time.sleep(0.5)
for i in range(40):
    mouse.position = (1888, 57)
    pressLeft()
    time.sleep(0.5)
    mouse.position = (1686, 59)
    pressLeft()
    pressLeft()
    time.sleep(2)
    mouse.position = (1301, 612)
    pressLeft()
    time.sleep(0.5)
    mouse.position = (1889, 531)
    pressLeft()
    time.sleep(2)