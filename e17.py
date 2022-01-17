#11.1
def sumatoria(lista):
    suma=0
    for n in lista:
        suma+=n
    return suma

def numerosMenores(lista, limite):
    nueva=[]
    for n in lista:
        if n<limite:
            nueva.append(n)
    return nueva

def frecuencias(lista):
    nueva=[]
    for n in lista:
        if [n, lista.count(n)] not in nueva:
            nueva.append([n, lista.count(n)])
    return nueva

#*
numeros=[]
nro=int(input("Número: "))
while nro!=0:
    numeros.append(nro)
    nro=int(input("Número: "))
#**
print("Sumatoria de los números:", sumatoria(numeros))
eliminar=int(input("Número a eliminar: "))
#***
if eliminar in numeros:
    numeros.remove(eliminar)
else:
    print("Ese número no está entre los ingresados")
#****
limite=int(input("Filtrar números menores a: "))
for n in numerosMenores(numeros, limite):
    print(n)
#*****
print("Frecuencias:")
for tupla in frecuencias(numeros):
    print(tupla[0],"aparece",tupla[1],"veces.")