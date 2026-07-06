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
# EJERCICIO 1: INTERSECCIÓN DE DICCIONARIOS (TDA DICCIONARIO)
# =========================================================================================
# Escribir una función que calcule la intersección de dos diccionarios (usando el TDA Diccionario):
# - Si una clave está en ambos diccionarios, en la intersección el significado de dicha clave 
#   es una tupla con los valores de ambos diccionarios (dic1_val, dic2_val).
# - Si una clave está en uno solo de los diccionarios, no formará parte de la intersección.
# Se debe devolver un nuevo TDA Diccionario y NO se pueden usar diccionarios nativos de Python.
def interseccion(dic1: Diccionario, dic2: Diccionario) -> Diccionario:
    res = Diccionario()
    for key in dic1.keys():
        if key in dic2.keys():
            res.insert(key, (dic1.get(key), dic2.get(key)))
    return res


# =========================================================================================
# EJERCICIO 2: MAXIMO POR NUMERO (TDA DICCIONARIO)
# =========================================================================================
# Escribir la función maximoPorNumero que recibe una lista de pares (x,y) que indica que el 
# número x está asociado al valor y.
# Se debe devolver un TDA Diccionario con clave x y significado (valor) y, donde y sea el 
# máximo valor asociado a x.
# Se debe resolver usando las operaciones del TDA Diccionario.
def maximoPorNumero(lista: list) -> Diccionario:
    dic = Diccionario()
    for par in lista:
        if par[0] in dic.keys():
            if dic.get(par[0]) < par[1]:
                dic.insert(par[0], par[1])
        else:
            dic.insert(par[0], par[1])
    return dic


# =========================================================================================
# EJERCICIO 3: INSERTAR CEROS (TDA LISTA)
# =========================================================================================
# Crear la operación insertarCeros del TDA Lista, que inserte un 0 (cero) entre 2 números 
# pares consecutivos. La función no debe crear una nueva lista, debe modificar la lista self.
# No se pueden utilizar las operaciones insertar y append. 
# Acceder a self._Lista__primero y trabajar con los nodos (siguiente, dato, tiene_siguiente).
def insertarCeros(self):
    nodoActual = self._Lista__primero
    while nodoActual.tiene_siguiente():
        if nodoActual.dato % 2 == 0 and nodoActual.siguiente.dato % 2 == 0:
            siguiente = nodoActual.siguiente
            nodoCero = self._Lista__NodoLista(0)
            nodoCero.siguiente = siguiente
            nodoActual.siguiente = nodoCero
            nodoActual = nodoActual.siguiente.siguiente
        else:
            nodoActual = nodoActual.siguiente


Lista.insertarCeros = insertarCeros


# =========================================================================================
# EJERCICIO 4: SUMA INTERNOS MENORES (TDA ABB y NODO)
# =========================================================================================
# Escribir la operación sumaInternosMenores del TDA ABB que devuelva la suma de los elementos 
# de los nodos internos (NO son hojas) del árbol que son menores a un valor N que se recibe por parámetro. 
# La función puede hacer uso de las siguientes operaciones del TDA ABB: estaVacio y 
# del TDA NodoArbol: tieneIzquierdo, tieneDerecho y esHoja.
# Hint: Probablemente necesites hacer una función recursiva oculta.
def sumaInternosMenores(self, N: int) -> int:
    if self.estaVacio():
        return 0
    return self._ABB__raiz.suma_desde_nodo(N)

def suma_desde_nodo(self_nodo, N):
    suma = 0
    if self_nodo.esHoja():
        suma = 0
    else:
        if self_nodo.dato < N:
            suma += self_nodo.dato
        suma += suma_desde_nodo(self_nodo.izquierdo, N)
        suma += suma_desde_nodo(self_nodo.derecho, N)
    return suma



ABB._ABB__NodoArbol.suma_desde_nodo = suma_desde_nodo
ABB.sumaInternosMenores = sumaInternosMenores


# =========================================================================================
# TEST UNITARIOS AL ESTILO HACKERRANK
# =========================================================================================
def run_tests():
    ej_a_correr = None
    if len(sys.argv) > 1:
        ej_a_correr = sys.argv[1]

    print("==========================================================")
    print("Iniciando pruebas de HackerRank - Simulacro Parcial 2")
    if ej_a_correr:
        print(f"> Corriendo SOLAMENTE el Ejercicio {ej_a_correr} <")
    print("==========================================================\n")
    score = 0
    max_score = 0

    # Test Ejercicio 1
    if ej_a_correr is None or ej_a_correr == '1':
        max_score += 25
        try:
            dic1 = Diccionario([1, 20, 8, 10, 5], ["casa", "perro", "gato", "mate", "auto"])
            dic2 = Diccionario([5, 2, 8, 15, 20], [3, 15, 20, 1, 25])
            res = interseccion(dic1, dic2)
            
            if type(res) != Diccionario:
                print(f"❌ Ejercicio 1: Intersección -> FAIL (El tipo devuelto no es Diccionario, es {type(res)})")
            else:
                errores = []
                # Verificamos si estan las claves correctas y los valores correctos
                if not (20 in res and res[20] == ("perro", 25)): errores.append("Falta clave 20 o su valor es incorrecto")
                if not (8 in res and res[8] == ("gato", 20)): errores.append("Falta clave 8 o su valor es incorrecto")
                if not (5 in res and res[5] == ("auto", 3)): errores.append("Falta clave 5 o su valor es incorrecto")
                
                sobrantes = [k for k in [1, 10, 2, 15] if k in res]
                if sobrantes: errores.append(f"Claves sobrantes (debería ser intersección): {sobrantes}")
                
                if len(errores) == 0:
                    print("✅ Ejercicio 1: Intersección             -> PASS (25 pts)")
                    score += 25
                else:
                    print(f"❌ Ejercicio 1: Intersección             -> FAIL")
                    print("   Detalle de errores:")
                    for err in errores: print(f"     - {err}")
                    print(f"   Diccionario devuelto: {res}")
        except Exception as e:
            print(f"❌ Ejercicio 1: Intersección             -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    # Test Ejercicio 2
    if ej_a_correr is None or ej_a_correr == '2':
        max_score += 25
        try:
            lista_pares = [(1,4), (2,5), (1,5), (3,8), (2,1), (2,5)]
            res = maximoPorNumero(lista_pares)
            
            if type(res) != Diccionario:
                print(f"❌ Ejercicio 2: Maximo Por Numero -> FAIL (No retornó un Diccionario)")
            else:
                errores = []
                if not (1 in res and res[1] == 5): errores.append("La clave 1 debería tener máximo 5")
                if not (2 in res and res[2] == 5): errores.append("La clave 2 debería tener máximo 5")
                if not (3 in res and res[3] == 8): errores.append("La clave 3 debería tener máximo 8")
                
                if len(errores) == 0:
                    print("✅ Ejercicio 2: Maximo Por Numero        -> PASS (25 pts)")
                    score += 25
                else:
                    print(f"❌ Ejercicio 2: Maximo Por Numero        -> FAIL")
                    for err in errores: print(f"     - {err}")
                    print(f"   Diccionario devuelto: {res}")
        except Exception as e:
            print(f"❌ Ejercicio 2: Maximo Por Numero        -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    # Test Ejercicio 3
    if ej_a_correr is None or ej_a_correr == '3':
        max_score += 25
        try:
            lista = Lista()
            for elem in [1, 3, 4, 6, 8, 1, 5, 8, 10, 7]:
                lista.agregar_al_final(elem)
            lista.insertarCeros()
            
            resultado = []
            aux = lista._Lista__primero
            while aux:
                resultado.append(aux.dato)
                aux = aux.siguiente
                
            esperado = [1, 3, 4, 0, 6, 0, 8, 1, 5, 8, 0, 10, 7]
            if resultado == esperado:
                print("✅ Ejercicio 3: Insertar Ceros           -> PASS (25 pts)")
                score += 25
            else:
                print(f"❌ Ejercicio 3: Insertar Ceros           -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {resultado}")
        except Exception as e:
            print(f"❌ Ejercicio 3: Insertar Ceros           -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    # Test Ejercicio 4
    if ej_a_correr is None or ej_a_correr == '4':
        max_score += 25
        try:
            arbol = ABB()
            for x in [50, 30, 70, 20, 40, 60, 80]:
                arbol.insertar(x)
            
            test1 = arbol.sumaInternosMenores(60) 
            test2 = arbol.sumaInternosMenores(30)
            test3 = arbol.sumaInternosMenores(100)

            if test1 == 80 and test2 == 0 and test3 == 150:
                print("✅ Ejercicio 4: Suma Internos Menores    -> PASS (25 pts)")
                score += 25
            else:
                print(f"❌ Ejercicio 4: Suma Internos Menores    -> FAIL")
                print(f"   Esperado: test1=80, test2=0, test3=150")
                print(f"   Obtenido: test1={test1}, test2={test2}, test3={test3}")
        except Exception as e:
            print(f"❌ Ejercicio 4: Suma Internos Menores    -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    print("\n==========================================================")
    print(f"PUNTAJE FINAL: {score} / {max_score}")
    print("==========================================================")
    if score == max_score and max_score > 0:
        print("¡Excelente! Pasaste las pruebas solicitadas. ¡Éxitos!")
    else:
        print("Aún hay detalles por arreglar. ¡Sigue practicando, tú puedes!")

if __name__ == '__main__':
    run_tests()
