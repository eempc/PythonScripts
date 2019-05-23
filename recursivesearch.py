# Python and the Windows file system, again, success!
# Must have full file permission otherwise it will crash
# Foreign characters will also crash out
import os

musicFiles = ('.mp3', '.wav', '.wma') # Tuples are (), arrays are []

def currentDirectoryContents(dir):
    # Take the dir argument and create an array of its contents
    dirEntries = os.listdir(dir)
    #Then loop through the array
    for entry in dirEntries:
        # Concatenate the full path together (2 ways listed here)
        fullPath = dir + "/" + entry
        # fullPath = os.path.join(dir,entry)
        if os.path.isfile(fullPath) and entry.lower().endswith(musicFiles):
            print("Audio file found: " + fullPath)
            #if entry.lower().endswith(('.mp3', '.wav', '.wma')):
            file.write(fullPath.replace('/','\\') + "\n") # Conversion to Windows format
        elif os.path.isdir(fullPath):
            print("Dir:  " + fullPath)
            currentDirectoryContents(fullPath) # recursively print out the contents of the sub directory here
        else:
            print("Unknown entry: " + fullPath)

# Output file
file = open("D:\\Music\\all.m3u", "w")
    # Activate the recursive function
currentDirectoryContents("D:/Music")
file.close()

input("Press enter to end")
