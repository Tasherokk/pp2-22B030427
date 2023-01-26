n = 0
x = []
sm = 0
mn = 999999999
mx = -999999999
thisdict = {}
print("Enter values, ending with \"0\":")
while 1:
    a = int(input())
    if a == 0:
        break
    if a in thisdict:
        thisdict[a] += 1
    else:
        thisdict[a] = 1
    n += 1
    if a > mx:
        mx = a
    if a < mn:
        mn = a
    sm += a
    x.append(a)
print("min val:",mn)
print("max val:",mx)
print("sum is:",sm)
print("average val:",sm / n)
uniq = set(x)
print("Unique values are:")
for i in uniq:
    print(i, "-", thisdict[i])
