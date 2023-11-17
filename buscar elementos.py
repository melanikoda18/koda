lista=[31329488,24355644,13456789,16094971,14687906,]
resp="S"
var=0
while resp=="S":
    var=int(input("ingrese la CI que quiera consultar: "))
    if var in lista:
        print ("usuario registrado")
    else :
        print("usuario no registrado")    
    resp=input("repetir ciclo S/N : ").upper()
