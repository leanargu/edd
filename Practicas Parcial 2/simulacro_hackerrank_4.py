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

        def esHoja(self):
            return not self.tieneIzquierdo() and not self.tieneDerecho()
            
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
# EJERCICIO 1: DICCIONARIOS - SUMA DE FRECUENCIAS COMUNES
# =========================================================================================
# Recibe un objeto Diccionario (self) y otro objeto Diccionario (otro).
# Ambos diccionarios guardan (palabra, frecuencia).
# Retornar un NUEVO TDA Diccionario que contenga SOLO las palabras que están en AMBOS.
# El valor de la palabra en el nuevo diccionario debe ser la SUMA de ambas frecuencias.
def sumarFrecuenciasComunes(self, otro) -> Diccionario:
    res = Diccionario()
    for key in self.keys():
        if key in otro.keys():
            res.insert(key, self[key] + otro[key])
    return res


Diccionario.sumarFrecuenciasComunes = sumarFrecuenciasComunes


# =========================================================================================
# EJERCICIO 2: LISTAS - ELIMINAR MAYORES A N
# =========================================================================================
# Recibe un número N. Debe eliminar de la lista todos los nodos cuyo dato sea MAYOR a N.
# Nota: La modificación se hace sobre la lista actual.
# ¡Ayudita!: Podés asumir que el primer nodo de la lista SIEMPRE es MENOR o IGUAL a N.
def eliminarMayoresA(self, N: int):
    nodoActual = self._Lista__primero
    while nodoActual.tiene_siguiente():
        if nodoActual.siguiente.dato > N:
            nodoActual.siguiente = nodoActual.siguiente.siguiente
        else:
            nodoActual = nodoActual.siguiente

Lista.eliminarMayoresA = eliminarMayoresA


# =========================================================================================
# EJERCICIO 3: ÁRBOLES - CONTAR HOJAS
# =========================================================================================
# Retornar la cantidad total de nodos "Hoja" que tiene el árbol (nodos sin hijos).
# Respetar la estructura de la cursada: método en el Nodo y método en el Árbol.

# 1. Método del Nodo
def contarHojas_nodo(self) -> int:
    cantidad = 0
    if self.esHoja():
        cantidad = 1
    else:
        if self.tieneIzquierdo():
            cantidad += self.izquierdo.contarHojas()
        if self.tieneDerecho():
            cantidad += self.derecho.contarHojas()
    return cantidad

ABB._ABB__NodoArbol.contarHojas = contarHojas_nodo

# 2. Método del Árbol
def contarHojas_arbol(self) -> int:
    if self._ABB__raiz is None:
        return 0
    else:
        return self._ABB__raiz.contarHojas()

ABB.contarHojas = contarHojas_arbol


# =========================================================================================
# TEST UNITARIOS
# =========================================================================================
def run_tests():
    ej_a_correr = None
    if len(sys.argv) > 1:
        ej_a_correr = sys.argv[1]

    print("==========================================================")
    print("ÚLTIMO REPASO ANTES DEL PARCIAL (3 PUNTOS CLAVE)")
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
            d1.insert("hola", 5)
            d1.insert("parcial", 2)
            d1.insert("hoy", 1)
            
            d2 = Diccionario()
            d2.insert("hola", 10)
            d2.insert("mañana", 3)
            d2.insert("parcial", 8)
            
            res = d1.sumarFrecuenciasComunes(d2)
            
            if res is not None and type(res) == Diccionario:
                dic_python = res.to_dict_python()
                esperado = {"hola": 15, "parcial": 10}
                if dic_python == esperado:
                    print("✅ Ejercicio 1: Sumar Comunes      -> PASS")
                    score += 33
                else:
                    print("❌ Ejercicio 1: Sumar Comunes      -> FAIL")
                    print(f"   Esperado: {esperado}")
                    print(f"   Obtenido: {dic_python}")
            else:
                print("❌ Ejercicio 1: Sumar Comunes      -> FAIL (Retornó None o no es TDA Diccionario)")
        except Exception as e:
            print("❌ Ejercicio 1: Sumar Comunes      -> EXCEPCIÓN:")
            traceback.print_exc()

    # Test Ejercicio 2
    if ej_a_correr is None or ej_a_correr == '2':
        max_score += 33
        try:
            lista = Lista()
            for x in [3, 8, 2, 9, 1, 10, 4]:
                lista.agregar_al_final(x)
            
            lista.eliminarMayoresA(5) 
            # Original: 3, 8, 2, 9, 1, 10, 4
            # Esperado: 3, 2, 1, 4
            
            res = lista.a_lista_python()
            esperado = [3, 2, 1, 4]
            if res == esperado:
                print("✅ Ejercicio 2: Eliminar Mayores   -> PASS")
                score += 33
            else:
                print("❌ Ejercicio 2: Eliminar Mayores   -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {res}")
        except Exception as e:
            print("❌ Ejercicio 2: Eliminar Mayores   -> EXCEPCIÓN:")
            traceback.print_exc()

    # Test Ejercicio 3
    if ej_a_correr is None or ej_a_correr == '3':
        max_score += 34
        try:
            arbol = ABB()
            #       20
            #      /  \
            #    10    30
            #   / \      \
            #  5  15     40
            for x in [20, 10, 30, 5, 15, 40]:
                arbol.insertar(x)
            
            res = arbol.contarHojas()
            esperado = 3 # Nodos 5, 15 y 40 son hojas
            
            if res == esperado:
                print("✅ Ejercicio 3: Contar Hojas       -> PASS")
                score += 34
            else:
                print("❌ Ejercicio 3: Contar Hojas       -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {res}")
        except Exception as e:
            print("❌ Ejercicio 3: Contar Hojas       -> EXCEPCIÓN:")
            traceback.print_exc()

    print("\n==========================================================")
    print(f"PUNTAJE FINAL: {score} / {max_score}")
    print("==========================================================")

if __name__ == '__main__':
    run_tests()
