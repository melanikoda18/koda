nombre=input("ingrese su nombre ").title()# el title sirve para poner la primera letra de cada palabra en mayuscula 
apellido=input("ingrese su apellido  ").upper() # el upper sirve para poner todas la frace en mayuscula 
cargo=input("imgrese su cargo en la empresa  ").title()
correo=input("ingrese su correo ").lower() #el lower sirve para poner toda la oracion  en  minuscula
ID=input(" ingrese su cedula ")
edad=input("edad ")
print("---------------------------------------")

print(f"{apellido}, {nombre}")
print(f"{cargo}, {edad}")
print(correo)
print()
print(ID+"-"+ str (len(ID))) # el str sirve para tranformar una variable o un numero  en "texto" y el len para indicar el largo de algo 
print("-----------------------------------------------")

print(f"Apellido: {str(len(apellido))}  caracteres  ")# str (len(apellido))
print(f"Nombre: {str(len(nombre))}  caracteres")
print(f"Cargo: {str(len(cargo))}  caracteres")
print(f"Correo: {str(len(correo))}  caracteres")
print("----------------------------------------------------------------")