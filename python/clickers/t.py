from pynput.mouse import Controller, Button
import time
mouse = Controller()

def pressRight():
    mouse.press(Button.right)
    mouse.release(Button.right)

def pressLeft():
    mouse.press(Button.left)
    mouse.release(Button.left)


time.sleep(2)
print(mouse.position)