# lee tres números
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

# verifica cuál de los números es el mayor con "max"
# y pásalo a la variable de mayor número
numeroMayor = max(numero1,numero2,numero3)

# verifica cuál de los números es el menor con "min"
# y pásalo a la variable de menor numero
numeroMenor = min(numero1,numero2,numero3)

# imprimir el resultado
print("El número más grande es:", numeroMayor) 
print("El número más pequeño es:", numeroMenor) 