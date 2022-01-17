#4.1
#*
cadena = "si, profe, es cierto... yo me comi la tarea"
print(cadena[10])
#**
print(cadena[-1])
#***
print(cadena[0:9])
#****
print(cadena[::3])
#*****
print(cadena[::-1])
#******
print(cadena[4:9])
#*******
s = "   hola, ¿cómo estás?"
print(s[::-1])
#*******
print(s[len(s)-1])
#*******
print(s.count("o"))
#*******
print(s.count("Hola"))
#*******
print(s[-4:])
#*******
print(s[15:])
#*******
print(s.find("o"))
#*******
print(s.strip())
#*******
x=s.upper
print(x == s)
#*******
print(s[14:].upper())
#*******
print(len(s)%2 != 0)
#*******
print(s.replace(" ", "*"))
#*******
print(s.replace("z", "Z"))
#*******
x = "programar en python"
print(len(x))
#*******
cadena = "hola"
print(cadena.find("2"))
#*******
print("a" in "dátiles")
#*******
print("me gusta programar".find(" "))
#*******
print("me gusta programar".count(" "))
#*******
# cadena[0] = "H" "Da error porque el tipo string es inmutable y no se puede cambiar lo que contiene"
#*******
nueva = "C"
print(nueva + cadena [1:])
#*******
x = "hoy es día miércoles"
print(x.replace("í", "i").replace("é","e"))
#*******
if len(x)%2 == 0:
    print("La longitud de la cadena de caracteres es par")
else:
    print("La longitud de la cadena de caracteres es impar")
#*******
print(x.count("a")+x.count("e")+x.count("i")+x.count("o")+x.count("u"))