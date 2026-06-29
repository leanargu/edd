class Lista:
    class __NodoLista:
        def __init__(self, dato: any):
            self.dato = dato
            self.siguiente = None

        def tiene_siguiente(self) -> bool:
            return self.siguiente is not None

    def __init__(self):
        self.__primero = None

    def __repr__(self) -> str:
        strLista = "primero"
        aux = self.__primero
        while aux != None:
            strLista += " -> " + str(aux.dato)
            aux = aux.siguiente
        return strLista + " -|"

    def esta_vacia(self) -> bool:
        return self.__primero is None

    def agregar_al_final(self, dato: any) -> None:
        nuevo = Lista.__NodoLista(dato)
        if self.esta_vacia():
            self.__primero = nuevo
        else:
            aux = self.__primero
            while aux.tiene_siguiente():
                aux = aux.siguiente
            aux.siguiente = nuevo

    def tamaño(self) -> int:
        cant_nodos = 0
        if not self.esta_vacia():
            nodo_aux = self.__primero
            while nodo_aux is not None:
                cant_nodos += 1
                nodo_aux = nodo_aux.siguiente

        return cant_nodos


    def insert(self, dato: any, pos: int) -> None:
        if pos >= 0:
            nuevo = Lista.__NodoLista(dato)
            if self.esta_vacia():
                self.__primero = nuevo
            elif pos == 0:
                nuevo.siguiente = self.__primero
                self.__primero = nuevo
            elif pos >= self.tamaño():
                self.agregar_al_final(dato)
            else:
                aux = self.__primero
                posAux = 0
                while posAux < pos - 1:
                    aux = aux.siguiente
                    posAux += 1
                nuevo.siguiente = aux.siguiente
                aux.siguiente = nuevo
        else:
            raise IndexError("La posición debe ser mayor o igual a cero")

    def borrar(self, pos: int) -> None:
        if 0 <= pos < self.tamaño():
            if pos == 0:
                self.__primero = self.__primero.siguiente
            else:
                posAux = 0
                aux = self.__primero
                while posAux < pos - 1:
                    aux = aux.siguiente
                    posAux += 1
                aux.siguiente = aux.siguiente.siguiente
        else:
            raise IndexError("La posición debe ser mayor y menor al tamaño de la lista")

    def obtener(self, pos: int) -> any:
        buscado = None
        if 0 <= pos < self.tamaño():
            if pos == 0:
                buscado = self.__primero
            else:
                posAux = 0
                aux = self.__primero
                while posAux < pos - 1:
                    aux = aux.siguiente
                    posAux += 1
                buscado = aux.siguiente
            return buscado.dato
        else:
            raise IndexError("La posición debe ser mayor y menor al tamaño de la lista")


l1 = Lista()
l1.agregar_al_final(1)
l1.agregar_al_final(7)
l1.agregar_al_final(3)
print(l1.obtener(2))
print(l1)
# print(l1.tamaño())

