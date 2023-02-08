import itertools

def allperm(s):
    permutation = list(s)
    permutations = list(itertools.permutations(permutation))
    return permutations

s = "ABC"

ss = allperm(s)

for x in ss:
    print(x)
