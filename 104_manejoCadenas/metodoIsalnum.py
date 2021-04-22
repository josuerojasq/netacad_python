#El método sin parámetros "isalnum()" comprueba si la cadena contiene solo dígitos
# o caracteres alfabéticos (letras) y devuelve True (verdadero) o False (falso) de acuerdo al resultado.
#Nota: cualquier elemento de cadena que no sea un dígito o una letra
# hace que el método regrese False (falso). Una cadena vacía también lo hace.
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())