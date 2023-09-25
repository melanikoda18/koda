n=float(input("ingrese primera nota:  "))#pido la nota al usuario
n1=float(input("ingrese la segunda nota: "))
n2=float(input("ingrese la tercera nota: "))
p=(n+n1+n2)/3#calculo las notas 
p=round(p)#le quito los decimales 
print(f"su nota es: {p}  ")#imprimo el resultado
if p >10:# si p es mayor a 10 me da el resultado de abajo q seria ¡aprobaste! 
    print("¡aprobaste!") 
elif p ==10:#si por el contrario el valor es igual a 10 entonces me da el resultado de abajo q es "suertudo,aprobaste"
    print("suertudo,aprobaste.")
else:
    print("reprobaste ")