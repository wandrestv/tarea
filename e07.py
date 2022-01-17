#6.1
#*
numero = int(input("Número: "))
if numero < 0: 
    numero = numero*-1
print ("El valor absoluto es", numero)
#**
nombre1 = input("Un nombre: ")
nombre2 = input("Otro nombre: ")
indice_final_n1 = len(nombre1)-1
indice_final_n2 = len(nombre2)-1
if nombre1[0] == nombre2[0] or nombre1[indice_final_n1] == nombre2[indice_final_n2]:
    print("Coincidencia")
else: 
    print("No hay coincidencia")
#***
candidato = input("Candidato elegido: ")
if candidato.upper() == "A":
    print("Usted ha votado por el partido rojo")
elif candidato.upper() == "B":
    print("Usted ha votado por el partido azul")
elif candidato.upper() == "C":
    print("Usted ha votado por el partido verde")
else:
    print("Opción errónea")
#****
letra = input("Letra: ")
if len(letra) != 1:
    print("Debe ser sólo una letra")
else:
    if letra.lower() in "aeiou":
        print("Es vocal")