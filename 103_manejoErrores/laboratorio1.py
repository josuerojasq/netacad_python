def readint(prompt, min, max):
    while True:
        try:
            num = int(input(prompt))
            assert num >= min and num <= max
            return num
        except ValueError:
            print("Error: entrada incorrecta")
        except AssertionError:
            print("Error: el valor no está dentro del rango permitido ("+ str(min) +".."+ str(max) +")")

v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)