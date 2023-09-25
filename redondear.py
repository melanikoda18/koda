import math
x=2.7
y=2.7
z=2.7
print(int(x),int(y),int(z))#lo redondea el numero al piso como floor
print(round(x),round(y),round(z))#lo reondea al numero del decimal ejemplo: 2.7 da 3
print(math.ceil(x),math.ceil(y),math.ceil(z))#ciel redondea el numero al mayor al techo. Ejemplo:2.7 pasa a ser 3 
print(math.floor(x),math.floor(y),math.floor(z))#floor redondea el numero al piso. Ejemplo:2.7 pasa a ser 2 no toma en cuenta los decimal
print(round(5.498,2))#