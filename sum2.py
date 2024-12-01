def sum2(a):
    if len(a) >=2:
        return a[0]+a[1]
    else:
        return a[0]
print(sum2([1,2]))
print(sum2([3,4,5]))
print(sum2([6]))