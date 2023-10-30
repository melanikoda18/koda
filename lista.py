maxi=float("-inf")
mini=float("inf")
l=[99,100,33,22,-1,400,0]
largo= len(l)
l.sort()#ordena de mayor a menor sobre numeros y alfabeticamente sobre palabras
for i in range(largo):
    if maxi<l[i]:#forma larga de buscar el valor maxino y minimo 
        maxi=l[i]
    if mini>l[i]:
        mini=l[i]    
print(f"valor maximo: {maxi} ")
print(f"valor minimo: {mini} ")
print(f"forma corta: valor maxino {max(l)} valor minimo {min(l)} ")#forma corta de buscar los valores minimo y maximo