import copy as cp

"""
Pruebas listas

lista = [1,2,3,4,5]
lista[0] = 55
print(lista.pop())
print(lista[:-1])
"""
class Pila:
    def __init__(self):
        self.__pila = []

    def __repr__(self):
        return f'Pila: {self.__pila}'

    def apilar(self, dato: any):
        self.__pila.append(dato)

    def desapilar(self) -> None:
        dato = None
        if not self.esta_vacia():
            dato = self.__pila.pop()
        else:
            raise Exception("La pila esta vacia")
        return dato

    def tamano(self) -> int:
        return len(self.__pila)

    def esta_vacia(self) -> bool:
        return self.tamano() == 0

    def top(self) -> any:
        dato = None
        if not self.esta_vacia():
            dato = self.__pila[-1]
        else:
            raise Exception("La pila esta vacia")
        return dato

    def vaciar(self):
        self.__pila = []

    def clonar(self):
        return cp.deepcopy(self)
"""
Pruebas pila

p1 = Pila()
print(p1)
p1.apilar(5)
p1.apilar(9)
p1.apilar(11)
print(p1)
print(p1.top())
p1.desapilar()
print(p1)
p2 = p1.clonar()
print(p2)
p2.vaciar()
"""
class Cola:
    def __init__(self):
        self.__queue = []

    def __repr__(self):
        return f'Cola: {self.__queue}'

    def enqueue(self, dato: any):
        self.__queue.append(dato)

    def esta_vacia(self) -> bool:
        return self.tamano() == 0

    def tamano(self) -> int:
        return len(self.__queue)

    def dequeue(self):
        dato = None
        if not self.esta_vacia():
            dato = self.__queue.pop(0)
        else:
            raise Exception("La Queue esta vacia")
        return dato

    def top(self) -> any:
        dato = None
        if not self.esta_vacia():
            dato = self.__queue[0]
        else:
            raise Exception("La Queue esta vacia")
        return dato

    def clonar(self):
        return cp.deepcopy(self)
"""
Pruebas queue   

q1 = Cola()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print("Q completa")
print(q1)
print("Q top")
print(q1.top())
q1.dequeue()
print("Q despues de dequeue")
print(q1)
print("Top despues de dequeue")
print(q1.top())
print("Tamaño despues de dequeue")
print(q1.tamano())
"""
def invertir_pila(pila: Pila):
    #Modificacion in place porque recibo la referencia a la pila original por parametro
    #No se mantienen las asignaciones sobre la referencia, solo modificaciones inplace
    aux = []
    while not pila.esta_vacia():
        aux.append(pila.desapilar())
    for elemento in aux:
        pila.apilar(elemento)
def invertir_pila_solo_pilas(pila: Pila):
    pila_aux = pila.clonar()
    pila.vaciar()
    while not pila_aux.esta_vacia():
        pila.apilar(pila_aux.desapilar())
"""
Prueba invertir pila

p1 = Pila()
p1.apilar(3)
p1.apilar(4)
p1.apilar(1)
p1.apilar(0)
print("Pila sin invertir")
print(p1)
print("Pila invertida")
invertir_pila(p1) / invertir_pila_solo_pilas(p1)
print(p1)
"""


