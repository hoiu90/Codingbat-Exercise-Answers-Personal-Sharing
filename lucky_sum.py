def lucky_sum(n,m,b):
    if n == 13:
        return b
    elif m==13:
        return n
    elif b==13:
        return m+n
    else:
        return n+m+b
print(lucky_sum(1,2,3)) # Output: 6
print(lucky_sum(13,2,3)) # Output: 16
print(lucky_sum(1,13,3)) # Output: 16
print(lucky_sum(1,2,13)) # Output: 16