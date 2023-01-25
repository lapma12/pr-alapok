def koszont():
	print('Üdv a fedélzeten!')

koszont()

def koszont_nevvel(nev):
	print('Szia '+ nev +', üdv a fedélzeten!')

koszont_nevvel('Ádám')


def koszont_ket_nevvel(nev1, nev2):
	print('Szia '+ nev1 + ', ' + nev2 +'!\nÜdv a fedélzeten!')

koszont_ket_nevvel('Nóra', 'Ádám')


def koszont_ket_nevvel(nev1, nev2):
	print('Szia '+ nev1 + ', ' + nev2 +'!\nÜdv a fedélzeten!')

koszont_ket_nevvel('Nóra', 'Ádám')


def osszegzo(list):
	osszesen = 0
	for szam in list:
		osszesen = osszesen + szam
	print('A listában lévő számok összege: ', osszesen)


szamok = [3, 5, 19, 11, 17, 1]
osszegzo(szamok)
    

'''
Változók hatóköre: globális és lokális változók
'''
def kepernyore_ir():
    lokalis_valtozo = 'alma'
    print(lokalis_valtozo)
    print(globalis_valtozo)
  
  
globalis_valtozo = 'gyümölcs'
kepernyore_ir()
  
print(globalis_valtozo)
    # a lokalis_valtozo az eljáráson KÍVŰL nem elérhető !!! # hibát eredményez !!!
    

    # Függvény definíciója
def festek_kalkulator(x, y):
    t = x * y
    l = t * 0.13
    return l


    # Függvény hívása
liter = festek_kalkulator(5, 2)

    # A függvény hívása lehet egy kifejezés része is
ar = festek_kalkulator(5, 2) * 700

  
    
    
    
  
  

  

  