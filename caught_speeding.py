def caught_speeding(speed, is_birthday):
    if is_birthday:
        if (speed <= 65):
            return 0
        elif (speed <= 85 and speed >= 66):
            return 1
        else:
            return 2
    else:
        if (speed <= 60):
            return 0
        elif (speed <= 80 and speed >= 61):
            return 1
        else:
            return 2
# Test the function
print(caught_speeding(65, True)) # Expected output: 0
print(caught_speeding(66, True)) # Expected output: 1
print(caught_speeding(67, True)) # Expected output: 2
print(caught_speeding(60, False)) # Expected output: 0