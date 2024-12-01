def sum67(nums):
    total = 0
    ignore = False
    for num in nums:
        if num == 6:
            ignore = True
            continue    
        elif num == 7 and ignore:
            ignore = False
            continue
        if not ignore:
            total += num
    return total
print(sum67([1, 2, 6, 7, 8, 9])) # Output: 25
print(sum67([1, 2, 6, 3, 4, 5, 7, 8, 9])) # Output: 25
print(sum67([1, 2, 3, 4, 5, 7, 8, 9])) # Output: 20
