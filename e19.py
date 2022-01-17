#12.1
#*
def cargarNombres(alumnos):
    nombre=input("Nombre: ")
    while nombre!="x":
        alumnos.add(nombre)
        nombre=input("Nombre: ")
    return alumnos

primaria=set()
secundaria=set()
print("ALUMNOS DE PRIMARIA")
primaria=cargarNombres(primaria)
print("ALUMNOS DE SECUNDARIA")
secundaria=cargarNombres(secundaria)

print("NOMBRES DE TODOS LOS ALUMNOS:")
for nombre in primaria|secundaria:
    print(nombre)

print("NOMBRES COMUNES:")
for nombre in primaria&secundaria:
    print(nombre)

print("NOMBRES DE PRIMARIA QUE NO SE REPITEN EN SECUNDARIA:")
for nombre in primaria-secundaria:
    print(nombre)
#**
def direcciones(ventas):
    domicilios=set()
    for venta in ventas:
        domicilios.add(venta[3])
    return domicilios