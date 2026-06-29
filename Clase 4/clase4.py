import numpy as np

#Ejemplo de recorrido
"""
v1 = np.array([3,7,4,1,5])
print(v1)
#for elemento in v1:
#    print(elemento)

for i in range(len(v1)):
    print(i,v1[i])

m1 = np.array([
    [3,4,5],
    [1,3,8],
    [2,6,9]
])

print(m1.shape)

#Recorrido por elementos
for vFila in m1:
    for n in vFila:
        print(n)

#Recorrido por indices
nFilas, nCols = m1.shape
for posFila in range(nFilas):
    for posCol in range(nCols):
        print(m1[posFila][posCol])


Ejercicio 1
Escribir una función que recibe un numero entero N y le pide al usuario que ingrese N
 numeros. Al final, el programa debe retornar un vector contiendo los números que 
 fueron ingresados. Tambien debe imprimir por pantalla la suma total de los valores y
  el promedio. Se deben hacer funciones para resolver el promedio y la suma total.
"""

def armar_array(n: int):
        array = np.zeros(n,int)
        for i in range(n):
            numero = int(input("Ingresa un numero: "))
            array[i] = numero
        print(array)
        print(sumar_valores_de(array))
        print(sacar_promedio_de(array))


def sumar_valores_de(array):
    suma = 0
    for numero in array:
        suma += int(numero)
    return suma

def sacar_promedio_de(array):
    return sumar_valores_de(array) / len(array)

#armar_array(5)

"""
Escribir una función que recibe un vector de strings y retorna otro con 
los mismos elementos del vector de entrada pero en orden inverso.
"""

def invertir(array: np.array):
    array_inverso = np.empty(len(array),str)
    for i in reversed(range(len(array))):
        indice_nuevo = len(array) - i - 1
        array_inverso[indice_nuevo] = array[i]

    return array_inverso

#print(invertir(["a","b","c","d","e"]))

"""
Ejercicio 3
Escribir la función sumaDeVectores que recibe dos vectores de enteros del mismo tamaño y 
retorna otro con la suma de ambos. La suma de vectores se realiza componente a componente, 
segun la siguiente forma:

v1 = [ v11 , v12 , v13 , ... , v1N ]
v2 = [ v21 , v22 , v23 , ... , v2N ]
v1 + v2 = [ v11 + v21 , v12 + v22 , v13 + v23 , ... , v1N + v2N ]
"""

def sumaDeVectores(array: np.array, array1: np.array):
    array_suma = np.empty(len(array),int)
    for i in range(len(array)):
        array_suma[i] = array[i] + array1[i]
    return array_suma

#print(sumaDeVectores([1,2,3],[4,5,6]))

"""
Ejercicio 4
Escribir una función que recibe un vector y desplaza todos sus elementos una posición 
hacia la derecha: el primero pasa a ser el segundo, el segundo pasa a ser el tercero y así sucesivamente. 
El último pasa a ser el primero.

Por ejemplo:

v1 = [2, 4, 1, 5, 7, 9]

desplazarADerecha(v1)

=> v1 = [9, 2, 4, 1, 5, 7]
"""

def desplazar_a_derecha(array: np.array):
    array_dez = np.empty(len(array),int)
    for i in range(len(array)):
        indice_desplazado = i + 1 if i < len(array) - 1 else 0
        array_dez[i] = array[indice_desplazado]
    return array_dez

#print(desplazar_a_derecha([1,2,3,4,5]))

"""
Ejercicio 5
Desarrollar una función que inserte un elemento en una posición en un vector. Al insertar el elemento,
 se debe producir un desplazamiento a la derecha de todos los elementos en las posiciones siguientes, 
 el último elemento se pierde.

Por ejemplo:

v1 = [2, 4, 1, 7, 6, 2]

insertar(v1, 5, 3) #insertamos un 5 en la posición 3

=> v1 = [2, 4, 1, 5, 7, 6]
"""

def insertar(array: np.array, numero: int, posicion: int):
    array_desplazado = array.copy()
    for i in range(len(array)):
        if i < posicion:
            array_desplazado[i] = array[i]
        elif i == posicion:
            array_desplazado[i] = numero
        else:
            array_desplazado[i] = array[i-1]
    return array_desplazado

#1,7,2,3,4
#print(insertar([1,2,3,4,5], 7, 1))

"""
Ejercicio 6
Escribir una función que elimine el elemento que ocupa una determinada posición de un vector. Al eliminar,
 los elementos a la derecha del eliminado, deben desplazarse a la izquierda un lugar y agregar un cero en la 
 última posición.

Por ejemplo:

v1 = [4, 3, 5, 8, 6, 7]

eliminar(v1, 2) #eliminamos el elemento de la posicion 2

=> v1 = [4, 3, 8, 6, 7, 0]
"""
def eliminar(array: np.array, posicion: int):
    array_nuevo = np.empty(len(array),int)
    for i in range(len(array)):
        if i < posicion:
            array_nuevo[i] = array[i]
        elif i >= posicion and llegue_al_final(array, i):
            array_nuevo[i] = array[i+1]
        else:
            array_nuevo[i] = 0
    return array_nuevo


def llegue_al_final(array, i):
    return i + 1 > len(array)


#print(eliminar([1,2,3,4,5],1))

"""
Ejercicio 7
Escribir una función que elimine todas las apariciones de un determinado elemento de un vector. 
Al eliminar se deben insertar tantos ceros al final como elementos se eliminaron.

Por ejemplo:

arr1 = [4, 3, 5, 8, 6, 5, 7, 5]

eliminarApariciones(arr1, 5) #eliminamos todos los 5 del arreglo

=> arr1 = [4, 3, 8, 6, 7, 0, 0, 0]
"""

def eliminar_apariciones(array: np.array, valor_a_eliminar: int):
    array_nuevo = array.copy()
    for i in range(len(array)):
        if array_nuevo[i] == valor_a_eliminar:
            array_nuevo = eliminar(array_nuevo, i)
    return array_nuevo

print(eliminar_apariciones([4, 3, 5, 8, 6, 5, 7, 5],5))

