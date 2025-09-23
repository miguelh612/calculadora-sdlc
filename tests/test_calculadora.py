from os import system
from test_ops import suma, resta, multiplicacion, division, raices, potencias, tablas, continuar

opciones=['suma',
          'resta',
          'multiplicación',
          'división',
          'raices',
          'potencias',
          'tablas de multiplicar']

def main(menu):
    while True:
        try:
            system('cls')
            print('### Calculadora ###\n')
            print('Ingresa una opción:')
            for i,opciones in enumerate(menu):
                print(f'{i+1}. {opciones.capitalize()}')
            opt=int(input('\nIngresa una opción: '))
            match opt:
                case 1:
                    print(f'\nEl resultado de la suma es: {suma()}')
                    continuar()
                case 2:
                    print(f'\nEl resultado de la resta es: {resta()}')
                    continuar()
                case 3:
                    print(f'\nEl resultado de la multiplicación es: {multiplicacion()}')
                    continuar()
                case 4:
                    print(f'\nEl resultado de la división es: {division()}')
                    continuar()
                case 5:
                    raices()
                    continuar()
                case 6:
                    potencias()
                    continuar()
                case 7:
                    tablas()
                    continuar()
                case _:
                    print('Opción no válida')
        except:
            print('Opción no válida')

main(opciones)