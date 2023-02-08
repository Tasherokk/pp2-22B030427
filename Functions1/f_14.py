def has33(nums):
    for i in range(len(nums)):
        if i == 0:
            continue
        elif nums[i] == 3 and nums[i-1] == 3:
            return True
    return False

def spy_game(nums):
    c = 0
    for i in range(len(nums)):
        if (c == 0 or c == 1) and nums[i] == 0:
            c += 1
        elif c == 2 and nums[i] == 7:
            return True
    return False

def ispal(nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True

def hist(nums):
    for x in nums:
        for i in range(x - 1):
            print('*', end = '')
        if x != 0:
            print('*')
        else:
            print()

l = []
while True:
    n = int(input())
    if n == -1:
        break
    l.append(n)

if(has33(l) and spy_game(l) and ispal(l)):
    hist(l)
else:
    print("Nope")
