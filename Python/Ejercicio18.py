
import random

opciones = ["piedra", "papel", "tijera"]


def obtener_eleccion_usuario():
    eleccion_usuario = input("Elige una opción (piedra, papel o tijera): ").lower()
    while eleccion_usuario not in opciones:
        eleccion_usuario = input("Opción inválida. Elige piedra, papel o tijera: ").lower()
    return eleccion_usuario


def obtener_eleccion_ordenador():
    return opciones[random.randint(0, 2)]


def determinar_ganador(eleccion_usuario, eleccion_ordenador):
    if eleccion_usuario == eleccion_ordenador:
        return "Empate"
    elif eleccion_usuario == "piedra":
        if eleccion_ordenador == "papel":
            return "Perdiste"
        else:
            return "Ganaste"
    elif eleccion_usuario == "papel":
        if eleccion_ordenador == "tijera":
            return "Perdiste"
        else:
            return "Ganaste"
    elif eleccion_usuario == "tijera":
        if eleccion_ordenador == "piedra":
            return "Perdiste"
        else:
            return "Ganaste"


def jugar_ronda():
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_ordenador = obtener_eleccion_ordenador()
    print("El ordenador eligió", eleccion_ordenador)
    resultado = determinar_ganador(eleccion_usuario, eleccion_ordenador)
    print(resultado)
    return resultado


resultados = []
for i in range(3):
    print("Ronda", i+1)
    resultados.append(jugar_ronda())


ganadas = resultados.count("Ganaste")
perdidas = resultados.count("Perdiste")
empates = resultados.count("Empate")
print("\nResultado final:")
print("Ganadas:", ganadas)
print("Perdidas:", perdidas)
print("Empates:", empates)
