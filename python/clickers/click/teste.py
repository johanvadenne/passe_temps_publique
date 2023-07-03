from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    print(f"mouse.position = ({x}, {y})")
    if not pressed:
        # Stop listener
        return False

# Collect events until released
with Listener(on_click=on_click) as listener:
    listener.join()

with Listener(on_click=on_click) as listener:
    listener.join()
    
with Listener(on_click=on_click) as listener:
    listener.join()

with Listener(on_click=on_click) as listener:
    listener.join()