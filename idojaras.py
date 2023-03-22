#Napi hőméréklet maximum, minumum Március 22-től Április 20-ig,Helyíség Emőd 
#A program globális változói
napi_maximum = [14,17,21,15,16,13,8,11,12,14,16,16,14,15,13,14,16,16,14,12,12,10,11,13,15,17,19,17,19,20]

napi_minumum = [8,8,9,6,7,1,0,2,3,5,4,4,3,5,4,6,8,6,4,2,1,-1,-1,1,3,5,7,5,7,9]

napi_minumum_darab = None
napi_maximum_darab = None

harmincnapos_napi_atlag = []

#1. Feladat

def megszamlalas_max(napi_max):
    darab = 0
    for szam in napi_max:
        darab +=  1
        napi_maximum_darab = darab
    return darab

print(f"Maximum hőmésékletek elmszáma: {megszamlalas_max(napi_maximum)} ")

def megszamlalas_min(napi_min):
    darab = 0
    for szam in napi_min:
        darab +=  1
        napi_minumum_darab = darab
    return darab

print(f"Minimum hőmésékletek elmszáma: {megszamlalas_max(napi_minumum)} ")

#2. Feldat
def atlag_max(napi_max):
    lista_eleminek_osszege = 0
    for szam in napi_max:
        lista_eleminek_osszege = lista_eleminek_osszege + szam
    atlag = lista_eleminek_osszege / len(napi_max)    
    return atlag
    

print(f"Maximum hőmésékletek átlaga: {atlag_max(napi_maximum):.2f} ")


def atlag_min(napi_min):
    lista_eleminek_osszege = 0
    for szam in napi_min:
        lista_eleminek_osszege = lista_eleminek_osszege + szam
    atlag = lista_eleminek_osszege / len(napi_min)    
    return atlag
    

print(f"Minimium hőmésékletek átlaga: {atlag_min(napi_minumum):.2f} ")

#3.Feledat, 30 napos átlag hőmérséklet
#3.a megoldás

print(f"A 30 napos átlag hőmérséklet éréke : {(atlag_max(napi_maximum) + atlag_min(napi_minumum)) / 2:.2f}")

#3.b Feledat Számítsuk ki a napi átlag hőmérsékltet és tároljuk egy harmincnapos_napi_atlag listában

def harminc_napi_atlag(atlag_maximum,altag_minimum):
    for i in range(len(napi_maximum)):
        napi_atlag = (atlag_maximum[i] + atlag_minimum[i]) / 2
        harmincnapos_napi_atlag.append(napi_atlag)






