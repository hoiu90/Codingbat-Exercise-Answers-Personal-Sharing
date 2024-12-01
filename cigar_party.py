def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40 
    else:
        return cigars >= 40 and cigars <= 60 
    
# Test the function
print(cigar_party(50, True)) # True
print(cigar_party(70, False)) # True
print(cigar_party(40, False)) # True
print(cigar_party(39, False)) # False