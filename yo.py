dd=int(input("Dia de nacimiento: "))
mm=int(input("Mes de nacimiento: "))
aa=int(input("Año de nacimiento: "))
e=2023-aa
if    10>mm:
    print(f"su edad es: {e}")
elif 10==mm:
    if 11>=dd:
        print(f"su edad es: {e}")
    elif 11<dd:
        print(f"su edad es: {e-1}")
elif 10<mm:
    print(f"su edad es: {e-1}")
    