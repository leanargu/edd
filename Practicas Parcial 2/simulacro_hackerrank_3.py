import sys
import traceback

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
# EJERCICIO 1: INSERTAR EN POSICIÓN (TDA LISTA)
# =========================================================================================
# Escribir la operación insertarEnPosicion del TDA Lista. Recibe un dato y una posición.
# Debe insertar un nuevo nodo con el dato exactamente en esa posición (desplazando al resto).
# Las posiciones arrancan en 1. 
# Nota: Podés asumir que la posición siempre es mayor a 1 (nunca te piden insertar primero)
# y si la posición es mayor al tamaño de la lista, se inserta al final de todo.
def insertarEnPosicion(self, dato: int, posicion: int):
    nodoActual = self._Lista__primero
    posicionActual = 1
    while posicionActual < posicion-1 and nodoActual.tiene_siguiente():
        nodoActual = nodoActual.siguiente
        posicionActual = posicionActual + 1
    siguiente = nodoActual.siguiente
    nodoActual.siguiente = self._Lista__NodoLista(dato)
    nodoActual.siguiente.siguiente = siguiente

Lista.insertarEnPosicion = insertarEnPosicion


# =========================================================================================
# EJERCICIO 2: ELIMINAR TODAS LAS APARICIONES (TDA LISTA)
# =========================================================================================
# Escribir la operación eliminarApariciones del TDA Lista. Recibe un dato por parámetro
# y debe eliminar TODOS los nodos de la lista que contengan ese dato.
# Nota: NO podés usar una lista auxiliar ni el método eliminar().
# Para facilitarte la lógica, el primer elemento de la lista NUNCA va a coincidir con el dato.
def eliminarApariciones(self, dato: int):
    nodoActual = self._Lista__primero
    while nodoActual.tiene_siguiente():
        if nodoActual.siguiente.dato == dato:
            nodoActual.siguiente = nodoActual.siguiente.siguiente
        else:
            nodoActual = nodoActual.siguiente

Lista.eliminarApariciones = eliminarApariciones

# =========================================================================================
# TEST UNITARIOS AL ESTILO HACKERRANK
# =========================================================================================
def run_tests():
    ej_a_correr = None
    if len(sys.argv) > 1:
        ej_a_correr = sys.argv[1]

    print("==========================================================")
    print("Iniciando pruebas - Simulacro Parcial 2 (ROUND 3 - LISTAS)")
    if ej_a_correr:
        print(f"> Corriendo SOLAMENTE el Ejercicio {ej_a_correr} <")
    print("==========================================================\n")
    
    score = 0
    max_score = 0

    # Ejercicio 1
    if ej_a_correr is None or ej_a_correr == '1':
        max_score += 50
        try:
            lista = Lista()
            for x in [10, 20, 30, 40]:
                lista.agregar_al_final(x)
            
            lista.insertarEnPosicion(99, 3) # Inserta en la posicion 3
            lista.insertarEnPosicion(88, 10) # Inserta al final por excederse
            
            res = lista.a_lista_python()
            esperado = [10, 20, 99, 30, 40, 88]
            if res == esperado:
                print("✅ Ejercicio 1: Insertar en Posicion -> PASS (50 pts)")
                score += 50
            else:
                print("❌ Ejercicio 1: Insertar en Posicion -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {res}")
        except Exception as e:
            print("❌ Ejercicio 1: Insertar en Posicion -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    # Ejercicio 2
    if ej_a_correr is None or ej_a_correr == '2':
        max_score += 50
        try:
            lista = Lista()
            # Frecuencia alta del 2 (hasta pegados) para probar bucles infinitos
            for x in [5, 2, 2, 8, 9, 2, 2, 4, 2]:
                lista.agregar_al_final(x)
            
            lista.eliminarApariciones(2)
            
            res = lista.a_lista_python()
            esperado = [5, 8, 9, 4]
            if res == esperado:
                print("✅ Ejercicio 2: Eliminar Apariciones -> PASS (50 pts)")
                score += 50
            else:
                print("❌ Ejercicio 2: Eliminar Apariciones -> FAIL")
                print(f"   Esperado: {esperado}")
                print(f"   Obtenido: {res}")
        except Exception as e:
            print("❌ Ejercicio 2: Eliminar Apariciones -> EXCEPCIÓN NO CONTROLADA:")
            traceback.print_exc()

    print("\n==========================================================")
    print(f"PUNTAJE FINAL: {score} / {max_score}")
    print("==========================================================")
    if score == max_score:
        print("¡PERFECTO! Dominaste las listas. ¡A dormir y romperla mañana!")
    else:
        print("Tranqui, revisá los errores (¡Ojo con los punteos y avanzar el nodo!)")

if __name__ == '__main__':
    run_tests()
