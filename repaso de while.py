resp="S"
while resp=="S":
    CI=int(input("ingrese su CI:  ")) 
    if CI%2==1:
        print("su cedula es impar ")
    elif CI%2==0:
        print("su CI es par") 
    resp=input("continuar?  S/N ").upper()
        