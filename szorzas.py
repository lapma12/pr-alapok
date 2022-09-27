# könyv példája
szorzandó = 5
szorzó = input('Mennyivel szorozzam meg az ' + str(szorzandó) + '-öt? ')
print(szorzandó, '-ször ', szorzó, ' annyi mint ', sep='', end='')
szorzó = int(szorzó)
print(szorzandó * szorzó)
