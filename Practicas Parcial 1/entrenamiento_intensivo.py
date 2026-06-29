import numpy as np

# =============================================================================
# ENTRENAMIENTO INTENSIVO PRE-PARCIAL (Nivel UnaHur)
# =============================================================================

# -----------------------------------------------------------------------------
# EJERCICIO 1: RECURSIVIDAD CON LÓGICA DOBLE
# Consigna: Implementar la función recursiva 'suma_pares_mayores(vector, limite)'
# que devuelva la suma de todos los números que sean PARES y además sean
# estrictamente MAYORES al 'limite' recibido.
# REGLA: Single Return.
# -----------------------------------------------------------------------------

def es_mayor_y_par(nro_actual, limite):
    return nro_actual > limite and nro_actual % 2 == 0
#[2, 10, 5, 8, 20]
def suma_pares_mayores(vector: np.array, limite: int) -> int:
    res = 0
    numero_actual = vector[0]
    """
    if len(vector) == 0:
        return 0
    """
    if len(vector) == 1:
        if es_mayor_y_par(numero_actual, limite):
            res += numero_actual
    else:
        if es_mayor_y_par(numero_actual, limite):
            res += numero_actual
        res += suma_pares_mayores(vector[1:], limite)
        #res = (vector[0] if es_mayor_y_par(vector, limite) else 0) + suma_pares_mayores(vector[1:], limite)
    return res





# -----------------------------------------------------------------------------
# EJERCICIO 2: TDA "DEPOSITO" (MATRICES + REGLAS DE UBICACIÓN)
# Consigna: Modelar un Depósito que organiza 'Cajas' en una matriz de NxM.
# 
# Requisitos:
# 1. Clase Caja: peso (float), es_fragil (bool).
# 2. Clase Deposito:
#    - __init__(filas, columnas): Matriz de objetos Caja (None por defecto).
#    - almacenar(f, c, caja): Ubica la caja. 
#      REGLA DE ORO: Las cajas FRÁGILES solo pueden ir en las columnas centrales 
#      (no pueden ir ni en la primera ni en la última columna).
#      Lanzar Exception si no cumple la regla, si el lugar está ocupado o fuera de rango.
#    - peso_total_recursivo(fila_vector): Función que recibe UNA FILA (vector)
#      y devuelve la suma de los pesos de las cajas de forma RECURSIVA.
# -----------------------------------------------------------------------------

class Caja:
    def __init__(self, peso: float, es_fragil: bool):
        self.peso = peso
        self.es_fragil = es_fragil


class Deposito:
    def __init__(self, filas: int, columnas: int):
        self.__estanteria = np.full((filas, columnas), None, dtype=object)

    def almacenar(self, f: int, c: int, caja: Caja):
        if self.__son_cordenadas_validas(f, c):
            self.__estanteria[f][c] = caja
        else:
            raise Exception("Las coordenadas no son validas")

    def __son_cordenadas_validas(self, f, c):
        size_fil, size_col = self.__estanteria.shape
        return (f < size_fil and f < len(self.__estanteria) and c < size_col and  c < len(self.__estanteria) and not self.__estanteria[f][c]
                and (f > 0 or c > 0) )



    def obtener_peso_fila(self, n_fila: int) -> float:
        # Esta función debe llamar a la recursiva pasando la fila completa
        fila_a_procesar = self.__estanteria[n_fila]
        return self.__sumar_pesos_rec(fila_a_procesar)

    def __sumar_pesos_rec(self, vector_fila) -> float:
        res = 0.0
        if len(vector_fila) == 1:
            res = vector_fila[0] if vector_fila[0] != None else 0
        else:
            res = vector_fila[0] if vector_fila[0] != None else 0 + self.__sumar_pesos_rec(vector_fila[1:])
        return res

# -----------------------------------------------------------------------------
# EJERCICIO 3: RECURSIVIDAD DE STRINGS (COMPRESIÓN)
# Consigna: Implementar la función 'comprimir_mensaje(cadena)' que reciba un
# string y devuelva uno nuevo eliminando los caracteres REPETIDOS CONSECUTIVOS.
# Ejemplo: "aaabbc" -> "abc" | "holaaa" -> "hola"
# REGLA: Single Return.
# -----------------------------------------------------------------------------

def comprimir_mensaje(cadena: str) -> str:
    res = ""
    # TODO: Implementar comparando cadena[0] con cadena[1] antes de recursear
    # [a,a,a,b,b,c]
    # [b,c] -> [a,a,a,b,b]

    if len(cadena) == 1:
        res = cadena[0]
    if len(cadena) == 2:
        if cadena[0] != cadena[1]:
            res = cadena
    else:
        if cadena[1] != cadena[0]:
            res += cadena[0]
        res += comprimir_mensaje(cadena[1:])

    """
    if len(cadena) == 1:
        res = cadena
    if len(cadena) == 2:
        res += cadena[0] if cadena[0] != cadena[1] else res
    else:
        res = (res + cadena[0] if cadena[0] != cadena[1] else res) + comprimir_mensaje(cadena[1:])
    """
    return res

# =============================================================================
# TESTS DE AUTOCORRECCIÓN
# =============================================================================

def test_entrenamiento():
    print("--- INICIANDO TEST ENTRENAMIENTO INTENSIVO ---")
    
    # Test 1: Suma condicionada
    v = np.array([2, 10, 5, 8, 20])
    # Pares > 9: 10, 20 -> Suma: 30
    if suma_pares_mayores(v, 9) == 30:
        print("Ejer 1 (Recursividad): [OK]")
    else:
        print("Ejer 1 (Recursividad): [FALLÓ]")

    # Test 2: TDA Depósito
    try:
        depo = Deposito(3, 3)
        caja_normal = Caja(10.0, False)
        caja_fragil = Caja(5.0, True)
        
        depo.almacenar(0, 1, caja_fragil) # Columna central: OK
        try:
            depo.almacenar(0, 0, caja_fragil) # Columna extremo: DEBE FALLAR
            print("Ejer 2 (Regla Fragilidad): [FALLÓ - No lanzó excepción]")
        except Exception:
            print("Ejer 2 (Regla Fragilidad): [OK]")
            
    except Exception as e:
        print(f"Ejer 2 (TDA): [ERROR] {e}")

    # Test 3: Compresión
    if comprimir_mensaje("aaabbc") == "abc":
        print("Ejer 3 (Compresión): [OK]")
    else:
        print(f"Ejer 3 (Compresión): [FALLÓ] Obtuviste: {comprimir_mensaje('aaabbc')}")

if __name__ == "__main__":
    test_entrenamiento()
    print(comprimir_mensaje("cccccdddffg"))
