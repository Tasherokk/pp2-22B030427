def hist(l):
    for x in l:
        for i in range(x - 1):
            print('*', end = '')
        print('*')

hist([4, 9, 7])
