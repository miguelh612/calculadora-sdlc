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
    return float(x / y)

def raices():
    system('cls')
    print('### Raíz Cuadrada ###\n')
    try:
        x = float(input('Ingresa el número para calcular la raíz cuadrada: '))
        if x < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo."
        return f"La raíz cuadrada de {x} es: {math.sqrt(x)}"
    except ValueError:
        return "Error: Por favor, ingresa solo números."

def potencias():
    system('cls')
    print('### Potencias ###\n')
    try:
        x = float(input('Ingresa la base: '))
        y = float(input('\nIngresa el exponente: '))
        return f"El resultado de {x} elevado a {y} es: {x ** y}"
    except ValueError:
        return "Error: Por favor, ingresa solo números."

def tablas():
    system('cls')
    print('### Tablas de Multiplicar ###\n')
    try:
        x = int(input('Ingresa el número de la tabla: '))
        rango_final = int(input('Ingresa el rango final (ej. 10 para 1 a 10): '))
        
        tabla_string = f"\nTabla del {x} (hasta {rango_final}):\n"
        for i in range(1, rango_final + 1):
            tabla_string += f"{x} x {i} = {x * i}\n"
        return tabla_string
    except ValueError:
        return "Error: Por favor, ingresa números enteros."

def continuar():
    input('\nPresiona ENTER para continuar...')
    return