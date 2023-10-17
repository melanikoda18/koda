cont=0
resp="S"
while resp=="S": # el while no se sabe las repeticiones 
    resp= input("repetir ciclo? S/N: ").upper() 
    cont +=1

print(f"el ciclo se repitio {cont} veces ")