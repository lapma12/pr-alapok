import fuggvenyek
numbers = []
for szamok in range(10):
    random_szam = fuggvenyek.szamgenerator()
    numbers.append(random_szam)
#Számok generálása és listába helyezése

paratlan_szam = 0
paros_szam = 0
for szam in numbers:
    if fuggvenyek.paros_szam(szam):
        paros_szam += 1
    else:
        paratlan_szam += 1
#For ciklussal végig futunk a listán és megszámoljuk mennyi páros és páratlan szám van

with open("kiir.txt" ,'w',encoding="UTF-8") as celfalj:
    print(f"A lista {paros_szam} páros és {paratlan_szam} páratlan számot tartalmaz.",file=celfalj)
#Beírjuk egy fájba a megkapodt eredményeket 
