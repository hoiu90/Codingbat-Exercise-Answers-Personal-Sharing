def rotate_left3(nums):
    return nums[1:] + nums[:1]

print(rotate_left3([1,2,3,4,5]))
print(rotate_left3([1,2,3,4]))