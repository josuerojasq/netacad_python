#Método simple que permite ingresar una línea llena de números y sumarlos fácilmente.
#El código tiene una debilidad importante: muestra un resultado falso
# cuando el usuario ingresa una línea vacía. ¿Puedes arreglarlo?
linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = linea.split()
total = 0
try:
    assert len(strings) > 0
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except AssertionError:
    print("no ingresaste ningun numero")
except:
    print(substr, "no es un numero.")