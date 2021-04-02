

while True :
    numb0=input('enter a number:')


    if numb0 == 'done':
        break
    try :
            numb=float(numb0)
    except :
        print('Invalid input')
        continue

largest = None
for value in [numb] :
    if largest is None :
        largest=value
    elif largest<value:
          largest=value
print('Maximum is',largest)

smallest=None
for valu in [numb]:

   if smallest is None :
      smallest=valu
   elif smallest>valu:
         smallest=valu
print('Minimum is',valu)
