import random

numero = random.randint(1, 5)

print("Bienvenido! Dame tu nombre: ")
nombre = input()

print("Estoy pensando un numero del 1 al 5...")
print("Adivina -> ")
adivina = input()

# If es una estructura de decision
if int(adivina) == numero:
    print("Muy bien " + nombre + "! Adivinaste!")
else:
    print("Nop! Lo siento " + nombre + " El número era: " + str(numero))
