from pynput import keyboard
list = []

def on_press(key):
    global list
    print('Key {} pressed.'.format(key))
    list.append(key)

def on_release(key):
    global list
    print('Key {} released.'.format(key))
    if str(key) == 'Key.esc':
        print('Exiting...')
        print(list)
        return False

with keyboard.Listener(
    on_press = on_press,
    on_release = on_release) as listener:
    listener.join()