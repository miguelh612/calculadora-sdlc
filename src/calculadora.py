from os import system
from ops import suma, resta, multiplicacion, division, raices, potencias, tablas

opciones=['suma',
          'resta',
          'multiplicación',
          'división',
          'raices',
          'potencias',
          'tablas de multiplicar']

def main(menu):
    system('cls')
    print('### Calculadora ###\n')
    print('Ingresa una opción:')
    for i,opciones in enumerate(menu):
        print(f'{i+1}. {opciones.capitalize()}')
    opt=int(input('\nIngresa una opción: '))
    match opt:
        case 1:
            suma()
        case 2:
            resta()
        case 3:
            multiplicacion()
        case 4:
            division()
        case 5:
            raices()
        case 6:
            potencias()
        case 7:
            tablas()
        case _:
            print('Opción no válida')

main(opciones)