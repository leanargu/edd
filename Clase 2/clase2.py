# Repaso de la clase 1
import math


def imprimir_tringulo(numero: int) -> None:
    for i in range(numero):
        salida = ""
        for j in range(1, 2 * (i + 1), 2):
            salida = str(j) + " " + salida
        print(salida)

def imprimir_asteriscos() -> None:
    num = 5
    for i in range(num):
        print((i + 1) * "*")

def contar_digitos(numero: int) -> None:
    contador = 0
    while (numero > 0):
        numero = numero // 10
        contador += 1
    print(contador)

#print("--- Ejercicios Clase 1 ---")
#contar_digitos(513)

# Practica de la clase 2

# 1. Ejemplo básico de función
def saludar() -> None:
    print("Hola mundo!!!")

# 2. Función con parámetros, type hinting y retorno
def generar_saludo(nombre: str) -> str:
    """Retorna un saludo personalizado."""
    return f"¡Hola, {nombre}!"


# 3. Función con parámetros por defecto
def sumaInt(num1: int = 0, num2: int = 0) -> int:
    return num1 + num2


#Ejercicios de la guia

# Ejercicio 3
def factorial(N:int) -> int:
    factorialN = 1
    for i in range(1, N + 1):
        factorialN = factorialN * i
    return factorialN
#print(factorial(50))
# Ejercicio 5

# Ejercicio 8
def potencia_numero(n: int, m: int) -> int:
    resultado = 1

    for i in range(m):
        resultado = resultado * n

    return resultado
# Ejercicio 10
def es_ano_biciesto(ano: int) -> bool:
    """

    Sea multiplo de 4 y no multiplo de 10
    Si es multiplo de 400, si es

    if (es_multiplo_de_400) o (es_multiplo_de_4 y no_es_multiplo_de_10)
    if (es_multiplo_de_4)
    """
# Ejercicio 12
def sumar_digitos(numero: int) -> int:
    """
    Escriba una funcion que tome un entero y retorne la suma de sus digitos
    """
    resultado = 0
    while numero > 0:
        resultado += numero % 10
        numero = numero // 10

    return resultado

#Ejercicio 14
def es_numero_primo(numero: int) -> bool:
    #Son divisibles solo por 1 y por si mismos
    #Son mayores que 1 (arrancan desde 2)
    #Para saber si es primo, dividir por los primos menores hasta la raiz de N
    divisor = 2

    while numero % divisor != 0 and divisor <= numero:
        divisor += 1

    return divisor == numero

print(es_numero_primo(33))






