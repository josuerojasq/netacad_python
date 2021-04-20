from sys import path

path.append('/home/joerojas/Desarrollo/Curso-Basico-Phyton/101.misModulos/modules')

import modulo2

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(modulo2.suma(zeroes))
print(modulo2.producto(ones))