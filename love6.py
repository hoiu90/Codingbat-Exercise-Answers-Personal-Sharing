def love6(n,m):
    if n == 6 or m == 6:
        return True
    elif (n+m==6)or (abs(n-m)==6):
        return True
    else:
        return False

print(love6(3,4)) # False
print(love6(6,6)) # True
print(love6(1,5)) # True
print(love6(5,1)) # True
print(love6(2,5)) # False