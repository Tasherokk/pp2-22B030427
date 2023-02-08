def solve(h, l):
    c = 1
    while l - c * 2 != (h - c) * 4:
        c += 1
    return (c, h - c)

print(solve(35, 94))
