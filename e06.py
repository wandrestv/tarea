#5.2
CapacidadM2 = 4
PorcentajeGra = 0.2
PorcentajeEsp = 0.3
PorcentajeCom = 0.7

dimensiones = float(input("Dimensiones del estadio (en m2): "))
personasgra = int(input("Cantidad de personas que caben en las gradas: "))
porcentajeesc = int(input("Porcentaje que ocupa el escenario: "))
m2gradas = dimensiones * PorcentajeGra
m2escenario = dimensiones * (porcentajeesc/100)
m2disponibles = dimensiones - m2gradas - m2escenario
personastot = (m2disponibles * 4) + personasgra
print("Caben", personastot, "personas")

precioentesp = float(input("Precio de la entrada especial: $"))
precioentcom = float(input("Precio entrada común: $"))
print("Ingreso total de ventas: $",(personastot * PorcentajeEsp) * precioentesp + (personastot * PorcentajeCom) * precioentcom)