#Condicional "if - else"

#Condicional "if"

centigradosAfuera = float(input("Cuantos grados centigrados tenemos afuera?\n"))

if centigradosAfuera >= 20.0:  #evalúa una expresión de prueba.
    print("Vamonos de caminata...") #se ejecuta si la expresión de prueba es Verdadera.
else:
    print("Vamos al cine...") #se ejecuta si la expresión de prueba es Falsa.
print("Al final de todo almorzaremos") #no pertenece al bloque "if - else", lo que significa que siempre se ejecuta.