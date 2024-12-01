def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return True
    else:
        return False
    
print(parrot_trouble(True, 6)) # True
print(parrot_trouble(True, 21)) # True
print(parrot_trouble(False, 6)) # False
print(parrot_trouble(False, 21)) # False