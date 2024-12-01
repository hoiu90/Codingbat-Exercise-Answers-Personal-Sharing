def near_hundred(n):
    if (n >= 90 and n <= 110) or (n >= 190 and n <= 210):
        return True
    else:
        return False
    
print(near_hundred(100)) # True
print(near_hundred(105)) # True
print(near_hundred(110)) # True     
print(near_hundred(190)) # True
print(near_hundred(195)) # True
print(near_hundred(200)) # True
print(near_hundred(210)) # True
print(near_hundred(2215)) # False