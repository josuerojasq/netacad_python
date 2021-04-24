#Algoritmo utilizado por los bancos europeos para especificar los números de cuenta.
# El estándar llamado IBAN (Número de cuenta bancaria internacional)
#Un número de cuenta compatible con IBAN consta de:
# - Un código de país de dos letras tomado del estándar ISO 3166-1
#   (por ejemplo, FR para Francia, GB para Gran Bretaña DE para Alemania, y así sucesivamente).
# - Dos dígitos de verificación utilizados para realizar las verificaciones de validez:
#   pruebas rápidas y simples, pero no totalmente confiables,
#   que muestran si un número es inválido (distorsionado por un error tipográfico) o valido.
# - El número de cuenta real (hasta 30 caracteres alfanuméricos;
#   la longitud de esa parte depene del país).
#El estándar dice que la validación requiere los siguientes pasos (según Wikipedia):
#(Paso 1) Verificar que la longitud total del IBAN sea correcta según el país
#         (este programa no lo hará, pero puedes modificar el código para cumplir con este requisito
#         si lo deseas; nota: pero debes enseñar al código a conocer todas las longitudes utilizadas en Europa).
#(Paso 2) Mueve los cuatro caracteres iniciales al final de la cadena (es decir, el código del país
#         y los dígitos de verificación).
#(Paso 3) Reemplaza cada letra en la cadena con dos dígitos, expandiendo así la cadena,
#         donde A = 10, B = 11 ... Z = 35.
#(Paso 4) Interpreta la cadena como un entero decimal y calcula el residuo de ese número
#         dividiendolo entre 97. Si el residuo es 1, pasa la prueba de verificación de dígitos
#         y el IBAN puede ser válido.
iban = input("Ingresa IBAN, por favor: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("Has introducido caracteres no válidos.")
elif len(iban) < 15:
    print("El IBAN ingresado es demasiado corto.")
elif len(iban) > 31:
    print("El IBAN ingresado es demasiado largo.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    ibann = int(iban2)
    if ibann % 97 == 1:
        print("El IBAN ingresado es válido.")
    else:
        print("El IBAN ingresado no es válido.")

#Inglés: GB72 HBZU 7006 7212 1253 00
#Francés: FR76 30003 03620 00020216907 50
#Alemán: DE02100100100152517108