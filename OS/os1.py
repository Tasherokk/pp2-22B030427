import os

path = r"C:\Users\Nitro\Desktop\PP2\lab6"
print("Allfolders in this path: ")
for i in os.listdir(path):
    if os.path.isdir(os.path.join(path, i)):
        print(i)
        
print("\nAll files in this path: ")
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        print(i)
        
print("\nAll files and folders: ")
for i in os.listdir(path):
    print(i)
