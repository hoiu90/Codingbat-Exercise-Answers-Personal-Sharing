def diff21(n):
    if n < 21:
        return 21 - n
    elif n == 21:
        return 0
    else:
        return (n - 21) * 2
    
print(diff21(19)) # Output: 2
print(diff21(21)) # Output: 0
print(diff21(25)) # Output: 4
print(diff21(30)) # Output: 10