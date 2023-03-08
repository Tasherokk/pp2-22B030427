import os

path = r"C:\Users\Nitro\Desktop\PP2\lab6\test1.txt"

mylist = ["666", "cups", "of", "tea", "14 points :D"]
file = open(path, "w")
for s in mylist:
    file.write(s + ' ')
file.close()

file = open(path, "r")
print(file.read())

