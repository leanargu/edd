import sys
import traceback

# =========================================================================================
# TDAs SIMPLIFICADOS PARA QUE LOS TESTS CORRAN (IGUALES A LOS VISTOS EN CLASE)
# =========================================================================================

class Diccionario:
    def __init__(self, keys=None, values=None):
        self._items = {}
        if keys and values:
            for k, v in zip(keys, values):
                self._items[k] = v
        
    def __setitem__(self, key, value):
        self._items[key] = value
        
    def __getitem__(self, key):
        if key not in self._items:
            raise Exception(f"key: {key} not in dict")
        return self._items[key]
        
    def get(self, key):
        return self[key]

    def insert(self, key, value):
        self._items[key] = value
        
    def remove(self, key):
        if key in self._items:
            return self._items.pop(key)
        return None
        
    def keys(self):
        return list(self._items.keys())
        
    def values(self):
        return list(self._items.values())
        
    def __contains__(self, key):
        return key in self._items
        
    def len(self):
        return len(self._items)
        
    def __repr__(self):
        return str(self._items)
class Lista:
    class __NodoLista:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
        def tiene_siguiente(self):
            return self.siguiente is not None
            
        def __repr__(self):
            return str(self.dato)

    def __init__(self):
        self.__primero = None

    def esta_vacia(self):
        return self.__primero is None

    def agregar_al_final(self, dato):
        nuevo = Lista.__NodoLista(dato)
        if self.esta_vacia():
            self.__primero = nuevo
        else:
            aux = self.__primero
            while aux.tiene_siguiente():
                aux = aux.siguiente
            aux.siguiente = nuevo
class ABB:
    class __NodoArbol:
        def __init__(self, dato):
            self.dato = dato
            self.izquierdo = None
            self.derecho = None

        def tieneIzquierdo(self) -> bool:
            return self.izquierdo is not None

        def tieneDerecho(self) -> bool:
            return self.derecho is not None

        def esHoja(self) -> bool:
            return not self.tieneIzquierdo() and not self.tieneDerecho()

    def __init__(self):
        self.__raiz = None

    def estaVacio(self):
        return self.__raiz is None

    def insertar(self, dato):
        if self.estaVacio():
            self.__raiz = ABB.__NodoArbol(dato)
        else:
            self._insertar_recursivo(self.__raiz, dato)
            
    def _insertar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.tieneIzquierdo():
                self._insertar_recursivo(nodo.izquierdo, dato)
            else:
                nodo.izquierdo = ABB.__NodoArbol(dato)
        elif dato > nodo.dato:
            if nodo.tieneDerecho():
                self._insertar_recursivo(nodo.derecho, dato)
            else:
                nodo.derecho = ABB.__NodoArbol(dato)


# =========================================================================================
# EJERCICIO 1: RESTA DE DICCIONARIOS (TDA DICCIONARIO)
# =========================================================================================
# Escribir la función resta que recibe dos diccionarios como parámetro (dic1 y dic2) y retorna 
# un nuevo TDA Diccionario con la resta de los dos, con el siguiente criterio:
# - Cuando una clave sólo está en el dic1, pasa al diccionario de salida con el significado original.
# - Si una clave está en ambos diccionarios (dic1 y dic2), no pasa al diccionario de salida.
# Se debe resolver usando las operaciones del TDA Diccionario, sin diccionarios de Python.
def resta(dic1: Diccionario, dic2: Diccionario) -> Diccionario:
    res = Diccionario()
    for key in dic1.keys():
        if key not in dic2.keys():
            res.insert(key, dic1[key])

    return res


# =========================================================================================
# EJERCICIO 2: ELIMINAR IMPARES (TDA LISTA)
# =========================================================================================
# Escribir una operación del TDA Lista que tome una lista y elimine todos los elementos impares.
# La operación NO debe retornar una nueva lista, sino modificar la lista con la cual se llama a la función. 
# Nota: No se puede utilizar la operación eliminar del TDA lista y el primer elemento siempre es par.
def eliminar_impares(self):
    nodoActual = self._Lista__primero
    while nodoActual.tiene_siguiente():
        if nodoActual.siguiente.dato % 2 == 1:
            nodoActual.siguiente = nodoActual.siguiente.siguiente
        else:
            nodoActual = nodoActual.siguiente


Lista.eliminar_impares = eliminar_impares


# =========================================================================================
# EJERCICIO 3: SUMA HASTA NIVEL (TDA ABB)
# =========================================================================================
# Escribir la operación sumaHastaNivel del TDA ABB que recibe un nivel N por parámetro y 
# retorna la suma de todos los números en el ABB en nodos que estén a nivel menor o igual a N. 
# La raíz se encuentra en el nivel 0.

# 1. MÉTODO PARA EL NODO
def sumaHastaNivel_nodo(self, N: int, nivel_actual: int) -> int:
    suma = None
    if nivel_actual > N:
        suma = 0
    else:
        suma = self.dato
        if self.tieneIzquierdo():
            suma += self.izquierdo.sumaHastaNivel(N, nivel_actual+1)
        if self.tieneDerecho():
            suma += self.derecho.sumaHastaNivel(N, nivel_actual + 1)
    return suma


ABB._ABB__NodoArbol.sumaHastaNivel = sumaHastaNivel_nodo

# 2. MÉTODO PARA EL ÁRBOL
def sumaHastaNivel_arbol(self, N: int) -> int:
    if self._ABB__raiz is None:
        return 0
    else:
        return self._ABB__raiz.sumaHastaNivel(N,0)

ABB.sumaHastaNivel = sumaHastaNivel_arbol


# =========================================================================================
# EJERCICIO 4: ELIMINAR SEGMENTO (TDA LISTA)
# =========================================================================================
# Escribir la operación eliminarSegmento del TDA Lista, que recibe dos posiciones ("inicio" y "final") 
# como entrada y elimina todos los nodos en la lista entre ambas (incluidas). 
# Las posiciones comienzan en 1 (el primer nodo es la posición 1).
# Si la posición "final" es más grande que el tamaño de la lista, se eliminan todos hasta el final.
# Se puede asumir que la lista arranca desde la posición 1 y "final" es mayor o igual que "inicio".
def eliminarSegmento(self, inicio: int, final: int):
    nodoActual = self._Lista__primero
    posicion = 1
    nodoAnterior = None
    nodoRestante = None
    while nodoActual.tiene_siguiente():
        if posicion == inicio - 1:
            nodoAnterior = nodoActual
        elif posicion == final:
            nodoRestante = nodoActual.siguiente
        posicion += 1
        nodoActual = nodoActual.siguiente
    nodoAnterior.siguiente = nodoRestante

Lista.eliminarSegmento = eliminarSegmento


# =========================================================================================
# TEST UNITARIOS AL ESTILO HACKERRANK
# =========================================================================================
def run_tests():
    ej_a_correr = None
    if len(sys.argv) > 1:
        ej_a_correr = sys.argv[1]

    print("==========================================================")
    print("Iniciando pruebas - Simulacro Parcial 2 (Parte 2)")
    if ej_a_correr:
        print(f"> Corriendo SOLAMENTE el Ejercicio {ej_a_correr} <")
    print("==========================================================\n")
    score = 0
    max_score = 0

    # Test Ejercicio 1
    if ej_a_correr is None or ej_a_correr == '1':
        max_score += 25
        try:
            dic1 = Diccionario([1, 3, 8, 4, 2], [4, 6, 14, 12, 6])
            dic2 = Diccionario([8, 10, 1, 2, 14], [5, 6, 7, 9, 8])
            res = resta(dic1, dic2)
            
            if type(res) != Diccionario:
                print(f"❌ Ejercicio 1: Resta Diccionarios   -> FAIL (El tipo devuelto no es Diccionario)")
            else:
                errores = []
                if not (3 in res and res[3] == 6): errores.append("Falta clave 3 o su valor es incorrecto (debería ser 6)")
                if not (4 in res and res[4] == 12): errores.append("Falta clave 4 o su valor es incorrecto (debería ser 12)")
                
                sobrantes = [k for k in res.keys() if k not in [3, 4]]
                if sobrantes: errores.append(f"Claves sobrantes (no deberían estar): {sobrantes}")
                
                if len(errores) == 0:
                    print("✅ Ejercicio 1: Resta Diccionarios   -> PASS (25 pts)")
                    score += 25
                else:
                    print(f"❌ Ejercicio 1: Resta Diccionarios   -> FAIL")
                    for err in errores: print(f"     - {err}")
                    print(f"   Diccionario devuelto: {res}")
        except Exception as e:
            print(f"❌ Ejercicio 1: Resta Diccionarios   -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    # Test Ejercicio 2
    if ej_a_correr is None or ej_a_correr == '2':
        max_score += 25
        try:
            lista = Lista()
            for elem in [2, 3, 5, 8, 1, 9, 4, 10]:
                lista.agregar_al_final(elem)
            
            lista.eliminar_impares()
            
            resultado = []
            aux = lista._Lista__primero
            while aux:
                resultado.append(aux.dato)
                aux = aux.siguiente
                
            esperado = [2, 8, 4, 10]
            if resultado == esperado:
                print("✅ Ejercicio 2: Eliminar Impares     -> PASS (25 pts)")
                score += 25
            else:
                print(f"❌ Ejercicio 2: Eliminar Impares     -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {resultado}")
        except Exception as e:
            print(f"❌ Ejercicio 2: Eliminar Impares     -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    # Test Ejercicio 3
    if ej_a_correr is None or ej_a_correr == '3':
        max_score += 25
        try:
            arbol = ABB()
            # Nivel 0: 50
            # Nivel 1: 30, 70
            # Nivel 2: 20, 40, 60, 80
            for x in [50, 30, 70, 20, 40, 60, 80]:
                arbol.insertar(x)
            
            test_nivel_0 = arbol.sumaHastaNivel(0) # 50
            test_nivel_1 = arbol.sumaHastaNivel(1) # 50 + 30 + 70 = 150
            test_nivel_2 = arbol.sumaHastaNivel(2) # 150 + 20 + 40 + 60 + 80 = 350
            test_nivel_10 = arbol.sumaHastaNivel(10) # 350

            if test_nivel_0 == 50 and test_nivel_1 == 150 and test_nivel_2 == 350 and test_nivel_10 == 350:
                print("✅ Ejercicio 3: Suma Hasta Nivel     -> PASS (25 pts)")
                score += 25
            else:
                print(f"❌ Ejercicio 3: Suma Hasta Nivel     -> FAIL")
                print(f"   Esperado: N0=50, N1=150, N2=350, N10=350")
                print(f"   Obtenido: N0={test_nivel_0}, N1={test_nivel_1}, N2={test_nivel_2}, N10={test_nivel_10}")
        except Exception as e:
            print(f"❌ Ejercicio 3: Suma Hasta Nivel     -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    # Test Ejercicio 4
    if ej_a_correr is None or ej_a_correr == '4':
        max_score += 25
        try:
            lista = Lista()
            # 1  2  3  4  5  6  7  8  9
            # 3, 5, 8, 2, 6, 7, 5, 8, 2
            for elem in [3, 5, 8, 2, 6, 7, 5, 8, 2]:
                lista.agregar_al_final(elem)
            
            lista.eliminarSegmento(2, 5) 
            # Debería quedar: 3, (eliminados 5, 8, 2, 6), 7, 5, 8, 2
            
            resultado = []
            aux = lista._Lista__primero
            while aux:
                resultado.append(aux.dato)
                aux = aux.siguiente
                
            esperado = [3, 7, 5, 8, 2]
            
            if resultado == esperado:
                # Test de posición final mayor que el largo
                lista2 = Lista()
                for elem in [3, 5, 8, 2]:
                    lista2.agregar_al_final(elem)
                lista2.eliminarSegmento(2, 50) # Elimina desde el 5 hasta el final
                
                res2 = []
                aux2 = lista2._Lista__primero
                while aux2:
                    res2.append(aux2.dato)
                    aux2 = aux2.siguiente
                if res2 == [3]:
                    print("✅ Ejercicio 4: Eliminar Segmento    -> PASS (25 pts)")
                    score += 25
                else:
                    print(f"❌ Ejercicio 4: Eliminar Segmento    -> FAIL (Falla cuando final es mayor al tamaño)")
                    print(f"   Esperado: [3]\n   Obtenido: {res2}")
            else:
                print(f"❌ Ejercicio 4: Eliminar Segmento    -> FAIL (Falla segmento intermedio)")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {resultado}")
        except Exception as e:
            print(f"❌ Ejercicio 4: Eliminar Segmento    -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    print("\n==========================================================")
    print(f"PUNTAJE FINAL: {score} / {max_score}")
    print("==========================================================")
    if score == max_score and max_score > 0:
        print("¡Tremendo! Sos una máquina. ¡Estás preparado para mañana!")
    else:
        print("Aún hay detalles por arreglar. ¡Sigue practicando, tú puedes!")

if __name__ == '__main__':
    run_tests()
