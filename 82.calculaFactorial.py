#La siguiente función a definir calcula factoriales
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1):
        producto *= i
    return producto

for n in range(1, 6): # probando
    print(n, factorialFun(n))