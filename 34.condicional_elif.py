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

#Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:
#Imprima el enunciado "Si, ¡El Espatifilo es la mejor planta de todos los tiempos!"  en la pantalla si la cadena ingresada es "Espatifilo".
#Imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo".
#Imprima  "¡Espatifilo! ¡No [entrada]!"  de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

entrada = input("Dime algo...\n")

if entrada == "Espatifilo" : print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif entrada == "espatifilo" : print("No, ¡quiero un gran Espatifilo!")
else: print("¡Espatifilo! ¡No " + entrada + "!")