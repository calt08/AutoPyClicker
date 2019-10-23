from pynput.keyboard import Key, Controller, Listener
import time

def on_press_start(key):
    if key == Key.space:
        print('starting...')
        return False

def on_press_loop(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press_start) as listener:
    listener.join() # Waits for the spacebar to be pressed

with Listener(on_press=on_press_loop) as listener:
    BOARD = Controller()
    time.sleep(2)
    while True:
        print('still running...')
        BOARD.press(Key.space)
        BOARD.release(Key.space)
        time.sleep(0.01)
        if not listener.running:
            break

