# Solicita al usuario que ingrese un nombre y lo guarda en la variable 'nombre'.
# Convierte la primera letra del nombre en mayúscula para que sea más legible.
nombre = input("Ingresa un nombre: ").title()

# Solicita al usuario que ingrese un primer verbo y lo guarda en la variable 'verbo1'.
# Convierte el verbo en minúsculas para asegurarse de que esté en el mismo formato.
verbo1 = input("Me puedes dar un verbo: ").lower()

# Solicita al usuario que ingrese un segundo verbo y lo guarda en la variable 'verbo2'.
# Convierte el verbo en minúsculas para que coincida con el formato del verbo1.
verbo2 = input("Me puedes dar otro verbo: ").lower()

# Solicita al usuario que ingrese un adjetivo y lo guarda en la variable 'adjetivo'.
# Convierte el adjetivo en mayúsculas para que sea más llamativo en el resultado final.
adjetivo = input("Ingresa un adjetivo: ").upper()

# Imprime una línea de guiones para separar los datos ingresados de la historia.
print("-----------------------------------------------------------------------")

# Imprime los datos ingresados por el usuario.
print(f"Nombre: {nombre}")
print(f"Verbo1: {verbo1}")
print(f"Verbo2: {verbo2}")
print(f"Adjetivo: {adjetivo}")

# Crea y muestra una historia personalizada utilizando los datos ingresados.
print(f"{nombre} se fue de paseo y se encontró un sendero misterioso en el bosque. {nombre} {verbo1} con curiosidad y {verbo2} una puerta antigua. Al entrar, quedó sorprendido al ver un jardín encantado, lleno de flores brillantes y árboles imponentes. {nombre} se sintió {adjetivo} y pasó horas explorando aquel lugar mágico.")
