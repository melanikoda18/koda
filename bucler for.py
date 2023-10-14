#for i in range (10): # se repite siempre como un bucler 
   #print(f"vuelta #: {i+1}")
   #print(f"el valor de i es: {i} ")
   # print("--------------------------------------")
for i in range(10):
    c=int(input("ingrese su numero de cedula: "))
    if  c%2==1:
        print(f"la cedula del {i+1} es: impar ")
    else:
        print(f"la cedula del {i+1} es: par ") 