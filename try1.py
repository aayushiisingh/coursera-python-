number= input('enter a number')
try:
    alpha=int(number)
except:
    alpha =-1

if alpha > 0 :
    print('it is a number')
else :
    print('you did not enter a number')
