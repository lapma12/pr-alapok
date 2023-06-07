import random
def szamgenerator():
    random_szam =  random.randint(1,100)
    return random_szam
def paros_szam(par1):  
    if par1 % 2 == 0:
        return True
    else:
        return False