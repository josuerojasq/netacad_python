#El método index() (es un método, no una función) busca la secuencia desde el principio,
# para encontrar el primer elemento del valor especificado en su argumento.
#Nota: el elemento buscado debe aparecer en la secuencia - su ausencia causará una excepción "ValueError".
#El método devuelve el índice de la primera aparición del argumento
# (lo que significa que el resultado más bajo posible es 0,
# mientras que el más alto es la longitud del argumento decrementado por 1).
exampleString = "aAbByYzZaA"

print(exampleString.index("b"))
print(exampleString.index("Z"))
print(exampleString.index("A"))