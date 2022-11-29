"""
szoveg = "Hello világ!"
hossz = len(szoveg)
for karakter in range(hossz):
    print(karakter)

print()

for szam in range(50,101,3):
    print(szam,end=" ")

print()

for szam in range(50,101,3):
    if szam % 2 == 0:
        print(szam,end=" ")

print()

for szam in range(50,101,3):
    if szam % 2 == 1:
        print(szam,end=" ")"""
"""
nev = input("Kérem a nevedet: ")
for karakter in nev:
    print(karakter.upper(),end ="")

print()"""

space = False
nev_kicsi = ""
nev = input("Kérem a nevedet: ")
for karakter in nev:
    nev_kicsi = nev_kicsi + karakter.lower()
print(nev_kicsi)

szamlalo = 0
for karakter2 in range(len(nev_kicsi)):
    if szamlalo == 0:
        print(nev_kicsi[szamlalo].upper(),end="")
        
    else:
        if space:
            print(nev_kicsi[szamlalo].upper(),end="")
            space = False
        else:
            print(nev_kicsi[szamlalo],end ="")
        
    
    if nev_kicsi[szamlalo] == " ":
        space = True
    szamlalo += 1