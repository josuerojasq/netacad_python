#Considera el caso donde la instrucción colocada después del "if"  es otro "if".

centigradosAfuera = float(input("Cuantos grados centigrados tenemos afuera?\n"))

if centigradosAfuera >= 20.0:  #evalúa una expresión de prueba.
    buenRestaurante = input("Encontramos un buen Restaurante? Si / No\n")
    if buenRestaurante == "Si":
        print("Almorzaremos allí...")
    else:
        print("Comeremos un sandwich")
else:
    boletosDisponibles = input("Hay boletos disponibles en el cine? Si / No\n")
    if boletosDisponibles == "Si":
        print("Veamos una película...")
    else:
        print("Vamonos de compras...")
print("Al final del día, volveremos a casa...")