#Una excepción concreta que surge cuando se intenta acceder al elemento de una secuencia inexistente
# (por ejemplo, el elemento de una lista).
# el codigo muestra una forma extravagante
# de dejar el bucle

lista = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(lista[ix])
        ix += 1
    except IndexError:
        doit = False

print('Listo')