def uniq(v):
    used = [0]
    l = []
    for i in range(1000):
        used.append(0)
    for x in v:
        if used[x] == 0:
            l.append(x)
        used[x] = 1
    return l

print(uniq([1, 1, 2, 2, 3, 3, 0, 0, 3, 2, 5]))
