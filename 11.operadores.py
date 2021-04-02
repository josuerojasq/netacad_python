#Operadores básicos

#Suma
print(2+2)
#Resta
print(5-2)
#Multiplicación
print(2*5)
#División
print(19/2)
#División entera
print(13//2)
#Modulo(Resto)
print(15%4)
#Potencia
print(3**3)

#Cuando ambos ** argumentos son enteros, el resultado es entero también.
#Cuando al menos un ** argumento es flotante, el resultado también es flotante.
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#Tambien aplica a la multiplicación
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#El resultado producido por el operador de división siempre es flotante.
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#El resultado carece de la parte fraccionaria,
#   - Está ausente (para los enteros),
#   - O siempre es igual a cero (para los flotantes);
# Esto significa que los resultados siempre son redondeados.
#Se ajusta a la regla entero vs flotante.

print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)