def AreaTriangulo (a, b):
    return (a * b)/2

Base = float(input("Ingresa la base del trinagulo: "))
Altura = float(input("Ingresa la altura del triangulo: "))

Area = AreaTriangulo(Base, Altura)

print(f"Este es el area del triangulo: {Area}")