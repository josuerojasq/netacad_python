#Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno.
#Hay 20 habitaciones en cada piso.
#Para esto, necesitas un arreglo que pueda recopilar y procesar información
#sobre las habitaciones ocupadas/libres.

#Primer paso: El tipo de elementos del arreglo. En este caso, sería un valor booleano (True/False).
#Paso dos: Análisis de la situación. Resume la información disponible:
#tres edificios, 15 pisos, 20 habitaciones.

habitaciones = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

#Ahora ya puedes reservar una habitación para dos recién casados:
#en el segundo edificio, en el décimo piso, habitación 14:
habitaciones[1][9][13] = True

#Desocupa el segundo cuarto en el quinto piso ubicado en el primer edificio:
habitaciones[0][4][1] = False

#Verifica si hay disponibilidad en el piso 15 del tercer edificio:
vacante = 0

for numeroHabitacion in range(20):
    if not habitaciones[2][14][numeroHabitacion]:
        vacante += 1
print("Habitaciones disponibles en piso 5, tercer edificio:",vacante)