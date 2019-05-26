import pyautogui
import time

pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

print(pyautogui.size())
time.sleep(1)

width, height = pyautogui.size()

print(width, height)

# Move absolute coordinates, can also use None as an argument to keep the x or the y
def move_absolute():
    for i in range(3):
        pyautogui.moveTo(100, 100, duration=0.2)
        pyautogui.moveTo(200, 100, duration=0.2)
        pyautogui.moveTo(200, 200, duration=0.2)
        pyautogui.moveTo(100, 200, duration=0.2)

# Move relative coordinates
def move_relative():
    for i in range(2):
        pyautogui.moveRel(100, 0, duration=0.5) # right
        pyautogui.moveRel(0, 100, duration=0.5) # down
        pyautogui.moveRel(-100, 0, duration=0.5) # left
        pyautogui.moveRel(0, -100, duration=0.5) # up

# move_relative()

print(pyautogui.position())

#pyautogui.click(54, 12, button='left')
#pyautogui.rightClick(1000, 500)
#pyautogui.doubleClick(450,400)

# dragging absolute and relative as well
time.sleep(1)

#pyautogui.dragRel(50,25,duration=0.3)
#pyautogui.scroll(200) scroll 200 up