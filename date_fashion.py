def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    elif you >= 8 or date >= 8:
        return 2
    else:
        return 1

print(date_fashion(3, 9)) # Output: 2
print(date_fashion(5, 7)) # Output: 1
print(date_fashion(2, 2)) # Output: 0