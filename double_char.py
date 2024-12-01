def double_char(s):
    return ''.join([char*2 for char in s])

print(double_char('456'))
print(double_char('123'))
print(double_char('hello'))