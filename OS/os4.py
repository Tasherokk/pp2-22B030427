import os

path = r"C:\Users\Nitro\Desktop\PP2\lab6\test.txt"
file = open(path, "r")
lines = 0
for i in file:
    if(i != '\n'):
        lines += 1
print("Amount of lines in this file is:", lines)
