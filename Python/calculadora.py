# crear una calculadorasimple en Python: 
#     Crear un programa que permita al usuario ingresar dos números y 
#     realizar operaciones básicas como suma, resta, multiplicación y división.
    
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b


num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Ingresa la operación que deseas realizar (+, -, *, /): ")


if operacion == '+':
    resultado = suma(num1, num2)
elif operacion == '-':
    resultado = resta(num1, num2)
elif operacion == '*':
    resultado = multiplicacion(num1, num2)
elif operacion == '/':
    resultado = division(num1, num2)
else:
    print("Operación no válida")
    resultado = None

if resultado is not None:
    print(f"El resultado de la operación {operacion} entre {num1} y {num2} es: {resultado}")
