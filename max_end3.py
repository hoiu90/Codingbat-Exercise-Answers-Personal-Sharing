def max_end3(arr):
    length=len(arr)
    if arr[0]>=arr[-1]:
        for i in range(length):
            arr[i]=arr[0]
    else:
        for i in range(length):
            arr[i]=arr[-1]
    return arr

print(max_end3([1,2,3,4,5]))
print(max_end3([5,4,3,2,1]))
print(max_end3([1,1,1,1,2]))