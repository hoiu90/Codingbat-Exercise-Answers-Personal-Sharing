def make_chocolate(s, b, g):
    n=g//5  # 这个是记录g能分成几块B
    m=(g%5) #这个是记录g处于b后，剩下多少a
    
    if b>=n and s>=m:
        return m
    elif b>=n and s<m:
        return -1
    elif b<n and s>=g-b*5:
        return g-n*5
    else:
        return -1
    
print(make_chocolate(1, 2, 10)) # Output: 2
print(make_chocolate(1, 2, 15)) # Output: -1
print(make_chocolate(1, 2, 6)) # Output: 0
print(make_chocolate(1, 2, 7)) # Output: 1
print(make_chocolate(1, 2, 8)) # Output: 1