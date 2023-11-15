lista=[]
for i in range(1,10,1):
    print(i)
    if i%3==0:
        lista.append(i)
print(lista)
for j in range(len(lista)):
    print(f"eliminado: {lista.pop()}")#elimina lo q esta en el final de la lista
print(lista)       