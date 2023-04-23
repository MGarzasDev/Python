from tokenize import String


def AreaTriangulo (a, b):
    return (a * b)/2

def numeroPar (a):
    if a % 2 == 0:
        print("El numero es Par")
    else:
        print("No es par")
        
def calcularLista(a):
    return sum(a)
    
def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado

def cadena(a):
    return a.upper()

print("¿Que deseas hacer?")
print("1. Area triangulo")
print("2. Numero Par")
print("3. Suma lista")
print("4. Calcular factorial")
print("5. Convertir cadena")

eleccion = int(input("Inserta una opcion "))

while eleccion > 0:
    if eleccion == 1:
        Base = float(input("Ingresa la base del trinagulo: "))
        Altura = float(input("Ingresa la altura del triangulo: "))
        Area = AreaTriangulo(Base, Altura)
        print(f"Este es el area del triangulo: {Area}")
        eleccion = int(input("Inserta una opcion "))
    elif eleccion == 2:
        Numero = int(input("Ingresa un numero: "))
        Par = numeroPar(Numero)
        eleccion = int(input("Inserta una opcion "))
    elif eleccion == 3:
        lista_numeros = [1,2,3,4,5]
        sumaLista = calcularLista(lista_numeros)
        print(f"Esta es la suma de la lista: {sumaLista}")
        eleccion = int(input("Inserta una opcion "))
    elif eleccion == 4:
        numero = int(input("Introduce un numero: "))
        CalcularFactorial = factorial(numero)
        print(f"El factorial de {numero} es {CalcularFactorial}")
        eleccion = int(input("Inserta una opcion "))
    elif eleccion == 5:
        Cadena = str(input("Introduce una frase: "))
        IntroducirCadena = cadena(Cadena)
        print(f"Cadena: {IntroducirCadena}")
        eleccion = int(input("Inserta una opcion "))
    else:
        print("No es una opcion válida")
        eleccion = int(input("Inserta una opcion "))
        
        