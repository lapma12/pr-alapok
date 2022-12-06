#Python lista
lista = ["alma","banán","cseresznye"]
print(lista)

#---------------------------------------

lista = ["alma","banán","cseresznye","alma","banán"]
print(lista)

#---------------------------------------

lista = ["alma","banán","cseresznye"]
print(len(lista))

#---------------------------------------

lista1 = ["alma","banán","cseresznye"]
lista2 = [1,5,7,9,3]
lista3 = [True , False , False]

#---------------------------------------

lista = ["abc",34,True,40,"férfi"]
print(lista)

#---------------------------------------

lista = ["alma","banán","cseresznye"]
print(type(lista)

#------------------------------------

lista = list(("alma","banán","cseresznye"))
print(lista)

#------------------------------------

lista = ["alma","banán","cseresznye"]
print(lista[1])

#-------------------------------------

lista = ["alma","banán","cseresznye"]
print(lista[-1])

#-------------------------------------

lista = ["alma-0","banán-1","cseresznye-2","narancs-3","kivi-4","szőlő-5","mangó-6"]
print(lista[2:5])
print(lista[1:6])

#------------------------------------

lista = ["alma-0","banán-1","cseresznye-2","narancs-3","kivi-4","szőlő-5","mangó-6"]
print(list[-4:-1])

#-----------------------------------

lista = ["alma-0","banán-1","cseresznye-2","narancs-3","kivi-4","szőlő-5","mangó-6"]
if "banán-1" not in lista:
    print("Igen a banán-1 elem nem szerepel a lista nevü listába")

#-----------------------------------

lista = ["alma","banán","cseresznye"]
lista[1]= "kivi"
print(lista)

#-------------------------------------

lista = ["alma-0","banán-1","cseresznye-2","narancs-3","kivi-4","szőlő-5","mangó-6"]
lista[1:3] = ["körte","szilva"]
print(lista)

#-----------------------------------

lista = ["alma-0","banán-1","cseresznye-2","narancs-3","kivi-4","szőlő-5","mangó-6"]
lista[1:2] = ["körte","szilva"]
print(lista)

#-------------------------------------

lista = ["alma-0","banán-1","cseresznye-2","narancs-3","kivi-4","szőlő-5","mangó-6"]
lista[1:3] = ["körte","szilva"]
print(lista)

#--------------------------------------

lista = ["alma-0","banán-1","cseresznye-2","narancs-3","kivi-4","szőlő-5","mangó-6"]
lista.insert(2,"körte")
print(lista)

#-------------------------------------

lista = ["alma-0","banán-1","cseresznye-2","narancs-3","kivi-4","szőlő-5","mangó-6"]
lista.append("körte")
print(lista)
