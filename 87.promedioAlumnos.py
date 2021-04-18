#Necesitas un programa para calcular los promedios de tus alumnos.
#El programa pide el nombre del alumno seguido de su calificación.
#Los nombres son ingresados en cualquier orden.
#El ingresar la palabra exit da por terminado el ingreso de nombres.
#Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.
grupo = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o exit para detenerse): ")
    if nombre == 'exit':
        break
    
    calif = int(input("Ingresa la calificación del alumno (0-10): "))
    
    if nombre in grupo:
        grupo[nombre] += (calif,)
    else:
        grupo[nombre] = (calif,)
        
for nombre in sorted(grupo.keys()):
    sum = 0
    contador = 0
    for calif in grupo[nombre]:
        sum += calif
        contador += 1
    print(nombre, ":", sum / contador)

print(grupo)
