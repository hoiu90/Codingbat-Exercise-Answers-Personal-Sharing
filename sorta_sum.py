def sorta_sum(a, b):
    sum = a + b
    if sum>=10 and sum<=20:
        return 20
    else:
        return sum

print(sorta_sum(5, 10)) # Output: 15
print(sorta_sum(15, 10)) # Output: 20
print(sorta_sum(10, 10)) # Output: 20   