def build_class(name, attributes,**kwargs):
    
    user_info={}
    user_info['qicheng_sun']=name
    user_info['attributes']=attributes
    
    user_info.update(kwargs)
    return user_info     

    user_text=build_class(
        'qicheng_sun',
        ['age','gender','height'],
        loction='beijing',
        filed='computer science'
    )
    print(user_text)
    