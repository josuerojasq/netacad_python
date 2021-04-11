#Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla:
for i in range(1, 11):
    if i % 2 != 0:
        print(i, end=" - ")
print()

#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla:
x = 1
while x < 11:
    if x % 2 != 0:
        print(x, end=" - ")
    x += 1
print()

#Crea un programa con un bucle "for" y una declaración break.
#El programa debe iterar sobre los caracteres en una dirección de correo electrónico,
#salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea.
correo = input("Ingrese una dirección de correo: ")
for ch in correo:
    if ch == "@":
        break
    print(ch, end="")
print()

#Crea un programa con un bucle "for" y una declaración "continue".
#El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x,
#e imprimir la cadena modificada en la pantalla:
cadena = input("Ingrese una cadena de digitos: ")
for digit in cadena:
    if digit == "0":
        print("x", end="")
        continue
    print(digit,end="")
print()

#Ejercicio 5
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)
print()

#Ejercicio 6
n = range(4)
for num in n:
    print(num - 1)
else:
    print(num)
print()

#Ejercicio 7
for i in range(0, 6, 3):
    print(i)