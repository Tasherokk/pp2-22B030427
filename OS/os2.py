import os

path = r"C:\Users\Nitro\Desktop\PP2\lab6"
if(os.access(path, os.F_OK)):
    print("File exists")
else:
    print("File doesn't exist")

if(os.access(path, os.R_OK)):
    print("File is readable")
else:
    print("File isn't readable")

if(os.access(path, os.W_OK)):
    print("File is writable")
else:
    print("File isn't writable")

if(os.access(path, os.X_OK)):
    print("File is executable")
else:
    print("File isn't executable")
