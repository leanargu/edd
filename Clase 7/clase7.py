import numpy as np

v = [1,3,4,5]
#print(v[1:])
#print(v[:-1])

# Sumar elementos de un array

def sumar_elementos(vector):
    if len(vector) == 1:
        return vector[0]
    else:
        return vector[0] + sumar_elementos(vector[1:])

#print(sumar_elementos(v))

#[1,3,4,5]
def sumar_elementos_2(vector):
    sumaTotal = 0
    if len(vector) == 0:
        sumaTotal = 0
    else:
            #          1 +  3    + sumar...([4,5])
        sumaTotal = vector[0] + sumar_elementos(vector[1:])
    return sumaTotal

#print(sumar_elementos_2(v))

def es_palindromo(palabra):
    palindromo = False
    if len(palabra) <= 1:
        palindromo = True
    else:
        palindromo = (palabra[0] == palabra[-1]
                      and es_palindromo(palabra[1:-1]))
    return palindromo

#print(es_palindromo("asd"))

vector = np.array([5,10,9,8,1,13])

def vir(v):
    if len(v) > 1:
        if v[1] < v[0]:
            v[1],v[0] = v[0], v[1]
        vir(v[1:])

vir(vector)
#print(vector)

"""
    Busqueda binaria
    si len(v) >= 0
        centro = len(v)/2
        if dato == v[centro]
            true
        elif dato < v[centro]
            buscar(v[0:centro])
        else
            buscar(v[centro:])
    else
        False
"""

v = [3,5,7,9,11,14,20]

def buscar_en(numero, vector):
    esta = False
    if len(vector) == 0:
        esta = False
    else:
        centro = len(vector) // 2
        if vector[centro] == numero:
            esta = True
        elif numero < vector[centro]:
            esta = buscar_en(numero, vector[0:centro])
        else:
            #Clave el +1 al centro, porque sino nunca deja el len del array en 0
            esta = buscar_en(numero, vector[centro+1:])
    return esta

#print(buscar_en(33, v))

def maximo_en(vector):
    maximo = 0
    if len(vector) == 1:
        maximo = maximo_entre(vector[0], maximo)
    else:
        maximo = maximo_entre(vector[0], maximo_en(vector[1:]))
    return maximo

def maximo_entre(un_numero, otro_numero):
    maximo = 0
    if un_numero >= otro_numero:
        maximo = un_numero
    elif un_numero < otro_numero:
        maximo = otro_numero
    return maximo

print(maximo_en([1,9,5,3,2,33,4]))
"""
    Es importante el pivote que elijo para recorrer
    
    Si voy quedandome con vector[0]
        debo recorrer hacia la derecha: vector[1:]
    Si voy a quedarme con vector[len(vector)-1]
        debo recorrer hacia la izquierda: vector[:-1]
"""

def contador_de_repetidos(vector):
    numeros_repetidos = [],[]
    if len(vector) == 1:
        numeros_repetidos[0].append(vector[0])
    else:
        numeros_repetidos = contador_de_repetidos(vector[1:])
        numero_actual = vector[0]
        if(numero_actual == numeros_repetidos[0][0]):
            numeros_repetidos[0].append(numero_actual)
        else:
            numeros_repetidos[1].append(numero_actual)
    return numeros_repetidos

def hay_misma_cantidad_de_repetidos(vector):
    contador = contador_de_repetidos(vector)
    return len(contador[0]) == len(contador[1])

print(hay_misma_cantidad_de_repetidos([2,2,2,2,3,3,3]))