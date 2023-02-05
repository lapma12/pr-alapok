#FELADAT 1

lista = []
szam = input("Kérek egy számot (X vagy x-et a kilépéshez): ")

while szam.lower() != "x" or szam.upper() != "X":
    lista.append(int(szam))
    szam = input("Kérek egy számot (X vagy x-et a kilépéshez): ")

valtozo = [x for x in lista if x % 2 == 0]

print(f"A lista elemei: {lista}")
print(f"A lista legkisebb páros  eleme: " ,min(valtozo) if valtozo else "Nincs legkisebb páros szám")
print(f"A lista legnagyobb páros eleme: " ,max(valtozo) if valtozo else "Nincs legnagyobb páros szám")
print("Vége")
"""

#FELADAT 2
words = []
word = input("Adj meg egy szót: ")

while word:
    words.append(word)
    word = input("Adj meg egy szót: ")

print("A megadott szavak:", words)
print("A legrövidebb szó:", min(words, key=len))
print("A leghosszabb szó:", max(words, key=len))
"""