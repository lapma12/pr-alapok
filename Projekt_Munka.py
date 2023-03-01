

def osszegzes():
    print("ÖSSZEGZES TÉTELE")
    print('Ez a program kiszámolja az átlagodat.')
    print('Ha már nem akarsz több jegyet megadni, írj 0-át!')
    print('--------------------------------------------')

    darab = 0
    osszeg = 0

    erdemjegy = int(input('Add meg az első érdemjegyet: '))
    while erdemjegy != 0:
        darab = darab + 1
        osszeg = osszeg + erdemjegy
        erdemjegy = int(input('Add meg az következő érdemjegyet: '))
    
    if darab != 0:
        print('A jegyeid átlaga: ', osszeg / darab)
    else:
        print('Nem adtál meg egy jegyet sem!')



def eldontes():
    lista1 = [2, 5, 4, 8, 9, 11, 10, 12]
    print("ELDÖNTÉS TÉTELE")
    print()
    print(f"Az eldöntés lista  {lista1}")
    talalat = False
    index = 0
    while index < len(lista1) and not talalat:
        if lista1[index] % 3 == 0:
            talalat = True
        index = index + 1
    
    if talalat:
        print('Van a listában hárommal osztható szám.')
    else:
        print('Nincs a listában hárommal osztható szám.')


#-------------------------------------------------------------------

def kereses():
    lista2 = ['kék', 'zöld', 'piros', 'fehér']

    print("KERESÉS TÉTELE")
    print()
    print(f"A keresés lista {lista2}")
    talalat = False
    index = 0
    while index < len(lista2) and not talalat:
        if lista2[index] == 'piros':
                talalat = True
        index = index + 1

    if talalat:
        print('Van a listában piros szín, az indexe: ', index-1)
    else:
        print('Nincs a listában piros szín.')



#-------------------------------------------------------------------

def kivalasztas():
    lista3 = [2, 5, 4, 8, 9, 11, 10, 12]

    print("KIVALASZTÁS TÉTELE")
    print()
    print(f"Kiválasztás lista {lista3}")
    talalat = False
    index = 0
    while not talalat:
        if lista3[index] % 3 == 0:
            talalat = True
        index = index + 1

    print('A hárommal osztható szám indexe a listában: ', index - 1)
    


#-------------------------------------------------------------------

def szamlalas():

    lista4 = [2, 5, 4, 8, 9, 11, 10, 12]
    print("SZAMLALÁS TÉTELE")
    print()
    print(f"Számlálás lista {lista4}")
    talalat = False
    index = 0
    while not talalat:
        if lista4[index] % 3 == 0:
            talalat = True
        index = index + 1

    print('A hárommal osztható szám indexe a listában: ', index - 1)


#-------------------------------------------------------------------


def szelso_ertekek():
    szamok = [3,21,7,63,9,27]
    print("SZÉLSŐÉRTÉK TÉTELE")
    print()
    print(f"Szélsőérték lista {szamok}")
    min = szamok[0]
    max = szamok[0]
    for szam in szamok:
        if szam < min:
            min = szam
        elif szam > max:
            max = szam

    print(f"A számok listában a legkisebb szám a {min}")
    print(f"A számok listában a legnagyobb szám a {max} ")

#-------------------------------------------------------------------------------

print("Kérdbe a számokkal az adott Tételt, és írj egy 0-át a kilépéshez!")
print()
while True:
    print()
    print("1 = Összegzés")
    print("2 = Eldöntés")
    print("3 = Keresés")
    print("4 = Kivalasztás")
    print("5 = Megszámlálás")
    print("6 = Szélsőérték")
    fuggveny = int(input("Kérem a függvény számát: "))
    if fuggveny == 1:
        osszegzes()
    elif fuggveny == 2:
        eldontes()
    elif fuggveny == 3:
        kereses()
    elif fuggveny == 4:
        kivalasztas()
    elif fuggveny == 5:
        szamlalas()
    elif fuggveny == 6:
        szelso_ertekek()
    elif fuggveny == 0:
        print("A program vége!!")
        break
