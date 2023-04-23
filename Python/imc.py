# Crear un programa que calcule el índicede masa corporal 
# (IMC): Crear un programa que permita al usuario ingresar su peso y altura y calcular su IMC utilizandola fórmulaIMC =peso / altura^2.

def imc(a, b):
    return a + b**2

peso = float(input("Ingresa tu peso: "))
altura = float(input("Ingresa tu altura: "))


resultadoimc = imc(peso, altura)

print(f"Este es tu IMC: {resultadoimc} ")