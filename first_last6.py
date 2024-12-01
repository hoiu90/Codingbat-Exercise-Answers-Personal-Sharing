def first_last6(nums):
    length = len(nums)
    if nums[length-1] == 6:
        return True
    else:
        return False
    
print(first_last6([1, 2, 3, 4, 5, 6])) # True
print(first_last6([1, 2, 3, 4, 5, 7])) # False  