def has22(nums):
    for i in range(len(nums)-1):
        if nums[i]==2 and nums[i+1]==2:
            return True
    return False
nums=[1,2,2,3,4,5,2,6,7,8,9,2,10]
print(has22(nums))
nums=[1,2,3,4,5,6,7,8,9,10]
print(has22(nums))
nums=[2,2,2,2,2,2]
print(has22(nums))