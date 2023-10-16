from pynput.mouse import Controller, Button
import time
mouse = Controller()

def pressRight():
    mouse.press(Button.right)
    mouse.release(Button.right)

def pressLeft():
    mouse.press(Button.left)
    mouse.release(Button.left)
    

time.sleep(0.5)
for i in range(1757):
    mouse.position = (932, 489)
    pressRight()
    time.sleep(0.1)
    mouse.position = (1025, 695)
    pressLeft()
    time.sleep(2)
    mouse.position = (784, 506)
    pressLeft()
    time.sleep(0.3)
    mouse.position = (1824, 486)
    pressLeft()
    time.sleep(1)