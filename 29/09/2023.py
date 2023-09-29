#import math
#print(round(7.199999))
N=input("Ingrese un nombre: ")
A=input("Ingrese un apellido: ").capitalize()
E=int(input("Ingresa tu edad:  ")) 
C=input("ingresa tu plato favorito: ").capitalize()
if len(N)>=20:
    print("Que Nombre Tan Largo")
elif len(N) <5:
    print("Que Nombre Tan Corto")
if A=="Gonzalez":
    print("Como speedy Gonzalez ")
if C=="Pizza":
    print("Kawabonga")
if E>=18 and E<=30:
    print("Perteneces al jas")
elif E<18:
    print("Perteneces a los jovenes")