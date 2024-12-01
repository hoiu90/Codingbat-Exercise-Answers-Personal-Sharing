def cat_dog(s):
    count_cat = 0
    count_dog = 0
    for i in range(len(s)-2):
        if s[i:i+3] == 'cat':
            count_cat += 1
        elif s[i:i+3] == 'dog':
            count_dog += 1
    return count_cat ==count_dog

        
    
print(cat_dog('catdog')) 
print(cat_dog('cat')) 
print(cat_dog('dog')) 
print(cat_dog('')) 
print(cat_dog('catcatdog')) 