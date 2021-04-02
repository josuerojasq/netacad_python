#Los operadores en su mayoria tiene un enlazado hacia la izquierda.
print(2 + 3 * 5)

print(9 % 6 % 2)

#El operador de exponenciación utiliza enlazado hacia la derecha.
print(2 ** 2 ** 3)

#Ambos operadores (* y %) tienen la misma prioridad
print(2 * 3 % 5)

#las sub-expresiones dentro de los paréntesis siempre se calculan primero.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)