def computepay(h,r):
    if h > 40 :
        fixed = r*h
        extra= (h-40)*r*0.5
        total= fixed+extra
    else :
        total=r*h
    return total    


hrs = input("Enter Hours:")
rate =input('enter rate:')
ho = float(hrs)
ra = float(rate)
p = computepay(ho,ra)
print("Pay",p)
