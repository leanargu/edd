import numpy as np

# =============================================================================
# PRÁCTICA DE RECURSIÓN: PATRÓN "LOOK-AHEAD" (MIRAR AL VECINO)
# Regla de Oro: Single Return y variable 'res'.
# =============================================================================

# -----------------------------------------------------------------------------
# EJERCICIO 1: EL SENSOR DE VUELO (Diferencias Críticas)
# Consigna: Un dron registra su altura cada segundo en un vector. El vuelo es 
# SEGURO si la diferencia de altura entre un segundo y el siguiente NUNCA 
# supera los 10 metros.
# Implementar la función recursiva 'vuelo_seguro(alturas: np.array) -> bool'.
# -----------------------------------------------------------------------------

def vuelo_seguro(alturas: np.array) -> bool:
    res = None
    ...
    return res

# -----------------------------------------------------------------------------
# EJERCICIO 2: EL INSPECTOR DE CALIDAD (Contador de Fallas Duplicadas)
# Consigna: En una línea de montaje, los productos pasan con un código de error.
# Si un código de error se REPITE dos veces seguidas, es una "Falla Crítica".
# Implementar la función 'contar_fallas_criticas(codigos: np.array) -> int' que
# cuente cuántas duplas de errores iguales hay.
# Ejemplo: [1, 2, 2, 3, 3, 3] -> 3 (el 2-2 una vez, el 3-3 dos veces).
# -----------------------------------------------------------------------------

def contar_fallas_criticas(codigos: np.array) -> int:
    res = 0
    ...
    return res

# -----------------------------------------------------------------------------
# EJERCICIO 3: EL CAMINO DEL REY (Tendencia Estricta)
# Consigna: Un camino es "Ascendente" si CADA paso es estrictamente MAYOR 
# al anterior. Implementar 'es_ascendente(pasos: np.array) -> bool'.
# Ejemplo: [1, 3, 5, 8] -> True | [1, 3, 3, 5] -> False
# -----------------------------------------------------------------------------

def es_ascendente(pasos: np.array) -> bool:
    res = None
    ...
    return res

# =============================================================================
# TESTS PARA PRACTICAR
# =============================================================================

def ejecutar_tests():
    print("--- TESTS RECURSIÓN AVANZADA ---")
    
    # Test 1
    vuelo = np.array([100, 105, 112, 110]) # Diferencias: 5, 7, 2 -> OK
    print(f"Ejer 1 (Vuelo): {'[OK]' if vuelo_seguro(vuelo) else '[FALLÓ]'}")

    # Test 2
    fallas = np.array([5, 5, 1, 2, 2, 2]) # 5-5 (1), 2-2 (1), 2-2 (1) -> Total 3
    if contar_fallas_criticas(fallas) == 3:
        print("Ejer 2 (Fallas): [OK]")
    else:
        print(f"Ejer 2 (Fallas): [FALLÓ] Obtuviste {contar_fallas_criticas(fallas)}")

    # Test 3 (Este lo completás vos)
    camino = np.array([1, 5, 10, 15])
    # print(f"Ejer 3 (Camino): {'[OK]' if es_ascendente(camino) else '[FALLÓ]'}")

if __name__ == "__main__":
    ejecutar_tests()
