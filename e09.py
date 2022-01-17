#7.1
#*
total = 0
for i in range(101):
    if i % 3 == 0:
        total += i
print("Sumatoria:", total)
#**
numero = int(input("Número: "))
f = 1
if numero != 0:
    for i in range(1, numero+1):
        f = f * i
print("Factorial:", f)
#***
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(8):
    n3 = n1 + n2
    print(n3)
    n1 = n2
    n2 = n3
#****
sumaNegativos = 0
sumaPositivos = 0
cantidadPositivos = 0
for i in range(6):
    nro = int(input("Número: "))
    if nro >= 0: 
        cantidadPositivos += 1
        sumaPositivos += nro
    else:
        sumaNegativos += nro
print("Sumatoria de negativos: ", sumaNegativos)
if cantidadPositivos != 0:
    print("Promedio de positivos: ", sumaPositivos/cantidadPositivos)
else: 
    print("No se ingresaron números positivos")