#El operador "in", comprueba si el argumento izquierdo (una cadena)
# se puede encontrar en cualquier lugar dentro del argumento derecho (otra cadena).
alpfabeto = "abcdefghijklmnopqrstuvwxyz"
prueba = "Esta oracion tiene espacios"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("1" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)
print(" " in alpfabeto)
print()

#El operador "not in" también es aplicable aquí
print("f" not in alpfabeto)
print("F" not in alpfabeto)
print("1" not in alpfabeto)
print("ghi" not in alpfabeto)
print("Xyz" not in alpfabeto)
print(" " not in prueba)