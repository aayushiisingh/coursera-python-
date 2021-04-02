hrs = input("Enter Hours:")
h = float(hrs)
rate= input('enter rate:')
r = float(rate)
if h > 40 :
    fixed = r*h
    extra= (h-40)*r*0.5
    total= fixed+extra
else :
    total=r*h
print("pay",total)
