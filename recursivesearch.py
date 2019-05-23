# Python and the Windows file system, again, success!
# Must have full file permission otherwise it will crash
# Foreign characters will also crash out
import os

def currentDirectoryContents(dir):
    dirEntries = os.listdir(dir)
    for entry in dirEntries:
        fullPath = dir + "/" + entry
        # fullPath = os.path.join(dir,entry)
        if os.path.isfile(fullPath) and entry.lower().endswith(('.mp3', '.wav', '.wma')):
            print("Audio file found: " + fullPath)
            #if entry.lower().endswith(('.mp3', '.wav', '.wma')):
            file.write(fullPath.replace('/','\\') + "\n")
        elif os.path.isdir(fullPath):
            print("Dir:  " + fullPath)
            currentDirectoryContents(fullPath) # recursively print out the contents of the sub directory here
        else:
            print("Unknown entry: " + fullPath)

file = open("D:\\Music\\all.m3u", "w")
currentDirectoryContents("D:/Music")
file.close()

input("Press enter to end")
