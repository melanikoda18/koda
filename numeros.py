lista=[]
for i in range(1,10,1):
    print(i)
    if i%3==0:# esto es para cual numero es multiplo al numero q pongamos 
        lista.append(i)# sirve para guardar algo al final de la lista
print(lista)
#for j in range(len(lista)):
print(f"eliminado: {lista.pop()}")#elimina lo q esta en el final de la lista
print(lista)       