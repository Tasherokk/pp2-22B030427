def spy_game(nums):
    c = 0
    for i in range(len(nums)):
        if (c == 0 or c == 1) and nums[i] == 0:
            c += 1
        elif c == 2 and nums[i] == 7:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))
