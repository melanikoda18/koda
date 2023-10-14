respuesta="S"
while respuesta =="S":# while significa mientras 
    p=int(input(" 1)cono (2500)\n 2)vaso (3000)\n 3)ensalada de frutas (5000)\n selecciona una opcion:  "))
    c=int(input("cantidad de pedidos: "))
    if p==1:
        total=c*2500
        if c==1:
            print(f"el total a pagar por {c} cono es: ({total}) ")
        else:
            print(f"el total a pagar por {c} conos es: ({total}) ")    
    elif p==2:
        total=c*3000
        if c==1:
            print(f"el total a pagar por {c} voso es: ({total}) ")
        else: 
            print(f"el total a pagar por {c} vasos es: ({total}) ")
    elif p==3:
        total=c*5000
        if c==1:
            print(f"el total a pagar por {c} ensalada de frutas es: ({total}) ")
        else:
            print(f"el total a pagar por {c} ensaladas de frutas es: ({total}) ") 
    respuesta=input("hay mas clientes? S/N: ").upper()
print("se acabo el bucle")