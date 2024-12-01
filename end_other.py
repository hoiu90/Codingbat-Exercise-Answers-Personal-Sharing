def end_other(a, b): 
    a = a.lower() 
    b = b.lower() 
    if a.endswith(b) or b.endswith(a): 
        return True 
    else: 
        return False 

print(end_other("hello", "llo")) # True 
print(end_other("hello", "world")) # False 
print(end_other("abc", "cba")) # True 
print(end_other("abc", "def")) # False