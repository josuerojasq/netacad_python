#La cadena comienza con tres apóstrofes, no uno.
# El mismo apóstrofe triplicado se usa para terminar la cadena.
multiLinea = '''Linea #1
Linea #2'''

##Son 16 visibles y el programa imprime 17. El caracter que falta es simplemente invisible:
# es un espacio en blanco. Se encuentra entre las dos líneas de texto.
#Se denota como: "\n"
print(len(multiLinea))

#Las cadenas multilínea pueden ser delimitadas también por comillas triples:
multiLinea2 = """Linea #1
Linea #2"""

print(len(multiLinea2))