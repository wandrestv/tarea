#7.2
#*
corrimiento = int(input("Corrimiento: "))
alfabeto = "abcdefghijklmnñopqrstuvwxyz"

for i in range (5):
    mensaje = input("Mensaje a encriptar: ")
    encriptado = ""
    for caracter in mensaje: 
        if caracter.lower() in alfabeto:
            indice = alfabeto.find(caracter.lower())
            indice = (indice + corrimiento) % 27
            encriptado += alfabeto[indice]
        else:
            encriptado += caracter
    print("***Mensaje encriptado:", encriptado)
    