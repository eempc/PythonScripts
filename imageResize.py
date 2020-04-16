#!python3.7
import os
from PIL import Image

imageFiles = ('.png', 'jpg', 'jpeg', 'gif')

def resizeAllImagesInDir(dir):
    entriesList = os.listdir(dir)
    for entry in entriesList:
        fullPath = dir + "/" + entry
        if os.path.isfile(fullPath) and entry.lower().endswith(imageFiles):
            print("Image file found: " + fullPath)
            image = Image.open(fullPath)
            width, height = image.size
            print(width, height)