#Una excepción concreta que surge cuando intentas acceder al elemento inexistente de una colección
# (por ejemplo, el elemento de un diccionario).
# como abusar del diccionario
# y cómo lidiar con ello

dict = { 'a' : 'b', 'b' : 'c', 'c' : 'd' }
ch = 'a'
try:
    while True:
        ch = dict[ch]
        print(ch)
except KeyError:
    print('No existe tal clave:', ch)