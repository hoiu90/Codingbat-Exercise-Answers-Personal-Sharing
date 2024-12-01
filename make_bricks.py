def make_bricks(small, big, goal):
    if goal > small + 5 * big:
        return False
    return True
# Test the function
print(make_bricks(3, 2, 11)) # True
print(make_bricks(3, 2, 8)) # False