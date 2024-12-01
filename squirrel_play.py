def squirrel_play(temp, is_summer):
    if temp >= 60 and temp <= 100 and is_summer:
        return True
    else:    
        return False

print(squirrel_play(70, True)) # True
print(squirrel_play(120, True)) # False
print(squirrel_play(50, False)) # False