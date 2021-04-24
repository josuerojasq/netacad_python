#El método "join()" es algo complicado, así que déjanos guiarte paso a paso:
#El método realiza una unión y espera un argumento del tipo lista;
# se debe asegurar que todos los elementos de la lista sean cadenas:
# de lo contrario, el método generará una excepción "TypeError".
#Todos los elementos de la lista serán unidos en una sola cadena pero...
#...la cadena desde la que se ha invocado el método será utilizada como separador,
# puesta entre las cadenas.
#La cadena recién creada se devuelve como resultado.
cadena = ","
print(cadena.join(["omicron", "pi", "rho"]))

lista = ['esta', 'es', 'una', 'prueba', 'del', 'metodo', 'join', 'para', 'el', 'labo']
texto = ""
texto = texto.join(lista)
print(texto)