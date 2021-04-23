#Escribir tu propia función, que se comporte casi como el método original "split()", por ejemplo:
# Debe aceptar únicamente un argumento: una cadena.
# Debe devolver una lista de palabras creadas a partir de la cadena,
# dividida en los lugares donde la cadena contiene espacios en blanco.
# Si la cadena está vacía, la función debería devolver una lista vacía.
def misplit(strng):
    listaFinal = []
    try:
        strng = strng.strip()
        if " " in strng:
            word = ""
            for char in strng:
                if ord(char) != 32: word += char
                else:
                    if len(word) > 0: listaFinal.append(word)
                    word = ""
            listaFinal.append(word)
        else:
            if len(strng) > 0: listaFinal.append(strng)
        return listaFinal
    except:
        print("Debes introducir una cadena...")
        return None

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("Joel  Rojas   Quisbert   JoeRojas  "))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))
print(misplit(1235))