xfile =open('jl.txt')
for  butter in xfile :
    butter= butter.rstrip()
    if not butter.startswith("I'm") :
        continue
    print(butter)
