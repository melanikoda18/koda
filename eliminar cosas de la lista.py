cont=0
lista=["melani","casa","mesa","lima","sapo","telefono","carro","libro"]
for i in range (len(lista)):
    if len(lista[i])>5:
        cont +=1
print(f"encontramos {cont} palabras con mas de 5 letras")