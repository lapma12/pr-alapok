# Megnyitási módok:
# r: olvasás 
# w: írás, fájlt hoz létre; ha léztezik ilyen nevű fájl már, felülírja az eredetit
# x: írás, fájlt hoz létre; ha léztezik ilyen nevű fájl már, hibát ad 
# a: a létező fájl végére hozzáfűz, ha még nem létezik ilyen nevű, akkor létrehozza
# a+: hozzáfűzést és olvasást is lehetővé tesz

with open('./adatok/kimenet.txt', 'w', encoding='utf-8') as celfajl:
    print('Ez kerül a fájlba...', file=celfajl)  

with open('./adatok/kimenet.txt', 'w', encoding='utf-8') as celfajl:
    # sztringet ír a fájlba
    celfajl.write('alma, körte, eper')

    # lista elemeit írja a fájlba
    celfajl.writelines(['alma\n', 'körte\n', 'eper\n'])

with open('./adatok/gyumolcsok.txt', 'r', encoding='utf-8') as forrasfajl, \
        open('./adatok/gyumolcsok_masolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            print(sor.strip(), file=celfajl)
  
with open('./adatok/gyumolcsok.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('./adatok/gyumolcsok_masolat.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(forrasfajl.read())