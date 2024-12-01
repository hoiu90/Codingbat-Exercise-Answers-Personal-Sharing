def sum3(a):
    length=len(a)
    sum=0
    for i in range(length):
        sum+=a[i]
    return sum
print(sum3([1,2,3,4,5]))
print(sum3([10,20,30,40,50]))