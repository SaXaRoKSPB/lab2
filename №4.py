f = open('sequence.txt')
ffile = []
for i in f:
    ffile.append(float(i))
km = 0
kb = 0
for i in range(len(ffile)):
    if ffile[i]<-5:
        km += 1
    else:
        if ffile[i]<=0:
            kb +=1
print('\u001b[41;1m' + ' ' * km + '\u001b[0m' + '  <-5')
print('\u001b[42;1m' + ' ' * kb + '\u001b[0m' + '  >-5')