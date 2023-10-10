import random

numero = random.randint(1, 5)
intento = 0

print("Bienvenido! Dame tu nombre: ")
nombre = input()

print("Estoy pensando un numero del 1 al 5...")


while intento < 3:
    print("Adivina -> ")
    adivina = input()

    if int(adivina) == numero:
        print("Muy bien " + nombre + "! Adivinaste!")
        break

    intento += 1


if intento == 3:
    print("Nop! Lo siento " + nombre + " El número era: " + str(numero))
