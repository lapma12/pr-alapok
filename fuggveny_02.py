#Olyan karakterláncot ad vissza, amelyben minden karakter kisbetű.
#lower()
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#Olyan karakterláncot ad vissza, amelyben minden karakter nagybetű.
#upper()
txt = "Hello my friends"
x = txt.upper()
print(x)

#Átkonvertálja az első karaktert nagy betűre az szövegben
#capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

#A metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel végződik, ellenkező esetben False-t
#endswith()
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

#Megekersi az éréket a szövegben és vissza adja hol találta 
#find()
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

#A metódus igaz értéket ad vissza, ha az összes karakter alfanumerikus, azaz ábécé betűi (az) és számok (0-9)
#isalnum()
txt = "Company12"
x = txt.isalnum()
print(x)

#A metódus igaz értéket ad vissza, ha az összes karakter ábécé betűje (az)
#isalpha()
txt = "CompanyX"
x = txt.isalpha()
print(x)

#A metódus igaz értéket ad vissza, ha minden karakter kisbetűvel van írva, ellenkező esetben False-t
#islower()
txt = "hello world!"
x = txt.islower()
print(x)

#A metódus az összes elemet iterálhatóvá teszi, és egyetlen karakterláncba egyesíti
#join()
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

#A metódus lecserél egy megadott kifejezést egy másik megadott kifejezésre
#replace()
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#A metódus megkeresi a megadott érték utolsó előfordulását
#rfind()
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

#A metódus eltávolítja a záró karaktereket (a karakterlánc végén lévő karaktereket), a szóköz az alapértelmezett eltávolítandó karakter
#rstrip()
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")


#A metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel kezdődik, ellenkező esetben False-t
#startswith()
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

#A metódus eltávolítja a kezdő (szóköz az elején) és a záró (szóköz a végén) karaktereket (a szóköz az eltávolítandó alapértelmezett kezdő karakter)
#strip()
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#A metódus egy karakterláncot ad vissza, ahol az összes nagybetű kisbetű, és fordítva
#swapcase
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#A metódus egy karakterláncot ad vissza, ahol minden szó első karaktere nagybetű. Mint egy fejléc vagy egy cím.
#Ha a szó számot vagy szimbólumot tartalmaz, az utána lévő első betű nagybetűvé alakul.
#title()
txt = "Welcome to my world"
x = txt.title()
print(x)

#A metódus középre igazítja a karakterláncot, és egy megadott karaktert használ (a szóköz az alapértelmezett) kitöltési karakterként
#center()
txt = "banana"
x = txt.center(20)
print(x)