def centered_average(nums):
    min_num = min(nums)
    max_num = max(nums)
    sum = 0
    for i in range(len(nums)-2):
        sum += nums[i]
    return sum / (len(nums)-2)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(centered_average(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(centered_average(nums))
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(centered_average(nums))