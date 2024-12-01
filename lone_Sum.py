def lone_sum(a,b,c):
    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    else:
        return a+b+c
    
print(lone_sum(1,2,3)) # Output: 6
print(lone_sum(1,2,2)) # Output: 3
print(lone_sum(1,3,2)) # Output: 6