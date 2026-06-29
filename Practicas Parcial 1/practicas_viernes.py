import numpy as np

def par_impar(arreglo):
    """
    #Verificamos los primeros 2 elementos
        2 casos
            alternan
                true
            no alternan
                false
    base
        array size 1 / 0 / vacio
            true
    """

    es_alternado = False

    if len(arreglo) < 2:
        es_alternado = True
    elif son_alternados(arreglo[0], arreglo[1]):
        es_alternado = par_impar(arreglo[1:])
    else:
        es_alternado = False
    return es_alternado

def son_alternados(numero: int, numero2: int) -> bool:
    return (es_par(numero) and not es_par(numero2)) or (not es_par(numero) and es_par(numero2))

def es_par(numero) -> bool:
    return numero % 2 == 0

class Examen:
    def __init__(self, fecha: int, hileras: int, mesas:int):
        self.__fecha = fecha
        self.__laboratorio = np.zeros((hileras, mesas), bool)

    def __repr__(self):
        return str(self.__laboratorio)

    def asignar_lugares(self, cant_alumnos:int) -> None:
        #Como arranco en 0,0 solo coloco si la columna es par
        cant_hileras, cant_mesas = self.__laboratorio.shape
        for i in range(cant_hileras):
            for j in range(0,cant_mesas,2):
                if(cant_alumnos > 0 and self.__laboratorio[i][j] == False):
                    self.__laboratorio[i][j] = True
                    cant_alumnos -= 1


examen1 = Examen(1, 10, 5)
#print(examen1)
examen1.asignar_lugares(15)
#print(examen1)

"""

"""
def invertir_palabra(palabra):
    palabra_invertida = ""
    if len(palabra) < 2:
        palabra_invertida =  palabra
    else:
        palabra_invertida = invertir_palabra(palabra[1:]) + palabra[0]
    return palabra_invertida

#print(invertir_palabra("hola"))

class Ingrediente:
    def __init__(self, nombre:str, cantidad:int, calorias:float):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__calorias = calorias

    def __repr__(self):
        return f"{self.__nombre} ({self.__cantidad} g - {self.__calorias} cal)"

    def get_calorias(self):
        return self.__calorias

class Receta:
    def __init__(self, nombre:str, tipo: str):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__ingredientes = np.empty(20, Ingrediente)

    def __repr__(self):
        return str(self.__ingredientes)

    def agregar_ingrediente(self, nombre:str, cantidad:int, calorias:float) -> None:
        agregue_ingrediente = False #Es importante el flag para no guardar en todas las posiciones y no usar un while
        for i in range(len(self.__ingredientes)):
            if not agregue_ingrediente and not self.__ingredientes[i]:
                self.__ingredientes[i] = Ingrediente(nombre, cantidad, calorias)
                agregue_ingrediente = True
        if not agregue_ingrediente:
            raise Exception("La receta ya tiene 20 ingredientes")

    def total_calorias(self) -> float:
        total = 0
        for ingrediente in self.__ingredientes:
            if ingrediente:
                total += ingrediente.get_calorias()
        return total

    def ingrediente_mas_calorico(self):
        mas_calorico = None
        for ingrediente in self.__ingredientes:
            if ingrediente:
                if mas_calorico is None:
                    mas_calorico = ingrediente
                elif ingrediente.get_calorias() > mas_calorico.get_calorias():
                    mas_calorico = ingrediente
        return mas_calorico


pastelDePapa = Receta("pastel de papa", "Omnivora")
pastelDePapa.agregar_ingrediente("papa", 1000, 1587.3)
pastelDePapa.agregar_ingrediente("cebolla", 500, 524.7)
pastelDePapa.agregar_ingrediente("carne",1000,2587.4)
#print(pastelDePapa)
#print(pastelDePapa.total_calorias())
#print(pastelDePapa.ingrediente_mas_calorico())

def esta_incluido(arr1: np.array, arr2:np.array) -> bool:
    esta_incluido = False
    if len(arr1) == 0:
        esta_incluido = True
    elif len(arr2) < len(arr1):
        esta_incluido = False
    else:
        esta_incluido = esta_incluido_inicio(arr1, arr2) or  esta_incluido_final(arr1, arr2)
    return esta_incluido


def esta_incluido_inicio(arr1: np.array, arr2:np.array) -> bool:
    esta = None
    if len(arr1) == 0:
        esta = True
    elif arr1[0] == arr2[0]:
        esta = esta_incluido_inicio(arr1[1:], arr2[1:])
    else:
        esta = False
    return esta

def esta_incluido_final(arr1: np.array, arr2:np.array) -> bool:
    pass