def alarm_clock(time,vacation):
    if (time>=1 and time<=5 and vacation==False):
        return 7.00
    elif (time>=6 and time<=7 and vacation==False):
        return 10.00
    elif (time>=1 and time<=5 and vacation==True):
        return 10.00
    else:
        return 10.00
print(alarm_clock(3,False)) # Output: 7
print(alarm_clock(6,False)) # Output: 10
print(alarm_clock(3,True)) # Output: 10
print(alarm_clock(8,False)) # Output: 10
print(alarm_clock(1,False)) # Output: 7