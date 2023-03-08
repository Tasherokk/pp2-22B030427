import os

file = "test3.txt"
path = r"C:\Users\Nitro\Desktop\PP2\lab6"
#if os.access(os.path.join(path, file), os.F_OK) == False:
#    os.mkfile(os.path.join(path, file))
print("Current files:")
for i in os.listdir(path):
    print(i)
print()
    
if(os.access(os.path.join(path, file), os.F_OK)):
    if(os.access(os.path.join(path, file), os.X_OK)):
        os.remove(os.path.join(path, file))

print("Files after deleting:")
for i in os.listdir(path):
    print(i)
