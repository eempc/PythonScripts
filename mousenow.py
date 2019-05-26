import pyautogui

print('Press CTRL-C to quit')

try:
    while True:
        x, y = pyautogui.position()
        pos_str = str(x).rjust(4) + str(y).rjust(4)
        print(pos_str, end='') # Removes the new line character
        print('\b' * len(pos_str), end='', flush=True) # Backspace deletes the length of the string

except KeyboardInterrupt:
    print('\nDone')

