def same_first_last(lst):
    if lst[0] == lst[-1]:
        return True
    else:
        return False

# Test the function
print(same_first_last([1, 2, 3, 4, 5])) # True
print(same_first_last([1, 2, 3, 4, 5, 5])) # False  