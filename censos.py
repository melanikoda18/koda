promedios=0
CI_impar=0
CI_pares=0
cant_personas=0
resp="S"
while resp=="S":
    CI=int(input("ingrese su cedula: "))
    edad=int(input("ingrese su edad: "))
    resp= input("hay mas personas S/N ").upper()
    cant_personas=cant_personas+1
    promedios=promedios+edad
    if CI%2==1:#es impar por q lo estamos dividiendo entre dos 2
        CI_impar+=1
    else:
        CI_pares+=1
D=promedios / cant_personas
print(f"cantidad de personas: {cant_personas} ")
print(f"el promedios es: {D}")
print(f"cantidad de CI impares {CI_impar}")
print(f"cantidad de CI pares {CI_pares}")