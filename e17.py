#10.4
#*
def validarDNI(dni):
    cantidad=0
    while dni!=0:
        cantidad+=1
        dni//=10
    return cantidad==7 or cantidad==8

print(validarDNI(340))
print(validarDNI(3408372))