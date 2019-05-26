import pyautogui

print('Press CTRL-C to quit')

try:
    while True:
        x, y = pyautogui.position()
        pos_str = str(x).rjust(4) + str(y).rjust(4)

        pixel_colour = pyautogui.screenshot().getpixel((x, y))
        colour_str = str(pixel_colour)

        full_str = pos_str + ' ' + colour_str

        print(full_str, end='') # Removes the new line character
        print('\b' * len(full_str), end='', flush=True) # Backspace deletes the length of the string

except KeyboardInterrupt:
    print('\nDone')

