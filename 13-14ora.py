"""
szam1 = int(input('Kérek egy egész számot: '))
szam2 = int(input('Kérek egy másik egész számot: '))
if szam1 > szam2:
    print('szam1 nagyobb mint a szam2')
if szam2 > szam1:
    print('szam2 nagyobb mint a szam1')
if szam1 == szam2:
    print('szam1 megegyezik a szam2-vel')"""

#-------------------------------------------

"""
szam1 = int(input('Kérek egy egész számot: '))
szam2 = int(input('Kérek egy másik egész számot: '))
if szam1 > szam2:
    print('szam1 nagyobb mint a szam2')
elif szam2 > szam1:
    print('szam2 nagyobb mint a szam1')
elif szam1 == szam2:
    print('szam1 megegyezik a szam2-vel')"""

#-----------------------------------------------

"""
szam1 = int(input('Kérek egy egész számot: '))
szam2 = int(input('Kérek egy másik egész számot: '))
if szam1 > szam2:
    print('szam1 nagyobb mint a szam2')
elif szam2 > szam1:
    print('szam2 nagyobb mint a szam1')
else:
    print('szam1 megegyezik a szam2-vel')"""

#-----------------------------------

"""
x = None
print(x)
print(type(x))

if x:
    print('Do you think None is true')
elif x is False:
    print('Do you think is false')
else:
    print('None is not true, or false ,None is just true...')"""

#----------------------------------------
"""
jegy = input('Kérek egy jegyet:')
if jegy == "1":
    print('Elégtelen')
elif jegy == "2":
    print('Elégséges')
elif jegy == "3":
    print('Közepes')
elif jegy == "4":
    print('Jó')
elif jegy == "5":
    print('Jeles')
else:
    print("Nincs ilyen osztályzat")
"""
#------------------------------------------

#Bekérek egy pozitív egész számot.Írjuk ki hogy páros vagy váratlan
"""
szam = int(input('Kérek egy egész számot: '))
if szam % 2 == 0 :
    print('A szám páros')
else:
    print("A szám páratlan")"""

#-------------------------------------------

# Véletlen szám előálítása
"""
import random

gondolt_szám = random.randint(1,6)
print('Súgók:', gondolt_szám)
tipp = int(input('Gondoltam egy számra.Tippeld meg: '))
if tipp == gondolt_szám:
    print('Egyezik')
else:
    print('Nem egyezik')"""



#Generaájunk 1-1000 között,irassuk ki a számot ha páros és kisebb mint 500 ,ha nme igaz akkor nem felet mega követelményeknek

import random

szam = random.randint(1,1000)
print(szam)
if not(szam % 2 == 0) and szam <= 500:
    print('Jó')
else:
    print('Nem jó')
