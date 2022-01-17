#8.1
#*
total = 0
monto = float(input("Monto de una venta: $"))
while monto != 0:
    if monto < 0:
        print("Monto no válido")
    else:
        total += monto
    monto = float(input("Monto de una venta: $"))
if total > 1000:
    total-= total*0.1
print("Monto total a pagar: $", total)
#**
totalPares = 0
totalImpares = 0 
numero = int(input("Número: "))
while numero != 0:
    pares = 0
    impares = 0
    while numero != 0:
        ultimoDigito = numero % 10
        if ultimoDigito % 2 == 0:
            pares += 1
            totalPares += 1
        else: 
            impares += 1
            totalImpares += 1
        numero = numero // 10
    print("El número ingresado tiene", pares,"digitos pares y",impares,"digitos impares")
    numero = int(input("Número: "))
print("Total de digitos pares: ",totalPares)
print("Total de digitos impares:",totalImpares)
#***
digitosEnLaLinea = 0
cantLineas = 0
titulo = input("Título del libro: ")
while titulo != "*":
    if titulo == "/":
        cantLineas += 1
        print("Linea completa. Aparecen", digitosEnLaLinea, "digitos")
        digitosEnLaLinea = 0
    else:
        for caracter in titulo:
            if caracter in "0123456789":
                digitosEnLaLinea += 1
    titulo = input("Título del libro: ")
print("Fin. Se leyeron", cantLineas, "linas")
