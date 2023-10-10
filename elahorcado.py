import random

DIBUJOS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def muestraDibujos(DIBUJOS, equivocadas, correctas, palabraSecreta):

    print(DIBUJOS[len(equivocadas)])
    print()

    print("Letras Equivocadas:", end=' ')

    for letra in equivocadas:
        print(letra, end=' ')
    print()

    blancos = '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in correctas:
            blancos = blancos[:i] + palabraSecreta[i] + blancos[i+1:]

    for letra in blancos:
        print(letra, end=' ')
    print()


def adivinaLetra(yaAdvinada):
    while True:
        print('Adivina una letra: ', end=' ')
        intento = input().lower()

        if len(intento) != 1:
            print('Ingresa sólo una letra.')
        elif intento in yaAdvinada:
            print('Ya elegiste esa letra. Prueba otra.')
        elif intento not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor inserta una letra')
        else:
            return intento


def obtenPalabraAleatoria(listaPalabras):
    tamano = len(listaPalabras)
    aleat = random.randint(0, tamano - 1)
    return listaPalabras[aleat]


def jugarOtra():
    print("Quieres jugar otra vez? (si/no)")
    return input().lower().startswith('s')


palabras = 'hormiga mono murcielago oso castor'
palabras = palabras.split()


print("E L A H O R C A D O")

equivocadas = ''
correctas = ''
palabraSecreta = obtenPalabraAleatoria(palabras)
juegoTerminado = False

while True:

    muestraDibujos(DIBUJOS, equivocadas, correctas, palabraSecreta)

    intento = adivinaLetra(equivocadas + correctas)
    #
    #
    #

    if intento in palabraSecreta:
        correctas += intento

        todasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in correctas:
                todasLasLetras = False
                break

        if todasLasLetras:
            print("Si! La palabra secreta es " + palabraSecreta + "! GANASTE!")
            juegoTerminado = True

    else:
        equivocadas += intento

        if len(equivocadas) == len(DIBUJOS)-1:
            muestraDibujos(DIBUJOS, equivocadas, correctas, palabraSecreta)
            print("Se te acabaron los intentos!")
            print("La palabra secreta era: " + palabraSecreta)
            juegoTerminado = True

    #
    #
    #

    if juegoTerminado:
        if jugarOtra():
            equivocadas = ''
            correctas = ''
            palabraSecreta = obtenPalabraAleatoria(palabras)
            juegoTerminado = False
        else:
            break
