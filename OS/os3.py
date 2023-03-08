import os

path = r"C:\Users\Nitro\Desktop\PP2\lab6\OS\os1.py"
if os.access(path, os.F_OK):
    print("Your path exists")
    x = os.path.split(path)
    print("Directory of the file:", x[0])
    print("Name of file:", x[1])
else:
    print("Your path doesn't exist")
