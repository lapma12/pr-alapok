#1.1Feladat
"""
paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

megszamolas = 0
szin = input('Adj meg egy színt!\t')
if szin in paletta:
#1.2Feladat
if szin in paletta:
"""
#1.2Feladat
"""
    print('A', szin, len([arnyalat for arnyalat in paletta if arnyalat == szin]), '-szor szerepel a listában:', ', '.join(paletta))
	print('A megadott szín szerepel a listában.')
else:
	print('A megadott szín nem szerepel a listában.')
"""
#1.3Feladat
"""
   paletta.appned(szin)
print(', '.join(paletta))  
print('A lista színei:')
for szin in paletta:
	print(szin, end=', ')
"""
"""
#2.Feladat
import random

lista = [random.randint(1, 3) for _ in range(10)]

print('A lista:', lista)

torles = int(input('Törlendő: '))

lista = [szam for szam in lista if szam != torles]

print('A lista', torles, '-es nélkül:', lista)
"""
#3Feladat
"""
betu_leves = []

while True:
    betu = input('Betű: ')
    if not betu:
        break

    if betu.lower() in betu_leves or betu.upper() in betu_leves:
        print('Ezt a betűt már rögzítettem')
    else:
        betu_leves.append(betu)
        betu_leves.sort()

    print('Rögzített betűk:', betu_leves)"""

#1.1Feladat
"""
szo = str(input("Kérek egy szót: "))
print(szo.upper())

#1.2Feladat
lista = ["alma","körte","barack","szeder"] #|1.3Feladat|
lista1 = [szo.upper() for szo in lista if len(szo) > 3]
print('A beirt:', lista)
print('Nagybetűs:', lista1)
"""

#1.4Feladat
"""
lista = ['Html', 'CSS', 'JaVa']
lista1 = [szo.swapcase() for szo in lista]
print('Eredeti:', lista)
print('Ellentétesbetűs:',lista1)"""

#2.1Feladat
"""
tartomany = list(range(-3, 5))

ertek_keszlet = [2 * x - 3 for x in tartomany if x >= 0]

print('Értelemzési tartomány:', tartomany)
print('Érték készlet:', ertek_keszlet)"""