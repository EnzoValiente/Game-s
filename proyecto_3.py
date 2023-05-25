#Ahorcado
from random import choice


usuario = input('¡ Hola !  Bienvenido al juego del ahorcado. \n ¿Como te llamas?: ').title()
print('*'*30)
print('*'*30,'\n')
print(f'Hola {usuario}, empezemos! \n Recuerda que tienes 6 vidas.')

palabras_ocultas = ['helicoptero', 'dentista', 'bicicleta', 'avion', 'profesor', 'tarantula']
oculta = choice(palabras_ocultas)
ocul = len(oculta) * '-'
letras_correctas = []
letras_incorrectas = []
print('*'*30)
print('*'*30,'\n')
print(f'Tu palabra oculta es: {ocul}')

def pedir_letra():
    letra = ''
    while len(letra) != 1 or letra.isdigit():
        letra = input('Ingrese una letra: ')
    print('*'*30)
    print('*'*30,'\n')
    return letra.lower()


def validar_letra():
    vidas_restantes = 6
    while vidas_restantes != 0:
        letra = pedir_letra()
        if letra in oculta:
            letras_correctas.append(letra)
            print(f'La letra "{letra}" se encuentra en la palabra oculta! ¡Bien echo!')
            print(f'Las letras que acertaste: {letras_correctas}')
            mostrar_tablero(oculta)
        else:
            letras_incorrectas.append(letra)
            print(f'La letra {letra} no se encuentra en la palabra vacia. Intentalo nuevamente..')
            vidas_restantes -= 1
            print(f'Te quedan {vidas_restantes} vidas..')
            print(f'Letras incorrectas: {letras_incorrectas}')
            mostrar_tablero(oculta)
    print('*'*30)
    print('*'*30,'\n')
    print(f'¡Has perdido! la palabra era "{oculta}"')
    print('*'*30)
    print('*'*30,'\n')

def mostrar_tablero(palabra):
    lista_oculta = []
    for i in oculta:
        if i in letras_correctas:
            lista_oculta.append(i)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))




validar_letra()







