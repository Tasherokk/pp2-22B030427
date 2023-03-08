import os

path = r"C:\Users\Nitro\Desktop\PP2\lab6\AtoZ"
for i in range(65, 91):
    os.mkdir(path + "\\" + chr(i) + ".txt")

for i in os.listdir(path):
    print(i)
