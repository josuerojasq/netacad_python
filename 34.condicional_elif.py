# "elif", es una forma más corta de else-if.
#Se usa para verificar más de una condición,
#y para detener cuando se encuentra la primera declaración verdadera.

print("Selecciona una de las siguientes opciones:")
print("1. El Clima es bueno hoy")
print("2. Hay boletos disponibles en el Cine")
print("3. Hay mesas libres en tu Restaurante favorito")
print("4. Ninguna de las anteriores")
opcion = int(input(""))

if opcion == 1:
    print("Vamonos de caminata hoy...")
elif opcion == 2:
    print("Veamos una pelicula hoy...")
elif opcion == 3:
    print("Almorcemos en nuestro lugar favorito...")
else:
    print("Quedemonos en casa y juguemos ajedrez...")