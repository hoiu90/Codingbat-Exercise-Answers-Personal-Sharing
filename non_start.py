def non_start(a, b):
    return a[1:] + b[1:]
print(non_start('hello', 'world')) # Output: "elloorld"
print(non_start('abc', 'xyz')) # Output: "bcxyz"