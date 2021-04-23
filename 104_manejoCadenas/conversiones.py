#cómo convertir un número (un entero o un flotante) en una cadena, y viceversa
#La conversión de cadena a número es simple, ya que siempre es posible.
# Se realiza mediante una función llamada "str()".
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

#La transformación inversa solo es posible cuando la cadena representa un número válido.
# Si no se cumple la condición, espera una excepción "ValueError".
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)