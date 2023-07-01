from pynput.mouse import Controller, Button
import time
mouse = Controller()

def pressRight():
    mouse.press(Button.right)
    mouse.release(Button.right)

def pressLeft():
    mouse.press(Button.left)
    mouse.release(Button.left)


for i in range(100):
    time.sleep(1.5)
    mouse.position = (934, 502)
    pressRight()
    time.sleep(0.2)
    mouse.position = (998, 784)
    pressLeft()
    time.sleep(0.5)
    mouse.position = (511, 484)
    pressLeft()
    time.sleep(0.5)
    mouse.position = (1821, 504)
    pressLeft()