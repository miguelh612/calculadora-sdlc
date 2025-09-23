from os import system

def suma():
    system('cls')
    print('### Suma ###\n')
    x=int(input('Ingresa el primer número: '))
    y=int(input('\nIngresa el segundo número: '))
    return x + y

def resta():
    system('cls')
    print('### Resta ###\n')
    x=int(input('Ingresa el primer número: '))
    y=int(input('\nIngresa el segundo número: '))
    return x - y

def multiplicacion():
    system('cls')
    print('### Multiplicación ###\n')
    x=int(input('Ingresa el primer número: '))
    y=int(input('\nIngresa el segundo número: '))
    return x * y

def division():
    system('cls')
    print('### División ###\n')
    x=int(input('Ingresa el primer número: '))
    y=int(input('\nIngresa el segundo número: '))
    return float(x / y)

def raices():
    pass

def potencias():
    pass

def tablas():
    pass

def continuar():
    input('\nPresiona ENTER para continuar...')
    return