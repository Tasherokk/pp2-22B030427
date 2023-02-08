def rev(s):
    l = []
    z = ""
    for x in s:
        if x == ' ':
            l.append(z)
            z = ""
        else :
            z = z + x
    l.append(z)
    return(list(reversed(l)))

s = "We are ready"

s = rev(s)

for x in s:
    print(x, end = ' ')
