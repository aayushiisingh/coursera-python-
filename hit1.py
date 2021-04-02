largest=None
smallest=None
while True :
    numb0=input('enter a number:')


    if numb0 == 'done':
        break
    try :
            numb=float(numb0)
    except :
        print('Invalid input')
        continue

    if largest is None :
        largest=numb
    elif largest<numb:
         largest=numb

    if smallest is None :
         smallest=numb
    elif smallest>numb :
         smallest = numb

print('Maximum is',largest)
print('Minimum is',smallest)
