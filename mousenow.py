import pyautogui

print('Press CTRL-C to quit')

try:
    while True:
        x, y = pyautogui.position()
        print(x, y)
        
except KeyboardInterrupt:
    print('\nDone')

