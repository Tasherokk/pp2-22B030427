import os

path1 = r"C:\Users\Nitro\Desktop\PP2\lab6\test1.txt"
path2 = r"C:\Users\Nitro\Desktop\PP2\lab6\test2.txt"

file1 = open(path1, "r")
text = file1.read()
file2 = open(path2, "w")
file2.write(text)
file2.close()
file2 = open(path2, "r")
print(file2.read())

