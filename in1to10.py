def in1to10(n,outside_mode):
    if n <= 1 or n >= 10 and outside_mode == True:
        return True
    elif n <= 1 or n >= 10 and outside_mode == False:
        return False
    elif n>=1 and n<=10 and outside_mode == False:
        return True
    else:
        return False
    
print(in1to10(5,True)) # True
print(in1to10(11,True)) # False
print(in1to10(5,False)) # True
print(in1to10(11,False)) # True