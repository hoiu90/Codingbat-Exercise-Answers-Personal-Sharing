def no_teen_sum(n):
    if 13<=n<=19 and n not in [15,16]:
        return 0
    return n

def no_teen_sum_list(a,b,c):
    return no_teen_sum(a) + no_teen_sum(b) + no_teen_sum(c)

print(no_teen_sum_list(1,2,3)) # Output: 6
print(no_teen_sum_list(2,13,1)) # Output: 3
print(no_teen_sum_list(2,1,14)) # Output: 3