idei_év = 2022 # módosítva
születési_év = input('Melyik évben születtél? ')
születési_év = int(születési_év)
volte = input('Volt már idén születésnapod? (i/n) ')
szülinapok_száma = idei_év - születési_év - 1
if volte == 'i':
 szülinapok_száma = szülinapok_száma + 1
print('Utoljára a ', szülinapok_száma, '. születésnapodat ünnepelted.', sep='')
