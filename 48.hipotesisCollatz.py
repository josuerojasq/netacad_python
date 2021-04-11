#1. Toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre "c0".
#2. Si es par, evalúa un nuevo c0 como c0 ÷ 2.
#3. De lo contrario, si es impar, evalúe un nuevo  c0  como 3 × c0 + 1.
#4. Si c0 ≠ 1, salta al punto 2.

c0 = int(input("Ingresa un número: "))
pasos = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)
    pasos += 1
print("pasos = ", pasos)
