def combo_string(s1, s2):
    if len(s1)>len(s2):
        return s2+s1+s2
    else:
        return s1+s2+s1
print(combo_string("hello", "world")) # Output: 12
print(combo_string("abc", "def")) # Output: 6
print(combo_string("abcd", "fgh")) # Output: 10