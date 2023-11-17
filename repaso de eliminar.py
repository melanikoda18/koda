var=0
resp="S"
lista=["melani","casa","mesa","lima","sapo","telefono","carro","libro"]
while resp=="S":
    print(lista)#nos muestra la lista 
    var=int(input("selecciona la posicion del elemento que quiera eliminar: "))
    koda=lista.pop(var)#pop sirve para eliminar cosas de la lista
    print(f"se ha eliminado {koda}")
    resp= input("repetir ciclo? S/N: ").upper() 
