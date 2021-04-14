#La "comprensión de listas" te permite crear nuevas listas a partir de las existentes
#de una manera concisa y elegante. La sintaxis de una lista de comprensión es la siguiente:
# "[expresión for elemento in lista if condicional]"
# El cual es un equivalente del siguiente código:
#"for elemento in lista:
#     if condicional:
#         expresión"
#Crea una lista de cinco elementos con los primeros cinco números naturales elevados a la potencia de 3:
cubos = [num ** 3 for num in range (5)]
print(cubos) # salidas: [0, 1, 8, 27, 64]

#Puedes usar listas anidadas en Python para crear matrices (es decir, listas bidimensionales)
# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

tabla = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(tabla)
print(tabla [0][0]) # salida: ':('
print(tabla [0][3]) # salida: ':)'

#Puedes anidar tantas listas en las listas como desee y, por lo tanto, crear listas n-dimensionales
# Cubo - un arreglo tridimensional (3x3x3)

cubo = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cubo)
print(cubo [0][0][0]) # salida: ':('
print(cubo [2][2][0]) # salida: ':)