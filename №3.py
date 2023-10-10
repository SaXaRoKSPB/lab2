ploskost=[['\u001b[47m' + ' ']*5 for i in range(11)]
for i in range(11):
    if i%3==0:
        ploskost[i][i//3] = '\u001b[44m' + ' '
for i in range(len(ploskost)-1, -1, -1):
    print('\u001b[47m'+ str(i), *ploskost[i])
s='  '
for i in range(4):
    s += str(i) + ' '
print(s+'\u001b[0m')
print('f(x)=3x')
