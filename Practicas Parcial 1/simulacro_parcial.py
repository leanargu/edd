import numpy as np

# =============================================================================
# EJERCICIO 1: RECURSIVIDAD CON ARREGLOS
# Consigna: Implementar la función recursiva 'contar_pares' que recibe un 
# arreglo de enteros y retorna la cantidad de números pares que contiene.
# REGLA: No usar bucles (for/while). Solo recursividad.
# =============================================================================

def contar_pares(vector: np.array) -> int:
    contador = 0
    if vector.size == 1:
        if vector[0] % 2 == 0:
            contador += 1
    else:
        a_sumar = 1 if vector[0] % 2 == 0 else 0
        contador = a_sumar + contar_pares(vector[1:])
    return contador
# =============================================================================
# EJERCICIO 2: TDA Y RECORRIDOS (MATRICES)
# Consigna: Implementar el TDA 'Cine'. La sala es una matriz de objetos 'Espectador'.
# Se pide el método 'contar_menores_en_fila' que recibe el número de una fila
# y retorna cuántos espectadores menores de 18 años hay en esa fila.
# REGLAS: Un solo return, Null-Safe (asientos vacíos son None), Validación de límites.
# =============================================================================

class Espectador:
    def __init__(self, nombre: str, edad: int):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_edad(self):
        return self.__edad

class Cine:
    def __init__(self, filas: int, columnas: int):
        # Matriz vacía (llena de None)
        self.__sala = np.full((filas, columnas), None, dtype=object)
    
    def ocupar_asiento(self, f, c, espectador: Espectador):
        # Validación de límites para no romper el programa
        n_f, n_c = self.__sala.shape
        if 0 <= f < n_f and 0 <= c < n_c:
            self.__sala[f][c] = espectador

    def contar_menores_en_fila(self, n_fila: int) -> int:
        menores_en_fila = 0
        longitud_fila = self.__sala.shape[1]
        if n_fila < longitud_fila:
            for espectador in self.__sala[n_fila]:
                if espectador and espectador.get_edad() < 18:
                    menores_en_fila += 1
        return menores_en_fila

# =============================================================================
# TESTS DE VALIDACIÓN (Ejecutar para verificar)
# =============================================================================

def test_simulacro():
    print("--- INICIANDO TESTS DE SIMULACRO ---")
    
    # Test Ejercicio 1 (Recursividad)
    v_test = np.array([2, 5, 8, 10, 11])
    # Se espera: 2, 8, 10 -> Total: 3
    actual_1 = contar_pares(v_test)
    expected_1 = 3
    
    if actual_1 == expected_1:
        print("EJERCICIO 1: [OK]")
    else:
        print(f"EJERCICIO 1: [FALLÓ] (Esperaba {expected_1}, obtuviste {actual_1})")

    # Test Ejercicio 2 (TDA)
    cine_unahur = Cine(3, 3)
    cine_unahur.ocupar_asiento(0, 0, Espectador("Ana", 25))
    cine_unahur.ocupar_asiento(0, 1, Espectador("Pedro", 15)) # Menor
    cine_unahur.ocupar_asiento(0, 2, None) # Vacío
    
    # Se espera en fila 0: 1 menor
    actual_2 = cine_unahur.contar_menores_en_fila(0)
    expected_2 = 1
    
    if actual_2 == expected_2:
        print("EJERCICIO 2: [OK]")
    else:
        print(f"EJERCICIO 2: [FALLÓ] (Esperaba {expected_2}, obtuviste {actual_2})")

    # Test Ejercicio 2 (Límites)
    actual_3 = cine_unahur.contar_menores_en_fila(10) # Fila inexistente
    if actual_3 == 0: # O lanzar excepción, depende de cómo lo manejes
        print("EJERCICIO 2 (Límites): [OK]")
    else:
        print("EJERCICIO 2 (Límites): [FALLÓ]")

if __name__ == "__main__":
    test_simulacro()
