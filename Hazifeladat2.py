#Házi feladat2
szam1 = int(input('Kérem az első számot 1-100 között: '))
szam2 = int(input('Kérem a második számot 1-100 között: '))
if szam1 == szam2:
    print('A két szám megegyezik')
if szam1 > szam2:
    print('Két szám nem egyezik meg')
    print('A második szám kisebb, a különbségük:',szam1 - szam2) 
if szam1 < szam2:
    print('két szám nem egyezik meg ')
    print('A második szám nagyobb, a különbségük:',szam2 - szam1) 
