def count_evens(nums):
    count=0
    for i in nums:
        if i%2==0:
            count+=1
    return count
nums=[1,2,3,4,5,6,7,8,9,10]
print(count_evens(nums))
nums=[1,3,5,7,9]
print(count_evens(nums))
nums=[2,4,6,8,10]
print(count_evens(nums))