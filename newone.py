fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
stuff=fh.read()
for line in stuff :
    line=line.lstrip()
    wrd=line.split()
    print(wrd)
    if len(wrd)<1:
        continue
        if wrd[0] != 'From':
            continue
            print(wrd[2])
