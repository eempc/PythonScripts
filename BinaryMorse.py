import string


file = open("BinaryMorse.txt", "w")

for c in string.ascii_lowercase:
    str = f"static Node {c} = new Node(\'{c.upper()}\', null, null);"
    print(str)
    file.write(str + '\n')

file.close()