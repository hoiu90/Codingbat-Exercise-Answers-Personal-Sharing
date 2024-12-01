def xyz_there(s):
    if ".xyz" in s:
        return False
    elif "xyz" in s:
        return True
    else:
        return False

print(xyz_there("abc.xyz"))  # False
print(xyz_there("abcxyz"))  # True
print(xyz_there("xyz.txt"))  # False