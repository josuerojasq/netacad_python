#El método sin parámetros "lstrip()" devuelve una cadena recién creada
# formada a partir de la original eliminando todos los espacios en blanco iniciales.
print("[" + " tau ".lstrip() + "]")
print()

#El método con un parámetro "lstrip()" hace lo mismo que su versión sin parámetros,
# pero elimina todos los caracteres incluidos en el argumento (una cadena),
# no solo espacios en blanco:
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))
print("aaron".lstrip("ar"))