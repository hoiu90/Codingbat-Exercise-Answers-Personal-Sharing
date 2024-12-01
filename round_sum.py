def round_sum(a):
    if 6<=(a % 10)<=9 and a%10>=1:
        return 10*(a%10+1)
    elif 0<=(a % 10)<=5 and a%10>=1:
        return 10*(a%10)
    elif 6<=(a % 10)<=9 and a%10<1:
        return 10
    elif 0<=(a % 10)<=5 and a%10<1:
        return 0
    else:
        return a
def round_sum_list(a,b,c):
    return round_sum(a)+round_sum(b)+round_sum(c)

print(round_sum_list(12,34,56))
print(round_sum_list(12,34,567))
print(round_sum_list(12,34,5678))