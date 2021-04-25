#Escribir un programa que responda la siguiente pregunta:
# ¿Los caracteres que comprenden la primera cadena están ocultos dentro de la segunda cadena?
#Por ejemplo: "dog"
#Si la segunda cadena es "vcxzxduybfdsobywuefgas", la respuesta es si.
#Si la segunda cadena es "vcxzxdcybfdstbywuefsas", la respuesta es no
# (ya que no están las letras "d", "o", "g", ni en ese orden).
#Consejos:
#Debes usar las variantes de dos argumentos de las funciones find() dentro de tu código.
#No te preocupes por mayúsculas y minúsculas.

txt1 = input("Introducir cadena a buscar: ")
txt2 = input("Introducir 2da. cadena: ")
txt1 = txt1.upper()
txt2 = txt2.upper()
sw = True
fnd = -1
for char in txt1:
    fnd = txt2.find(char, fnd + 1)
    if fnd == -1:
        sw = False
        break
if sw: print("Si")
else: print("No")