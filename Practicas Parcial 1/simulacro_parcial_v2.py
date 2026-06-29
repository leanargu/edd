import numpy as np

# =============================================================================
# SIMULACRO PRE-PARCIAL V2 - ESTRUCTURA DE DATOS
# Objetivo: Practicar Recursividad Avanzada, TDA con Matrices y Excepciones.
# =============================================================================

# -----------------------------------------------------------------------------
# EJERCICIO 1: RECURSIVIDAD DE BÚSQUEDA (VECTORES)
# Consigna: Implementar la función recursiva 'todos_mayores_a(vector, n)' que
# retorna True si TODOS los elementos son estrictamente mayores a 'n'.
# REGLA: No usar bucles. Usar slicing y operadores lógicos.
# -----------------------------------------------------------------------------

def todos_mayores_a(vector: np.array, n: int) -> bool:
    son_todos_mayores = False
    if len(vector) == 1:
        son_todos_mayores = vector[0] > n
    else:
        son_todos_mayores = vector[0] > n and todos_mayores_a(vector[1:],n)
    return son_todos_mayores

# -----------------------------------------------------------------------------
# EJERCICIO 2: TDA "VIVERO" (MATRICES DE OBJETOS + LÓGICA)
# Consigna: Modelar un Vivero que administra plantas en una matriz de NxM.
# 
# Requisitos:
# 1. Clase Planta: nombre (str), dias_sin_riego (int), es_desertica (bool).
# 2. Clase Vivero:
#    - __init__(filas, columnas): Matriz de objetos Planta (inicialmente None).
#    - plantar(f, c, planta): Ubica la planta. Lanza Exception si el lugar
#      está ocupado o fuera de rango.
#    - necesitan_agua_en_fila(n_fila): Retorna cuántas plantas en esa fila 
#      necesitan agua. Una planta necesita agua si (dias_sin_riego > 3) 
#      Y NO es desértica. (Cuidado con los None).
# -----------------------------------------------------------------------------

class Planta:
    def __init__(self, nombre: str, dias_sin_riego: int, es_desertica: bool):
        self.__nombre = nombre
        self.__dias_sin_riego = dias_sin_riego
        self.__es_desertica = es_desertica

    def dias_sin_riego(self):
        return self.__dias_sin_riego

    def es_desertica(self):
        return self.__es_desertica

class Vivero:
    def __init__(self, filas: int, columnas: int):
        self.__plantas = np.empty((filas, columnas), dtype=object)

    def plantar(self, f: int, c: int, planta: Planta):
        filas_vivero, columnas_vivero = self.__plantas.shape
        if f < filas_vivero and c < columnas_vivero:
            self.__plantas[f][c] = planta

    def necesitan_agua_en_fila(self, n_fila: int) -> int:
        filas_vivero = self.__plantas.shape[0]
        plantas_a_regar = 0
        if n_fila < filas_vivero:
            fila = self.__plantas[n_fila]
            for planta in fila:
                if planta and planta.dias_sin_riego() > 3 and not planta.es_desertica():
                    plantas_a_regar += 1
        return plantas_a_regar

# -----------------------------------------------------------------------------
# EJERCICIO 3: RECURSIVIDAD DE STRINGS (CORTES)
# Consigna: Implementar la función 'solo_mayusculas(cadena)' que retorna un 
# nuevo string que contenga ÚNICAMENTE las letras mayúsculas de la original.
# Ejemplo: "Hola Mundo" -> "HM"
# Ayuda: cadena[0].isupper() devuelve True si el carácter es mayúscula.
# -----------------------------------------------------------------------------

def solo_mayusculas(cadena: str) -> str:
    mayusculas = ""
    if len(cadena) == 1:
        if cadena[0].isupper():
            mayusculas += cadena[0]
    else:
        if cadena[0].isupper():
            mayusculas += cadena[0]
        mayusculas = mayusculas + solo_mayusculas(cadena[1:])
    return mayusculas



# =============================================================================
# SUITE DE TESTS (No modificar, usar para validar)
# =============================================================================

def ejecutar_tests():
    print("--- INICIANDO VALIDACIÓN SIMULACRO V2 ---")
    
    # Test Ejercicio 1
    v = np.array([10, 15, 20, 12])
    res1 = todos_mayores_a(v, 5)   # Debería ser True
    res2 = todos_mayores_a(v, 18)  # Debería ser False
    print(f"Ejer 1 (Búsqueda): {'[OK]' if res1 == True and res2 == False else '[FALLÓ]'}")

    # Test Ejercicio 2
    try:
        jardin = Vivero(2, 2)
        p1 = Planta("Rosa", 5, False)   # Necesita agua
        p2 = Planta("Cactus", 10, True) # No necesita (es desértica)
        jardin.plantar(0, 0, p1)
        jardin.plantar(0, 1, p2)
        
        cant = jardin.necesitan_agua_en_fila(0)
        print(f"Ejer 2 (TDA Vivero): {'[OK]' if cant == 1 else '[FALLÓ]'}")
    except Exception as e:
        print(f"Ejer 2 (TDA Vivero): [ERROR EN IMPLEMENTACIÓN] -> {e}")

    # Test Ejercicio 3
    res_str = solo_mayusculas("Estructura De Datos")
    print(f"Ejer 3 (Strings): {'[OK]' if res_str == 'EDD' else f'[FALLÓ] Obtuviste: {res_str}'}")

if __name__ == "__main__":
    ejecutar_tests()
