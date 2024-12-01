def makes10(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False
print(makes10(5, 5)) # True
print(makes10(5, 10)) # True
print(makes10(10, 5)) # True
print(makes10(10, 10)) # True
print(makes10(3, 7)) # False