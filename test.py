from pynput import mouse

def on_move(x, y):
    print('Mouse moved to ({}, {})'.format(x, y))

with mouse.Listener(on_move=on_move) as listener:
    listener.join()
