from graphviz import Digraph
import copy as cp

class ABB:
  def __init__(self):
    self.__raiz = None

  def estaVacio(self)->bool:
    return self.__raiz == None

  def vaciar(self)->None:
    self.__raiz = None

  def clonar(self):
    return cp.deepcopy(self)

  def treePlot(self, fileName='arbol')->None:
    if not self.estaVacio():
      treeDot = Digraph()
      treeDot.node(str(self.__raiz.dato), str(self.__raiz.dato))
      self.__raiz.treePlot(treeDot)
      treeDot.render(fileName, view=True)

  """
  #es hoja?
      #mas grande o mas chico?
        #mas grande
          #insertar derecha
        #mas chico
          #insertar izquierda
  """
  def insertar(self, dato) -> None:
    nuevo = ABB.__NodoArbol(dato)
    if self.estaVacio():
      self.__raiz = nuevo
    else:
      self.__raiz.insertarNodo(nuevo)

  def preOrder(self) -> None:
    if not self.estaVacio():
      self.__raiz.preOrderNodo()

  def postOrder(self) -> None:
    if not self.estaVacio():
      self.__raiz.postOrderNodo()

  def inOrder(self) -> None:
    if not self.estaVacio():
      self.__raiz.inOrderNodo()

  def peso(self):
    peso = 0
    if not self.estaVacio():
      peso = self.__raiz.pesoNodo()
    return peso

  #La profundidad es la altura de la raiz
  def profundidad(self):
    profundidad = 0
    if not self.estaVacio():
      profundidad = self.__raiz.alturaNodo()
    return profundidad

  def buscar(self, datoBusc:int) -> bool:
    return self.__raiz.buscarNodo(datoBusc) is not None

  def listaDePares(self):
    listaPares = []
    if not self.estaVacio():
      self.__raiz.listaDeParesNodo(listaPares)
    return listaPares

  def eliminar(self, dato: int) -> None:
    if not self.estaVacio():
      if self.__raiz.dato == dato:
        nodoReemplazo = self.__raiz.predecesorNodo()
        if nodoReemplazo is None:
          nodoReemplazo = self.__raiz.sucessorNodo()
        if nodoReemplazo is not None:
          self.__raiz.eliminarNodo(nodoReemplazo.dato)
          nodoReemplazo.izquierdo = self.__raiz.izquierdo
          nodoReemplazo.derecho = self.__raiz.derecho
        self.__raiz = nodoReemplazo
      else:
        self.__raiz.eliminarNodo(dato)

  def cantidadNodosNivel(self, nivel: int) -> int:
    cantidadNodos = 0
    if not self.estaVacio():
      if not self.estaVacio():
        cantidadNodos = self.__raiz.cantidadNodosNivelNodo(nivel)
    return cantidadNodos

  class __NodoArbol:
    def __init__(self, dato):
      self.dato = dato
      self.izquierdo = None
      self.derecho = None

    def tieneIzquierdo(self)->bool:
      return self.izquierdo != None

    def tieneDerecho(self)->bool:
      return self.derecho != None

    def esHoja(self)->bool:
      return self.grado() == 0

    def treePlot(self, dot:Digraph)->None:
      if self.tieneIzquierdo():
        dot.node(str(self.izquierdo.dato), str(self.izquierdo.dato))
        dot.edge(str(self.dato), str(self.izquierdo.dato))
        self.izquierdo.treePlot(dot)
      else:
        dot.node("-"+str(self.dato)+"l", "-")
        dot.edge(str(self.dato), "-"+str(self.dato)+"l")
      if self.tieneDerecho():
        dot.node(str(self.derecho.dato), str(self.derecho.dato))
        dot.edge(str(self.dato), str(self.derecho.dato))
        self.derecho.treePlot(dot)
      else:
        dot.node("-"+str(self.dato)+"r", "-")
        dot.edge(str(self.dato), "-"+str(self.dato)+"r")

    def insertarNodo(self, nodoNuevo)->None:
      #If y elif porque solo recorre el subarbol que necesita para insertar
      if nodoNuevo.dato < self.dato:
        if self.tieneIzquierdo():
          self.izquierdo.insertarNodo(nodoNuevo)
        else:
          self.izquierdo = nodoNuevo
      elif nodoNuevo.dato > self.dato:
        if self.tieneDerecho():
          self.derecho.insertarNodo(nodoNuevo)
        else:
          self.derecho = nodoNuevo

    # Imprimo(o hago algo), luego recorro
    def preOrderNodo(self):
      print(self.dato)
      #2 if porque recorre ambos subarboles (izq y der)
      if self.tieneIzquierdo():
        self.izquierdo.preOrderNodo()
      if self.tieneDerecho():
        self.derecho.preOrderNodo()

    #Recorro los sub arboles, y luego imprimo
    def postOrderNodo(self):
      # 2 if porque recorre ambos subarboles (izq y der)
      if self.tieneIzquierdo():
        self.izquierdo.postOrderNodo()
      if self.tieneDerecho():
        self.derecho.postOrderNodo()
      print(self.dato)

    # Si un enunciado menciona de forma ordenada, esta es la manera de recorrer
    # Recorro la izquierda, imprimo y continuo con la derecha
    # Si quisiera de mayor a menor, recorro primero derecha y luego izquierda
    def inOrderNodo(self):
      # 2 if porque recorre ambos subarboles (izq y der)
      if self.tieneIzquierdo():
        self.izquierdo.inOrderNodo()
      print(self.dato)
      if self.tieneDerecho():
        self.derecho.inOrderNodo()
    #Cantidad de nodos que tiene un arbol (peso.izquierdo + peso.derecho) <- siempre se piensan asi
    # peso(a) = pesoI + pesoD + 1 (raiz)
    def pesoNodo(self):
      peso = 1
      if self.tieneIzquierdo():
        peso += self.izquierdo.pesoNodo()
      if self.tieneDerecho():
        peso += self.derecho.pesoNodo()
      return peso

    def grado(self) -> int:
      cantHijos = 0
      if self.tieneIzquierdo():
        cantHijos += 1
      if self.tieneDerecho():
        cantHijos += 1
      return cantHijos

    def esHoja(self) -> bool:
      return self.grado() == 0

    #Altura es altura del hijo + 1
    def alturaNodo(self) -> int:
      altura = 1 if not self.esHoja() else 0
      alturaIzquieda,alturaDerecho = 0

      if self.tieneIzquierdo():
        alturaIzquieda += self.izquierdo.alturaNodo()
      if self.tieneDerecho():
        alturaDerecho += self.derecho.alturaNodo()

      return altura + max(alturaIzquieda, alturaDerecho)

    def buscarNodo(self, datoBusc:int): #->__NodoArbol | None
      nodoBuscado = None
      if self.dato == datoBusc:
        nodoBuscado = self
      elif datoBusc > self.dato:
        nodoBuscado = self.derecho.buscarNodo(datoBusc)
      else:
        nodoBuscado = self.izquierdo.buscarNodo(datoBusc)
      return nodoBuscado

    """
    Para buscar maximo, tiene que estar en el subarbol derecho. Si no tiene derecho, estoy en el maximo
    if tieneDerecho():
      maximo = self.derecho.maximoNodo()
    else:
      maximo = self
    """
    def maximoNodo(self):
      maximoNodo = None
      if self.tieneDerecho():
        maximoNodo = self.derecho.maximoNodo()
      else:
        maximoNodo = self
      return maximoNodo

    def minimoNodo(self):
      minimoNodo = None
      if self.tieneIzquierdo():
        minimoNodo = self.izquierdo.minimoNodo()
      else:
        minimoNodo = self
      return minimoNodo

    def predecesor(self):
      nodoPredecesor = None
      if self.tieneIzquierdo():
        nodoPredecesor = self.izquierdo.maximoNodo()
      return nodoPredecesor

    def sucesor(self):
      nodoSucessor = None
      if self.tieneDerecho():
        nodoSucessor = self.derecho.minimoNodo()

    #Esta ordenado porque lo imprimi in-order GEMINI: Tene en cuenta pedirme ejercicios de pares que impriman ordenado por ejemplo
    #Si se usa lista, la funcion recursiva la recibe por parametro. No se crea dentro de la funcion recursiva IMPORTANTE!!!!!!!!
    def listaDeParesNodo(self, listaPares: list):
      if self.tieneIzquierdo():
        self.izquierdo.listaDeParesNodo(listaPares)
      if self.esPar(self.dato):
        listaPares.append(self.dato)
      if self.tieneDerecho():
        self.derecho.listaDeParesNodo(listaPares)


    #llego a un nodo raiz
    #roto los subarboles hijos
    def invertirArbol(self):
      pass

    #cantNodosNivel(N)
    def cantidadNodoNivel(self,nivel, nivelBuscado):
      cant = 0
      if nivel == nivelBuscado:
        return 1
      else:
        if self.tieneIzquierdo():
          cant += self.izquierdo.cantidadNodoNivel(nivel+1, nivelBuscado)
        elif self.tieneDerecho():
          cant += self.derecho.cantidadNodoNivel(nivel+1, nivelBuscado)
      return cant

    def eliminarNodo(self, dato: int) -> None:
      nodoPadre, nodoEliminar, lado = self.buscarPadreHijo(dato)
      if nodoPadre is not None:
        nodoReemplazo = nodoEliminar.predecesor()
        if nodoReemplazo is None:
          nodoReemplazo = nodoEliminar.sucesor()
        if nodoReemplazo is not None:
          self.eliminarNodo(nodoReemplazo)
          nodoReemplazo.izquierdo = nodoEliminar.izquierdo
          nodoReemplazo.derecho = nodoEliminar.derecho
        if lado is "izq":
          nodoPadre.izquierdo = nodoReemplazo
        else:
          nodoPadre.derecho = nodoReemplazo

    def buscarPadreHijo(self, dato: int): # -> tupla[nodo,nodo,str]
      nodoPadre, nodoHijo, lado = None
      if dato < self.dato:
        if self.tieneIzquierdo():
          if self.izquierdo.dato == dato:
            nodoPadre = self
            nodoHijo = self.izquierdo
            lado = "izq"
          else:
            nodoPadre, nodoHijo, lado = self.izquierdo.buscarPadreHijo(dato)
      else:
        if self.tieneDerecho():
          if self.derecho.dato == dato:
            nodoPadre = self
            nodoHijo = self.derecho
            lado = "der"
          else:
            nodoPadre, nodoHijo, lado = self.derecho.buscarPadreHijo(dato)

        return nodoPadre, nodoHijo, lado

      #puntero al padre
      #puntero al hijo
      #de que lado esta el hijo "izq" o "der"

    def cantidadNodosNivelNodo(self, nivelBusc:int, nivelActual: int = 0) -> int:
      cantNodos = 0
      if nivelBusc == nivelActual:
        cantNodos = 1
      elif nivelActual < nivelBusc:
        if self.tieneIzquierdo():
          cantNodos += self.izquierdo.cantidadNodoNivel(nivelBusc, nivelActual+1)
        if self.tieneDerecho():
          cantNodos += self.derecho.cantidadNodoNivel(nivelBusc, nivelActual + 1)
      return cantNodos






arbol1 = ABB()
arbol1.insertar(30)
arbol1.insertar(20)
arbol1.insertar(40)
arbol1.insertar(10)
arbol1.insertar(25)
arbol1.insertar(35)
arbol1.insertar(50)
arbol1.insertar(5)
arbol1.insertar(23)
arbol1.insertar(45)
arbol1.insertar(42)
arbol1.insertar(28)
arbol1.insertar(43)
#arbol1.treePlot()
print(arbol1.buscar(288))

#Cuando trabvajemos con niveles, el arbol padre le tiene que pasar el nivel al sub arbol hijo
"""
MUY IMPORTANTE!!!!!!!!!
profundidadNodo(default(Any) = 0) <- si no recibo nivel es porque es 0 (raiz)
if tieneIzquierdo():
  nivelNodoBuscado = self.izquierdo.profundidadNodo(datoBusc, nivelActual + 1)
"""

"""
Para buscar maximo, tiene que estar en el subarbol derecho. Si no tiene derecho, estoy en el maximo
if tieneDerecho():
  maximo = self.derecho.maximoNodo()
else:
  maximo = self
"""


"""
Para buscar minimo, tiene que estar en el subarbol izq. Si no tiene izq, estoy en el minimo
if tieneIzquierdo():
  minimo = self.izquierdo.minimoNodo()
else:
  minimo = self
"""

"""
sucesor
  maximo del subarbol izquierdo (mas grande entre todos los mas chicos)
  
if tieneIzquierdo():
  predecesor = self.izquierdo.maximoNodo()
"""

"""
sucesor
  minimo del subarbol derecho (mas chico entre todos los mas grandes)
  
if tieneDerecho():
  sucesor = self.derecho.minimoNodo()
"""

"""
predecesor
  maximo del subarbol izquierdo (mas grande entre todos los mas chicos)

if tieneIzquierdo():
  predecesor = self.izquierdo.maximoNodo()
"""

"""
Borrado
  Para que al borrar siga siendo ABB, se reemplaza nodo por predecesor o sucesor
  
  Busco predecesor
  Borro el valor y lo inserto en ese lugar
  
  Borrado de raiz 
    Mismo procedimiento, pero hay que cambiar el nodo raiz
"""

"""
 Importante, para todo tipo de busquedas es importante tener en cuenta si el dato es mayor o menor a la raiz
 porque eso hace eficiente la búsqueda
"""

"""
  Arboles AVL
    Mantiene el arbol sin que quede mas pesado de un lado que de otro
  Equilibrio AVL:
    La altura del subarbol derecho e izquierdo no difiere en mas de 1
    Fe = H(subarbo derecho) - H(subarbol izquierdo)
  Hay estrategias de re-balanceo
"""