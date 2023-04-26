#fájl megnyitása
forrasfajl = open("szoveg.txt")

#fájl objektum bejárása
"""
for sor in forrasfajl:
    print(sor)
forrasfajl.close()

print("-----------------------------------")


with open("szoveg.txt" ,"r",encoding="utf-8") as forrasfajl:
    for sor in forrasfajl:
        sor = sor.strip() #megtisztítom sor a végét
        print(sor)
print()
print("-----------------------------------")
"""

with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
        print('Ez kerül a fájlba...', file=celfajl)  
with open('kimenet.txt', 'w', encoding='utf-8') as celfajl:
        print('Ez kerül a fájlba >>> kimenet.txt', file=celfajl)