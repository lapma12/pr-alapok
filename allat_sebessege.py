# könyv példája
állatfaj = input('Add meg egy állatfaj nevét! ')
sebesség = input('Add meg az állatfaj sebességét! ')
sebesség = int(sebesség)
if sebesség <= 50:
 hol = 'városban'
elif sebesség <= 90:
 hol = 'országúton'
else:
 hol = 'autópályán'
print('Az', állatfaj, 'legnagyobb sebességével', hol, 'haladhat.')
