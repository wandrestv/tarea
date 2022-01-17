#3.1
#*
print(not True)
#**
print(not(1+2 !=3))
#***
x=(len("jugar")>5) and (len("jugar")<10)
print(x)
#****
print("alto"[2]=="t" and x)
#*****
print(842913%10 != 3 and len("café")==3)
#******
print(0 != 0 or "a" < "y")
#*******
print(True or int("50") >= 50)
#********
edad=20
print(not(x) or edad %2==0)
#*********
es_cliente = False
print(not (es_cliente and not (edad <18)))
#**********
num = int(input("Ingrese un número, no puede ser menor que 0 ni mayor que 100"))
if num >= 0 and num <= 100:
    print("Excelente")
else:
    print("Número incorrecto")
#***********
eda = int(input("Ingrese una edad, debe estar entre 10 y 20"))
if eda > 10 and edad < 20:
    print("Excelente")
else:
    print("Edad incorrecta")
#*************
cadena = input("Ingrese una frase, no sobrepase los 10 caracteres (se cuentan los espacios)")
if len(cadena) <= 10:
    print("Excelente")
else:
    print("La frase contiene más de 10 caracteres")
#***************
nume = int(input("Ingrese un número"))
if nume % 4 == 0 and nume < 0:
    print("El numero es múltiplo de 4 y también es negativo")
else:
    print("El numero no es múltiplo de 4")
#*****************
kilometraje = int(input("Ingrese el kilometraje del vehículo"))
modelo = int(input("Ingrese el año del modelo"))
if kilometraje < 30000 and (modelo>=15 and modelo <=2017):
    print("Listo para la compra")
else:
    print("No cumple con las condiciones para la compra")
#******************
porcentaje = int(input("Ingrese la cantidad de estudios completos (en una escala del 1 al 100)"))
magrupacion = input("¿Es miembro de alguna otra agrupación académica? (Si o No)")
if magrupacion == "Si" or magrupacion == "si":
    agrupacion = True
else:
    agrupacion = False

if porcentaje > 30 and not (agrupacion):
    print("Aceptado")
else:
    print("Denegado")
#*********************
es_invierno = True
tiene_calefacción = False
está_abrigada = False
es_invierno and not tiene_calefacción and not está_abrigada
es_invierno and not (tiene_calefacción or está_abrigada)