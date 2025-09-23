from os import system
from ops import suma, resta, multiplicacion, division, raices, potencias, tablas, continuar

opciones=['suma',
          'resta',
          'multiplicación',
          'división',
          'raices',
          'potencias',
          'tablas de multiplicar',
          'salir']

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
                    resultado = raices()
                    print(f'\nEl resultado de la raiz es: {resultado}')
                    continuar()

                case 6:
                    resultado = potencias()
                    print(f'\nEl resultado de la potencia es: {resultado}')
                    continuar()

                case 7:
                    resultado = tablas()
                    print(f'\nLa tabla es:\n{resultado}')
                    continuar()

                case 8:
                    system('cls')
                    print('Fin del programa.')
                    break

                case _:
                    print('Opción no válida')
        except ValueError:
            print('Opción no válida')

main(opciones)