import random

def Feladat1():
    numbers = []
    for i in range(5):
        veletlen = random.randint(1, 10)
        numbers.append(veletlen)

    print(f"A lista elemei: {numbers} ")
    osszeg = 0
    for szam in numbers:
        if szam % 2 == 0:
            osszeg += szam
    print(f"A páros számok összege: {osszeg} ")
#Feladat1()


lista = []
def Feladat2():
    osszeg = 0
    valid_input = True
    while valid_input:
        szam = int(input("Adj meg egy számot -5;5 intervallumból: "))
        if szam >= -5 and szam <= 5:
            lista.append(szam)
            osszeg += szam
        else:
            valid_input = False

    print(f"A lista elemei: {lista}")
    print(f"Az összegük:  {osszeg} ")
#Feladat2()


def Feladat3():
    szavak = ["Alma", "banán", "Ananász", "narancs", "eper"]

    szamlalo = 0
    print("Azok a szavak amelyek A és a betűvel kezdődnek:")
    for szo in szavak:
        if szo[0] == 'A' or szo[0] == 'a':
            print(szo)
            szamlalo += 1

    print(f"Az 'A' vagy 'a' betűvel kezdődő szavak száma: {szamlalo}")

#Feladat3()


