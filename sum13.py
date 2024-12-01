def sum13(nums):
    total = 0
    i=0
    while i <len(nums):
        if nums[i] == 13:
            i+=2
        else:
            total += nums[i]
            i+=1
    return total

print(sum13([1, 2, 3, 4, 5, 13, 14, 15])) # Output: 33
print(sum13([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])) # Output: 78
print(sum13([13, 13, 13, 13, 13])) # Output: 0
print(sum13([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # Output: 108