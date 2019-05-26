import pyautogui
import time

time.sleep(3)

message = "Hello World"
key_presses = ["!", "enter"]
interval = 0.1

pyautogui.typewrite(message, interval)
pyautogui.typewrite(key_presses)

# To get the Euro symbol (method 1)
pyautogui.keyDown('ctrlleft')
pyautogui.keyDown('altleft')
pyautogui.press('4')
pyautogui.keyUp('ctrlleft')
pyautogui.keyUp('altleft')

# Hotkey method
pyautogui.hotkey('ctrl', 'alt', '4')