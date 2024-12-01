def front_back(s:str) -> str:
    if len(s) <= 1:
        return s
    else:
        return s[-1]+s[1:-1]+s[0]
    
print(front_back("hello")) # "helo"
print(front_back("a")) # "a"
print(front_back("ab")) # "ba" 