#escribir un programa que:
#Le pregunta al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA;
# en realidad, el orden de los dígitos no importa).
#Da como salida El Dígito de la Vida para la fecha ingresada.
def obtenerDigitoVida(birthday):
    ddlV = 0
    listaDigitos = list(birthday)
    for digito in listaDigitos:
        ddlV += int(digito)
    if ddlV > 9: ddlV = obtenerDigitoVida(str(ddlV))
    return ddlV


birthday = input("""Ingresa tu fecha de nacimiento
Formatos AAAAMMDD o AAAADMM o MMDDAAAA: \n""")
if birthday.isdigit() and len(birthday) >= 7:
    ddlV = obtenerDigitoVida(birthday)
    print("Digito de la vida = ", ddlV)
else:
    print("Debes introducir un valor con el formato señalado...")