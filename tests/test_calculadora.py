from os import system
from ops import suma, resta, multiplicacion, division, raices, potencias, tablas

opciones=['suma',
          'resta',
          'multiplicación',
          'división',
          'raices',
          'potencias',
          'tablas de multiplicar']

def main(opciones):
    system('cls')
    print('### Calculadora ###\n')
    print('Ingresa una opción:')
    for i,opciones in enumerate(opciones):
        print(f'{i}. {opciones.capitalize()}')
    opt=int(input('\nIngresa una opción: '))
    match opt:
        case 0:
            suma()
        case 1:
            resta()
        case 2:
            multiplicacion()
        case 3:
            division()
        case 4:
            raices()
        case 5:
            potencias()
        case 6:
            tablas()
        case _:
            print('Opción no válida')

main(opciones)