def has33(nums):
    for i in range(len(nums)):
        if i == 0:
            continue
        elif nums[i] == 3 and nums[i-1] == 3:
            return True
    return False

print(has33([1, 3, 3]))
print(has33([1, 3, 1, 3]))
print(has33([3, 1, 3]))
