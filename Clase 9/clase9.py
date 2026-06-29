#!/usr/bin/env python

from typing import Any
import copy as cp
import numpy as np

class Diccionario:
	# La clase Pair es privada, interna de la clase Diccionario
	class _Pair:
		def __init__(self, key: Any, value: Any) -> None:
			self._association = (key, value)

		def __repr__(self) -> str:
			return str(self._association)

		def __eq__(self, key: Any) -> bool:
			return self._association[0] == key

		def __hash__(self) -> int:
			return hash(self._association[0])

		def key(self) -> Any:
			return self._association[0]

		def value(self) -> Any:
			return self._association[1]

	def __init__(self, keys: list = None, values: list = None) -> None:
		if keys == None and values != None or keys != None and values == None:
			raise Exception("missing arguments")

		if keys != None and len(keys) != len(values):
			raise Exception("len(keys) != len(values)")

		self._items = set()

		if keys == None:
			return

		for i in range(len(keys)):
			self[keys[i]] = values[i]

	def __repr__(self):
		return str(self._items)

	def __setitem__(self, key: Any = None, value: Any = None) -> None:
		if key == None:
			return

		if key in self:
			self._items.remove(key)

		self._items.add(Diccionario._Pair(key, value))

	def insert(self, key: Any = None, value: Any = None) -> None:
		if key == None:
			return

		self._items.add(Diccionario._Pair(key, value))

	def remove(self, key) -> Any:
		if key not in self:
			return None

		v = self[key]
		self._items.remove(key)
		return v

	def clear(self):
		self._items = set()

	def clone(self):
		return cp.deepcopy(self)

	# self[key]
	def __getitem__(self, key: Any) -> Any:
		for p in self._items:
			if p.key() == key:
				return p.value()

		raise Exception(f"key: {key} not in dict")

	# self.get(key)
	def get(self, key):
		return self[key]

	def keys(self):
		return [x.key() for x in self._items]

	def values(self):
		return [x.value() for x in self._items]

	# key in self
	def __contains__(self, key):
		return key in self._items

	def len(self):
		return len(self._items)

"""
Ejercicio 2
Escribir un programa que declare un Diccionario de <entero , entero> (clave entero y significado entero) 
y le agrege 4 pares. Luego debe mostrar el diccionario por pantalla y su tamaño.

Finalmente, redefinir 2 significados y volver a imprimir.
"""
def ejercicio2():
    diccionario = Diccionario()
    diccionario.insert(1,1)
    diccionario.insert(2, 2)
    diccionario.insert(3, 3)
    diccionario.insert(4, 4)

    print(diccionario)
    print(len(diccionario.keys()))

    diccionario[3] = 5
    diccionario[4] = 6

    print(diccionario)
    print(len(diccionario.keys()))

print("#############EJERCICIO-2################")
ejercicio2()

"""
Ejercicio 3
Escribir un diccionario con sinónimos. Luego intentar insertar dos pares <clave , significado> con claves 
repetidas con la operacion insert y ver que sucede.
"""
def ejercicio3():
    diccionario = Diccionario()
    diccionario.insert("mirar", "observar")
    diccionario.insert("mirar", "amanizar")
    print(diccionario)

print("#############EJERCICIO-3################")
ejercicio3()

"""
Ejercicio 4

Escribir una función que dado una lista de enteros me devuelve otra(no necesariamente en el mismo orden)
 sin los numeros repetidos.

Por ejemplo:

Lista de entrada = [1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]

Lista de salida = [1 , 3 , 2, 4]
"""
def ejercicio4(lista_de_enteros):
    return list(set(lista_de_enteros))

print("#############EJERCICIO-4################")
print(ejercicio4(lista_de_enteros=[1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]))

"""
Ejercicio 5
Rehacer le ejercicio 4 pero retornando un diccionario en lugar de una lista.

Por ejemplo:

Lista de entrada = [1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]

Diccionario de salida = { (1 , None) , (3 , None) , (4 , None) , (2 , None) }
"""
def ejercicio5(lista_de_enteros):
    dic = Diccionario()

    for entero in lista_de_enteros:
        dic.insert(entero, None)
    return dic

print("#############EJERCICIO-5#############")
print(ejercicio5(lista_de_enteros=[1 , 3 , 4 , 1 , 2 , 4 , 3 , 2]))

"""
Ejercicio 6
Escribir una función que recibe una lista de números como parámetro y devuelve un diccionario con los 
números de la lista como claves y la cantidad de apariciones de cada uno como su significado.

Por ejemplo:

Lista de entrada = [1 , 3 , 4 , 2 , 1 , 3 , 1 , 4 , 2 , 5 , 2]

Diccionario de salida = { (1 , 3) , (3 , 2) , (4 , 2) , (2 , 3) , (5 , 1) }
"""
def ejercicio6(lista_de_enteros):
    dic = Diccionario()
    for entero in lista_de_enteros:
        if entero in dic:
            dic[entero] = dic.get(entero) + 1
        else:
            dic[entero] = 1

    return dic

print("#############EJERCICIO-6#############")
print(ejercicio6([1 , 3 , 4 , 2 , 1 , 3 , 1 , 4 , 2 , 5 , 2]))

"""
Ejercicio 7
Escribir una función que recibe dos diccionarios y devuelve otro con la mezcla de los dos, para las claves
repetidas, se queda con los significados de primer diccionario.

Por ejemplo:

Diccionario de entrada 1 = { (1 , 3) , (3 , 2) , (4 , 4) , (2 , 3) , (5 , 1) }

Diccionario de entrada 2 = { (10 , 3) , (3 , 5) , (2 , 30) , (8 , 1) , (9 , 3) }

Diccionario de salida = { (1 , 3) , (3 , 2) , (4 , 4) , (2 , 3) , (5 , 1) , (10 , 3) , (8 , 1) , (9 , 3) }
"""
def ejercicio7(dic1, dic2):
    dic_mergeado = Diccionario()

    for key in dic1.keys():
        dic_mergeado.insert(key, dic1.get(key))
    for key in dic2.keys():
        dic_mergeado.insert(key, dic2.get(key))

    return dic_mergeado
def test_ejercicio7():
    dic1 = Diccionario()
    dic2 = Diccionario()

    dic1.insert(1,3)
    dic1.insert(3,2)
    dic1.insert(4,4)
    dic1.insert(2,3)
    dic1.insert(5,1)

    dic2.insert(10,3)
    dic2.insert(3,5)
    dic2.insert(2,30)
    dic2.insert(8,1)
    dic2.insert(9,3)
    print("#############EJERCICIO-7#############")
    print(ejercicio7(dic1, dic2))

"""
Ejercicio 8
Escribir una función que modele el problema de administrar las materias que cursa un alumno. 
Es decir que reciba un diccionario, un alumno y una materia y agregue esa materia a las materias que cursa.

Nota: La lista de materias de cada alumno no debe tener materias repetidas.

Por ejemplo:

Diccionario = { ( "Alumno1" , ["Materia1" , "Materia2"] ) , ( "Alumno2", [ "Materia2" , "Materia3" , "Materia4" ] ) }
"""
def ejercicio8(dic, alumno, materia):
    if alumno in dic.keys():
        dic.get(alumno).add(materia)
    else:
        dic.insert(alumno, set())
        dic.get(alumno).add(materia)
def test_ejercicio8():
    dic = Diccionario()
    alumno1 = "Alumno1"
    materia1 = "Materia1"
    materiaRepetida = "Materia1"
    materia2 = "Materia2"

    alumno2 = "Alumno2"
    materia3 = "Materia3"

    ejercicio8(dic, alumno1, materia1)
    ejercicio8(dic, alumno1, materiaRepetida)
    ejercicio8(dic, alumno1, materia2)

    ejercicio8(dic, alumno2, materia1)
    ejercicio8(dic, alumno2, materiaRepetida)
    ejercicio8(dic, alumno2, materia3)
    print("#############EJERCICIO-8#############")
    print(dic)

"""
Ejercicio 9
Escribir una función listaToDic que recibe una lista con chirimbolos y devuelve un diccionario con cada 
chirimbolo como clave y como significado una matriz de nxn donde n es la cantidad de veces que aparece el 
chirimbolo en la lista. La matriz se debe llenar con el chirimbolo de la clave. 

Se debe resolver usando las operaciones del TDA diccionario que vimos en clase, sin violar 
el encapsulamiento ni utilizando estructuras auxiliares. Si es necesario definir funciones auxiliares. 
Ejemplo:

lista = [‘*’, ‘#’, ‘/’, ‘*’, ‘#’, ‘/’, ‘*’, ‘$’]
listaToDic(lista) –> Diccionario
Entonces, listaToDic(lista) =>
{(‘*’,  [[‘*’,‘*’,‘*’],[‘*’,‘*’,‘*’],[‘*’,‘*’,‘*’]]) , (‘$’ , [[‘$’]]), (‘/’ , [[‘/’,‘/’],[‘/’,‘/’]]) , 
(‘#’ , [[‘#’,‘#’],[‘#’,‘#’]])}
"""
def ejercicio9(list):
    dic = Diccionario()
    simbolo_veces = ejercicio6(list)
    for simbolo in simbolo_veces.keys():
        dic[simbolo] = np.full((simbolo_veces[simbolo], simbolo_veces[simbolo]), simbolo)

    return dic

print("#############EJERCICIO-9#############")
print(ejercicio9(["*", "#", "/","*","#","/","*","$"]))

"""
Ejercicio 10
Escribir la función promedios que recibe una lista de materias (strings) y una lista de notas (enteros) del
 mismo tamaño. Retorna un diccionario que posee como clave cada materia y como significado su nota promedio.
Se debe resolver usando las operaciones del TDA diccionario que vimos en clase, 
sin violar el encapsulamiento ni utilizando estructuras auxiliares. 

Por ejemplo:
listaMaterias = [“Intro Prog”, “Objetos”, “Estructura de Datos”, “Intro Prog”, ”Inglés”, 
“Objetos”, “Estructura de Datos”]

listaNotas = [4, 4, 4, 6, 7, 6, 6]

dic = promedios(listaMaterias , listaNotas)

Entonces, dic = { (“Intro Prog”, 5) , (“Estructura de Datos”, 5) , (”Inglés”, 7) , ( “Objetos”, 5) }
"""
def ejercicio10(listaMaterias, listaNotas):
    dic = Diccionario()

    for i in range(len(listaMaterias)):
        if listaMaterias[i] in dic.keys():
            dic[listaMaterias[i]] = (dic[listaMaterias[i]] + listaNotas[i]) / 2
        else :
            dic[listaMaterias[i]] = listaNotas[i]
    return dic
def test_ejercicio10():
    listaMaterias = ["Intro Prog", "Objetos", "Estructura de Datos", "Intro Prog", "Inglés", "Objetos",
                     "Estructura de Datos"]
    listaNotas = [4, 4, 4, 6, 7, 6, 6]

    print("#############EJERCICIO-10#############")
    print(ejercicio10(listaMaterias, listaNotas))
test_ejercicio10()

"""
Ejercicio 11
Tenemos un diccionario del tipo <Entero , Lista de enteros> (clave número entero, significado lista de enteros) 
que dado un numero X, guarda las posibles combinaciones de ese número con otros.

Escribir una función que recibe un diccionario de este tipo y devuelve una lista con los posibles pares 
de números (en formato de tupla).

Por ejemplo:

Diccionario de entrada = { (5 , [5 , 3 , 7 ] ) , ( 8, [ 15 , 3 ] ) }

Lista de salida = [ (5 , 5) ,(5 , 3) , (5 , 7) , (8 , 15) , (8 , 3) ]
"""


