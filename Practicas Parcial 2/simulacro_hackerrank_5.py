import sys
import traceback

# =========================================================================================
# TDA DICCIONARIO
# =========================================================================================
class Diccionario:
    def __init__(self):
        self.__datos = [] # Lista de tuplas (clave, valor)
    def insert(self, key, value):
        for i, (k, v) in enumerate(self.__datos):
            if k == key:
                self.__datos[i] = (key, value)
                return
        self.__datos.append((key, value))
    def __getitem__(self, key):
        for k, v in self.__datos:
            if k == key:
                return v
        raise KeyError(key)
    def hasKey(self, key):
        for k, v in self.__datos:
            if k == key: return True
        return False
    def remove(self, key):
        for i, (k, v) in enumerate(self.__datos):
            if k == key:
                self.__datos.pop(i)
                return
    def keys(self):
        return [k for k, v in self.__datos]
    def to_dict_python(self):
        return {k: v for k, v in self.__datos}

# =========================================================================================
# TDA LISTA
# =========================================================================================
class Lista:
    class __NodoLista:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None
        def tiene_siguiente(self):
            return self.siguiente is not None

    def __init__(self):
        self.__primero = None

    def esta_vacia(self):
        return self.__primero is None

    def agregar_al_final(self, dato):
        nuevo = self.__NodoLista(dato)
        if self.esta_vacia():
            self.__primero = nuevo
        else:
            aux = self.__primero
            while aux.tiene_siguiente():
                aux = aux.siguiente
            aux.siguiente = nuevo

    def a_lista_python(self):
        res = []
        aux = self.__primero
        while aux is not None:
            res.append(aux.dato)
            aux = aux.siguiente
        return res

# =========================================================================================
# TDA ÁRBOL (ABB)
# =========================================================================================
class ABB:
    class __NodoArbol:
        def __init__(self, dato):
            self.dato = dato
            self.izquierdo = None
            self.derecho = None
        
        def tieneIzquierdo(self):
            return self.izquierdo is not None
            
        def tieneDerecho(self):
            return self.derecho is not None
            
    def __init__(self):
        self.__raiz = None

    def estaVacio(self):
        return self.__raiz is None

    def insertar(self, dato):
        if self.estaVacio():
            self.__raiz = self.__NodoArbol(dato)
        else:
            self._insertar_recursivo(self.__raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.tieneIzquierdo():
                self._insertar_recursivo(nodo.izquierdo, dato)
            else:
                nodo.izquierdo = self.__NodoArbol(dato)
        elif dato > nodo.dato:
            if nodo.tieneDerecho():
                self._insertar_recursivo(nodo.derecho, dato)
            else:
                nodo.derecho = self.__NodoArbol(dato)


# =========================================================================================
# EJERCICIO 1: DICCIONARIOS - ELIMINAR CLAVES COMUNES
# =========================================================================================
# Recibe un Diccionario (self) y una lista de Python con claves.
# Debe eliminar del Diccionario (self) todas las claves que se encuentren en esa lista.
def eliminarClavesComunes(self, lista_claves):
    for key in lista_claves:
        self.remove(key)

Diccionario.eliminarClavesComunes = eliminarClavesComunes


# =========================================================================================
# EJERCICIO 2: LISTAS - INTERCAMBIAR EXTREMOS
# =========================================================================================
# Debe intercambiar el VALOR (.dato) del PRIMER nodo con el VALOR del ÚLTIMO nodo.
# Nota: Modificá solo los atributos ".dato", no hace falta cambiar los punteros.
# HINT DE SINTAXIS: Para acceder al primer nodo, usá -> self._Lista__primero
def intercambiarExtremos(self):
    nodoActual = self._Lista__primero
    valorPrimero = self._Lista__primero.dato
    while nodoActual.tiene_siguiente():
        nodoActual = nodoActual.siguiente
    self._Lista__primero.dato = nodoActual.dato
    nodoActual.dato = valorPrimero

Lista.intercambiarExtremos = intercambiarExtremos


# =========================================================================================
# EJERCICIO 3: ÁRBOLES - SUMAR NODOS PARES
# =========================================================================================
# Retornar la suma de todos los Nodos cuyo VALOR sea par (dato % 2 == 0).

# 1. Método del Nodo
# HINT DE SINTAXIS: Cuando te llames recursivamente usá -> self.izquierdo.sumarNodosPares()
def sumarNodosPares_nodo(self) -> int:
    suma = 0
    if not self.tieneIzquierdo() and not self.tieneDerecho():
        if self.dato % 2 == 0:
            suma += self.dato
    else:
        if self.dato % 2 == 0:
            suma += self.dato
        if self.tieneIzquierdo():
            suma += self.izquierdo.sumarNodosPares()
        if self.tieneDerecho():
            suma += self.derecho.sumarNodosPares()
    return suma

ABB._ABB__NodoArbol.sumarNodosPares = sumarNodosPares_nodo

# 2. Método del Árbol
# HINT DE SINTAXIS: Para acceder a la raiz, usá -> self._ABB__raiz
def sumarNodosPares_arbol(self) -> int:
    if self._ABB__raiz is None:
        return 0
    else:
        return self._ABB__raiz.sumarNodosPares()

ABB.sumarNodosPares = sumarNodosPares_arbol


# =========================================================================================
# TEST UNITARIOS
# =========================================================================================
def run_tests():
    ej_a_correr = None
    if len(sys.argv) > 1:
        ej_a_correr = sys.argv[1]

    print("==========================================================")
    print("ÚLTIMO REPASO PARTE 2: LA REVANCHA")
    if ej_a_correr:
        print(f"> Corriendo SOLAMENTE el Ejercicio {ej_a_correr} <")
    print("==========================================================\n")
    
    score = 0
    max_score = 0

    # Test Ejercicio 1
    if ej_a_correr is None or ej_a_correr == '1':
        max_score += 33
        try:
            d1 = Diccionario()
            d1.insert("manzana", 1)
            d1.insert("banana", 2)
            d1.insert("pera", 3)
            
            d1.eliminarClavesComunes(["banana", "kiwi"]) 
            # Deberia volar banana, y perdonarle la vida a kiwi porque no existe
            
            dic_python = d1.to_dict_python()
            esperado = {"manzana": 1, "pera": 3}
            if dic_python == esperado:
                print("✅ Ejercicio 1: Eliminar Claves    -> PASS")
                score += 33
            else:
                print("❌ Ejercicio 1: Eliminar Claves    -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {dic_python}")
        except Exception as e:
            print("❌ Ejercicio 1: Eliminar Claves    -> EXCEPCIÓN:")
            traceback.print_exc()

    # Test Ejercicio 2
    if ej_a_correr is None or ej_a_correr == '2':
        max_score += 33
        try:
            lista = Lista()
            for x in [10, 20, 30, 99]:
                lista.agregar_al_final(x)
            
            lista.intercambiarExtremos() 
            # Esperado: 99, 20, 30, 10
            
            res = lista.a_lista_python()
            esperado = [99, 20, 30, 10]
            if res == esperado:
                print("✅ Ejercicio 2: Intercambiar       -> PASS")
                score += 33
            else:
                print("❌ Ejercicio 2: Intercambiar       -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {res}")
        except Exception as e:
            print("❌ Ejercicio 2: Intercambiar       -> EXCEPCIÓN:")
            traceback.print_exc()

    # Test Ejercicio 3
    if ej_a_correr is None or ej_a_correr == '3':
        max_score += 34
        try:
            arbol = ABB()
            #       20
            #      /  \
            #    11    32
            #   / \      \
            #  4  15     40
            for x in [20, 11, 32, 4, 15, 40]:
                arbol.insertar(x)
            
            res = arbol.sumarNodosPares()
            esperado = 96 # 20 + 32 + 4 + 40 = 96 (El 11 y el 15 son impares)
            
            if res == esperado:
                print("✅ Ejercicio 3: Sumar Pares        -> PASS")
                score += 34
            else:
                print("❌ Ejercicio 3: Sumar Pares        -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {res}")
        except Exception as e:
            print("❌ Ejercicio 3: Sumar Pares        -> EXCEPCIÓN:")
            traceback.print_exc()

    print("\n==========================================================")
    print(f"PUNTAJE FINAL: {score} / {max_score}")
    print("==========================================================")

if __name__ == '__main__':
    run_tests()
