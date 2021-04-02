smallest = None
for value in [14,45,26,27,8,6,4,1,12,16,19,55,3,90,1] :
    if smallest is None :
        smallest=value
    elif smallest>value :
         smallest=value
print('the smallest no is',smallest)
