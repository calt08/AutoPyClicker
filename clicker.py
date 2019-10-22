from pynput.keyboard import Key, Controller, Listener
import time, threading

def on_press_start(key):
    if key == Key.f12:
        print('starting...')
        return False

def on_press_loop(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press_start) as listener:
    listener.join() # wait for F11...

with Listener(on_press=on_press_loop) as listener:
    BOARD = Controller()
    time.sleep(5)
    for _ in range(50):
        print('still running...')
        BOARD.press(Key.space)
        BOARD.release(Key.space)
        time.sleep(0.25)
        if not listener.running:
            break

# time.sleep(2)
# BOARD = Controller()

# # for i in range(10):
# #     BOARD.press(Key.space)
# #     BOARD.release(Key.space)
# #     time.sleep(0.25)
# try:
#     for i in range(20):
#         BOARD.press(Key.space)
#         BOARD.release(Key.space)
#         time.sleep(0.25)
# except KeyboardInterrupt:
#     pass

# printOnConsole, on_release=c

# t1 = threading.Thread(target=)

# with Listener(on_press=clickButton) as l:
#     try:
#         l.join()
#     except Exception as e:
#         print('{0} was pressed'.format(e.args[0]))

# def printOnConsole(key):
#     BOARD = Controller()
#     if key == keyboard.Key.esc:
#         BOARD.press(Key.space)
#         BOARD.release(Key.space)

# def clickButton(key):
#     BOARD = Controller()
#     if key == keyboard.Key.esc:
#         x += 1
#         while(x == True):
#             BOARD.press(Key.space)
#             BOARD.release(Key.space)

