def big_diff(arr):
    min_num = min(arr)
    max_num = max(arr)
    return max_num - min_num

print(big_diff([1, 2, 3, 4, 5])) # Output: 4
print(big_diff([10, 20, 30, 40, 50])) # Output: 40  