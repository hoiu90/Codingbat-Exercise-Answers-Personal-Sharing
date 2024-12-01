def has23(nums):
    length = len(nums)
    for i in range(length):
        if nums[i] == 2 or nums[i] == 3:
            return True
    return False

print(has23([1, 2, 3, 4, 5]))  # True
print(has23([1, 2, 4, 5]))  # False
print(has23([2, 3, 5]))  # True