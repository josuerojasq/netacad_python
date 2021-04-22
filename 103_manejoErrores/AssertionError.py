#Una excepción concreta generada por la instrucción de aserción cuando su argumento se evalúa como
# False (falso), None (ninguno), 0, o una cadena vacía.
from math import tan, radians
angle = int(input('Ingresa el angulo entero en grados: '))

# debemos estar seguros de ese angulo != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))