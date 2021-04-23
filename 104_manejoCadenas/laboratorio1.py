#Escribir tu propia función, que se comporte casi como el método original "split()", por ejemplo:
# Debe aceptar únicamente un argumento: una cadena.
# Debe devolver una lista de palabras creadas a partir de la cadena,
# dividida en los lugares donde la cadena contiene espacios en blanco.
# Si la cadena está vacía, la función debería devolver una lista vacía.
def misplit(strng):
    listaFinal = []
    try:
        strng = strng.strip()
        
print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))