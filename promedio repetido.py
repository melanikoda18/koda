sum_notas=0
cant_notas=0
prom=0
for _ in range(2):#se repite el programa cuantas veces le pongas  
    n=input("ingrese su nombre: ")
    c=(input("ingrese su cedula: "))
    p=float(input("ingrese su promedio: "))
    cant_notas=cant_notas+1
    sum_notas=sum_notas+p
    p=round(p,0)
    if p>=80:
        print(f"{n},{c} has aprobado ")
    elif p<80:
        print(f"{n},{c} has reprobado ")
prom= round(sum_notas/cant_notas,0)
print(f"el promedio general de los estudiantes es {prom}")