#10.1
#*
def validar(email):
    caracterBuscado = "@"
    emailValido = False
    for c in email:
        if c == caracterBuscado:
            emailValido = True
            break
    return emailValido

direccion = input("Tu email: ")
if validar(direccion):
    print("Dirección válida")
else:
    print("Dirección inválida")
#**
def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

num = int(input("Número a procesar: "))
while num != 0:
    print("Suma:",sumaDigitos(num))
    num = int(input("Número a procesar: "))
#***
def sumaDigitos(numero):
    suma = 0
    while numero != 0:
        digito  = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma

sumatoria = 0 
num = int(input("Número a procesar: "))
while num != 0:
    print("Suma:",sumaDigitos(num))
    sumatoria = sumatoria + num
    num = int(input("Número a procesar: "))
print("Sumatoria:",sumatoria)
print("Dígitos:",sumaDigitos(sumatoria))
#****
def primo(num):
        for i in range(2,num):
           if num%i==0:
               return False
        return True

def frecuencia(numero,digito):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       if ultDigito==digito:
           cantidad+=1
       numero=numero//10
   return cantidad

def factorial(numero):
    f=1
    if numero!=0:
        for i in range(1,numero+1):
            f=f*i
    return f

def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

mayor=0
numero=int(input("Número primo: "))
while primo(numero):
    print("Suma de los dígitos:",sumaDigitos(numero))
    digito=int(input("Dígito: "))
    print("El",digito,"aparece",frecuencia(numero,digito),"veces")
    if numero > mayor:
        mayor=numero
    numero=int(input("Número primo: "))
print("Factorial de",mayor,":",factorial(mayor))