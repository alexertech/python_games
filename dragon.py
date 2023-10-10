import random
import time


#
# Sección de funciones
#

def bienvenida():
    print("Estas en un mundo lleno de dragones.")
    print("Al  frente de ti hay dos cuevas...")
    print("Una tiene un dragon amistoso, y la otra uno hambriento")


def eligeCueva():
    cueva = ''
    while cueva != '1' and cueva != '2':
        print("Cual cueva eliges? (1-2)")
        cueva = input()

    return cueva


def revisarCueva(cuevaElegida):
    print("Te acercas a la cueva...")
    time.sleep(2)
    print("Esta obscura y tenebrosa...")
    time.sleep(2)
    print("Un gran dragón salta al frente de ti!!")
    print("Abre su mandibula y ...")
    time.sleep(2)

    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print("Te da su tesoro!!!")
    else:
        print("Te traga de un mordizco!! >:) ")

#
# Programa principal
#


jugarOtra = 'si'

while jugarOtra == 'si' or jugarOtra == 's':

    bienvenida()

    selCueva = eligeCueva()

    revisarCueva(selCueva)

    print("Quieres jugar otra vez? (si/no)")
    jugarOtra = input()
