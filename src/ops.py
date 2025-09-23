from os import system
import math

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
    if y == 0:
        return "Valor inválido, no divida por 0."
    return float(x / y)

def raices():
    system('cls')
    print('### Raíz Enésima ###\n')
    x = int(input('Ingresa el número para la raíz: '))
    y = int(input('\nIngresa el exponente de la raíz (ej. 2 para raíz cuadrada): '))
        
    if y == 0:
            return "Error: El exponente de la raíz no puede ser cero."
    if x < 0 and y % 2 == 0:
            return "Error: No se puede calcular una raíz par de un número negativo."
    return x ** (1 / y)

def potencias():
    system('cls')
    print('### Potencias ###\n')
    x = int(input('Ingresa la base: '))
    y = int(input('\nIngresa el exponente: '))
    return x ** y

def tablas():
    system('cls')
    print('### Tablas de Multiplicar ###\n')
    x = int(input('Ingresa el número de la tabla: '))
    rango_final = int(input('Ingresa el rango final (ej. 10 para 1 a 10): '))
        
    tabla_string = f"\nTabla del {x} (hasta {rango_final}):\n"
    for i in range(1, rango_final + 1):
        tabla_string += f"{x} x {i} = {x * i}\n"
    return tabla_string

def continuar():
    input('\nPresiona ENTER para continuar...')
    return