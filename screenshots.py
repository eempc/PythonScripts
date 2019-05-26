import pyautogui

image = pyautogui.screenshot()

coords = (1800,980)
x, y = coords

print("Full RGB of pixel",coords,image.getpixel(coords))
print("Red value is", image.getpixel(coords)[0])

# Colour match boolean, e.g. is pixel 1800, 300 of RGB 35,35,35 with tolerance of 10 colour units
print(pyautogui.pixelMatchesColor(x, y, (35, 35, 35), tolerance=10))

# Found the Split Terminal button (slow)
button_box_coords = pyautogui.locateOnScreen('vsbin.png', region=(0, 0, 1919, 1079))
print(button_box_coords)

auto_centre_coords = pyautogui.center(button_box_coords)
print(auto_centre_coords)

pyautogui.moveTo(auto_centre_coords, duration=0.2)
# or click
#pyautogui.click(auto_centre_coords)

## For multiple results
#image_search = 'vsbin.png'
#image_list = list(pyautogui.locateAllOnScreen(image_search))
#print(image_list)



## Biggest issue here is to ensure that coordinates are tuples in brackets, and the correct number of brackets are there