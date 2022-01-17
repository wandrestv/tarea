#5.1
#*
nombre = "Andres"
print(nombre, "¿Cuál es tu edad?")
A = input
#**
precio = float(input("Precio: "))
total = precio + (precio * 0.10)
print("El precio total es: ",total)
#***
edad = int(input("Edad: "))
print("Tu edad es: ",edad)
#****
edad = int(input("Edad: "))
print("Veamos si tu edad es 18...",edad==18)
#*****
N = input("Ingrese su nombre: ")
print("Ahora estás en la matrix,",N)
#******
precio_cena = float(input("Ingrese el costo de la cena: $"))
precio_cenat = precio_cena + (precio_cena * 0.062) + (precio_cena * 0.1)
print("Costo total de la cena es: $",precio_cenat)
#*******
dia = int(input("Día de tu nacimiento: "))
mes = int(input("Mes de tu nacimiento: "))
anio = int(input("Año de tu nacimiento: "))
print(dia,"/",mes,"/",anio)

dia2 = input("Día de tu nacimiento: ")
mes2 = input("Mes de tu nacimiento: ")
anio2 = input("Año de tu nacimiento: ")
print(dia2+"/"+mes2+"/"+anio2)

fecha=int(input("Fecha de nacimiento en formato DDMMAAAA: "))
fanio = fecha % 10000
fdia = fecha // 1000000
fmes = (fecha // 10000) % 100
print(fdia,"/",fmes,"/",fanio)

fecha2=input("Fecha de nacimiento en formato DDMMAAAA: ")
f2dia = fecha2[:2]
f2mes = fecha2[2:4]
f2anio = fecha2[4:]
print(f2dia+"/"+f2mes+"/"+f2anio)

#*******
capacidad = float(input("Capacidad del tanque: "))
km_l = float(input("Rendimiento (Km por litro): "))
recorrido = float(input("Km totales a recorrer: "))
print("Seran necesarios", recorrido / (capacidad*km_l),"tanques")
