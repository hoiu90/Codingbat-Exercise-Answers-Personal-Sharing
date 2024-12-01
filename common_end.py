def common_end(a, b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False
print(common_end("hello", "world")) # True 
print(common_end("hello", "hell")) # True 
print(common_end("hello", "ello")) # True 
print(common_end([1,2,3,1], [1,23,4,51,6,7,8,9,10])) # False 