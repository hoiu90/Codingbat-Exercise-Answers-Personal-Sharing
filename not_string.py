def not_string(s):
    if s.startswith('not'):
        return s
    else:
        return 'not'+ s
    
print(not_string('apple')) # not apple
print(not_string('not apple')) # not apple
print(not_string('not')) # not
print(not_string('')) # not