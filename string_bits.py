def string_bits(str):
    return str[::2]

print(string_bits("Hello World")) # "HloWrd"
print(string_bits("Python is awesome")) # "Pythn sweme"
print(string_bits("123456789")) # "13579"
