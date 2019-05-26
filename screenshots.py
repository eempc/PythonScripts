import pyautogui

image = pyautogui.screenshot()

coords = (1800,980)
x, y = coords

print("Full RGB of pixel",coords,image.getpixel(coords))
print("Red value is", image.getpixel(coords)[0])

# Colour match boolean, e.g. is pixel 1800, 300 of RGB 35,35,35 ?
print(pyautogui.pixelMatchesColor(x, y, (35, 35, 35)))

# Found the Split Terminal button (slow)
button_coords = pyautogui.locateOnScreen('vsbin.png')
print(button_coords)

auto_centre_coords = pyautogui.center(button_coords)
print(auto_centre_coords)

pyautogui.moveTo(auto_centre_coords, duration=0.2)
# or click
#pyautogui.click(auto_centre_coords)

#image_search = 'vsbin.png'
#image_list = list(pyautogui.locateAllOnScreen(image_search))
#print(image_list)



## Biggest issue here is to ensure that coordinates are tuples in brackets, and that the brackets are correct