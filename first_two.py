def firsr_two(a ):
    if isinstance(a, (str,list)):
        return a [:2]
    else:
        return []
print(firsr_two([1, 2, 3, 4, 5])) # Output: [1, 2] 
print(firsr_two([1])) # Output: [1]
print (firsr_two("sdasddas")) # Output: []