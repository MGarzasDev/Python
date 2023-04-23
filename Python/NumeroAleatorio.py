import random

numeroAleatorio = random.randint(0,5)

numeroUsuario = int(input("Inserta un numero "))

if numeroAleatorio == numeroUsuario:
    print("Felicidades! Has acertado!")
else:
    print("Lo siento, el numero era: ", numeroAleatorio)