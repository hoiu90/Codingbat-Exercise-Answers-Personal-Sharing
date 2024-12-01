def missing_char(s: str, n: int) -> str:
    
    return s[:n] + s[n+1:]
print(missing_char("hello", 1)) # "hlleo"
print(missing_char("python", 3)) # "pythno"
print(missing_char("coding", 4)) # "codiing"