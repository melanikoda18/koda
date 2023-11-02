#maxi=float("-inf")
#mini=float("inf")
l=[42,26,11,1,0,100]#la lista
largo= len(l)#buscar el largo de la lista
l.sort()#acomodar las lista de mayor a menor
for i in range (largo):#forma de recorrer la lista
    print(f"elemento {i+1}: {l[i]}")# motrar le la lista al usuario de forma ordenada
print(f"las cantadad de numeros es:{len(l)}")#muetra la cantidad de elementos de la lista
print(f"maxi: {max(l)} mini: {min(l)} ")#muestra el maximo y el minimo de la lista

