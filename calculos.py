import math
#radio=float(input("ingrese el numero de radio del circulo: "))
#a=math.pi*radio**2
#print(f"resultado del area: {a}")

#lado=int(input("ingresa la medida de un lado del cubo: "))#float/int=para convertir texto a numero
#volumen=lado**3#                                             float:convierte texto a numeros incluyendo los decimales
#print (f"el volumen del cubo es: {volumen} ")#               int:para numeros completos (olvida los decimales)
 
#a=float(input("imgrese el lado a:  "))
#b=float(input("ingrese el lado b:  "))
#perimetro=2*(a+b)
#print(f"el perimetro del terreno es: {perimetro} ")

#h=float(input("cual es la altura del cilindro: "))
#r=float(input("cual es el radio del cilindro:  "))
#v=math.pi*r**2*h
#print(f"el volumen del tanque es: {v} ")

#B=float(input("ingrese el valor de base mayor:  " ))
#b=float(input("ingrese el valor de base menor: ")) 
#h=float(input("ingrese el valor de la altura: "))
#A=(B+b)*h/2 
#print(f"el valor del area es: {A}  ")

#x=3*((3+3)/3-3)*3
#print(f" el valor de  x es: {x}")

r=float(input("ingrese el radio del cilindro:  ")) 
h=float(input("ingrese la altura del cilindro: "))
A=2*math.pi*r*(h+r)
print(f"el valor de la superficie es: {round(A,2)} ")#round sirve para poner los decimales q tu quieras 