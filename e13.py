#9.1
#*
cantidad = 0
n = int(input("Número: "))
while n != 0:
    primo = True
    for i in range(2,n):
        if n % i == 0:
            primo = False
            break
    if primo:
        cantidad += 1
    n = int(input("Número: "))
print("Primos: ",cantidad)
#**
anioInicio = int(input("Año inicial: "))
anioFin = int(input("Año final: "))
for anio in range(anioInicio, anioFin + 1):
    if not anio % 10 == 0:
        continue
    if not anio % 4 == 0:
        continue
    if anio % 100 != 0 or anio % 400 == 0:
        print(anio)