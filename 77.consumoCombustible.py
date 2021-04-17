#El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes.
#Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.
#En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.
#Escribir un par de funciones que conviertan l/100km a mpg(milas por galón), y viceversa.
#Aquí hay información para ayudarte:
# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.
def l100kmtompg(liters):
    litroskm = liters / 100
    milla = 1 / 1.609344 #valor de 1 km en millas
    galon = 1 / 3.785411784 # valor de 1 litro en galones
    mpg = milla / (litroskm * galon)
    return mpg

def mpgtol100km(miles):
    kmgalon = miles * 1.609344
    litroskm = 3.785411784 / kmgalon
    l100km = litroskm * 100
    return l100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))