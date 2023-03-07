s = input()
ul = 0
ll = 0
for i in s:
    if(ord(i) >= 65 and ord(i) <= 90):
        ul += 1
    elif(ord(i) >= 97 and ord(i) <= 122):
        ll += 1
print("Lower case letters:", ll, "\nUpper case letters:", ul)
