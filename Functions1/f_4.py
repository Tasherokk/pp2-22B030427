def isprime(x):
    for i in range(x):
            if i == 1 or i == 0:
                continue
            if x % i == 0:
                return False
    return True

def filter_prime(v):
    l = []
    for x in v:
        if isprime(x):
            l.append(x)
    return l

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_prime(a))
