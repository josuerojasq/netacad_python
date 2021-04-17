#Función que verifique si tres lados de ciertas longitudes pueden formar un triángulo.
#La suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado.
def esUnTriangulo (a, b, c):
    return a + b > c and b + c > a and c + a > b

#print(esUnTriangulo (1, 1, 1))
#print(esUnTriangulo (1, 1, 3))
a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")

#Verificar si un triángulo es un triángulo rectángulo.
def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo  (a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    else:
        return b ** 2 == a ** 2 + c ** 2

print(esUnTrianguloRectangulo(5, 3, 4))
print(esUnTrianguloRectangulo(1, 3, 4))
print(esUnTrianguloRectangulo(3, 5, 4))

#Evaluar el campo de un triángulo con la Formula de Heron
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

print(campoTriangulo(1., 1., 2. ** .5))