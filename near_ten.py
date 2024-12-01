def near_ten(num):
    if (num%10) ==8 or (num%10) ==9 or (num%10) ==1 or (num%10) ==2 or (num%10)==0:
        return True
    else:
        return False
    
print(near_ten(10)) # True
print(near_ten(12)) # True
print(near_ten(15)) # False
print(near_ten(20)) # True
print(near_ten(22)) # False
print(near_ten(18)) # True