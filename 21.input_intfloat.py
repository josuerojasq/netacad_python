#Convertir los datos ingresados por teclado a int o float
algo = float(input("Inserta un número: "))
resultado = algo ** 2.0
print(algo, "al cuadrado es", resultado)

#Introducir dos valores enteros y realizar las 4 operaciones
x = int(input("Inserta el valor de x: "))
y = int(input("Inserta el valor de y: "))
suma = print("x + y =", x + y)
resta = print("x - y =", x - y)
multi = print("x * y =", x * y)
div = print("x // y =", x // y)

#Calcular el valor de la hipotenusa de un triangulo
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)