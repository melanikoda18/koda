e=int(input("Ingrese su edad: "))
c=input("Tienes un codigo de recomendacion ingresalo: ").upper()
if c=="XIA-097":
    print("Tu beca es de 2.000.000 pesos")        
elif e>=12 and e<=14:
    print("Tu beca es de 1.000.000 pesos")
elif e>=15 and e<=17:
    print("Tu beca es de 800.000 pesos")
elif e>=18 and e <=20:
    print("Tu beca es de 600.000 pesos")
elif e>=21:
    print("Tu beca es de 400.000 pesos")