#lista=["-42","26","-11","-1","0","-111"]
#lista=["melani","gato","lentes","cilla"]
lista = []
rep= "S"
while rep== "S":
    var=input("ingrese una palabra: ").capitalize()
    lista.append(var)
    rep=input("S/N:").upper()
lista.sort()
for i in range (len(lista)):
    print(f"Elemento {i+1}: {lista[i]}")
print(f"maxi: {max(lista)} mini: {min(lista)}")