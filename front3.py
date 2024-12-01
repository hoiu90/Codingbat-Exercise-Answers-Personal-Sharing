def front3(str):
    if len(str) >= 3:
        return str[:3]*2
    else:
        return str*2
print(front3("hello")) # Output: "helhel"
print(front3("abc")) # Output: "abcabc"
print(front3("ab")) # Output: "abab"