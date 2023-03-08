#Lapostyán Martin, B.csoport, 10.C, 2.csoport 2023.03.08

szam_sororzat = [15,4,5,19,2]

def main(szam_lista):
    min = szam_lista[0]
    max = szam_lista[0]
    for szam in szam_lista:
        if szam < min:
            min = szam
        elif szam > max:
            max = szam
    print(f"A legkisebb szám a listában: {min}")
    #Plus Feladat
    print(f"A legnagyobb szám a listában: {max}")

main(szam_sororzat)