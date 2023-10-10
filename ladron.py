import random

print(":: ENCUENTRA AL LADRON::")

print("Tienes 100 creditos para encontra al ladron, por cada")
print("intento fallido, perderás 25 créditos. Hay 8 pisos.")
print("Donde esta?")

jugar = 's'

while jugar == 's':

    # Creando pisos y escondiendo al ladron
    pisos = [0, 0, 0, 0, 0, 0, 0, 0]
    ladron = random.randint(0, 7)
    pisos[ladron] = 1

    # Inicializar el Juego
    intento = 0
    encontrado = 0
    creditos = 100

    while creditos > 0 and encontrado == 0:

        while str(intento) not in '12345678':
            print("Piso (1-8): ")
            intento = input()

        intento = int(intento)-1

        if pisos[intento] == 1:
            encontrado = 1
        else:
            print("Nop, ahí no está!")
            creditos -= 25
            print(str(creditos) + " creditos restantes!")
            intento = 0

    if encontrado == 1:
        print("Muy bien, lo encontraste con " + str(creditos) + " creditos!")
    else:
        print("Perdiste! el ladrón estaba en el piso: " + str(ladron+1))

    print("Quieres otra partida? (s/n)")
    jugar = input()
