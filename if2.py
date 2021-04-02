score = input("Enter Score: ")
try :
    score <= 1.0
except :
    print("input not acceptable")

if score >=9.0:
    print('A')
elif score >=0.8:
    print('B')
elif score >=0.7:
    print('C')
elif score >=0.6:
    print('D')
elif score <0.6:
    print('F')
