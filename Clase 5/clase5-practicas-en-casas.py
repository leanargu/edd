"""
def calcular_ganancias():
    tipo_funcion = self.tipo_funcion
    for fila in filas
        for columna in columnas
         calcular_ganancia(tipo_funcion, butacas[fila][columna])])

 def calcular_ganancia(espectador):
    if tipo_funcion == 2D
         if espectador.edad < 14
            algo
        else
            otra cosa
    else
        if espectador.edad < 14
            algo
        else
            otra cosa
"""

import numpy as np

class SalaDeCine:

  def init(self, numeroDeSala:int, tipoDeSala, cantFilas = 30, cantAsientos = 40):
    self.butacas = np.empty((cantFilas, cantAsientos), Espectador)
    self.numeroDeSala = numeroDeSala
    self.tipoDeSala = tipoDeSala

  def repr(self)->str:
    return str(self.butacas)

  def ocuparAsiento(self, filaAOcupar, columnaAOcupar, dni, edad):
    cantFilas, cantCol = self.butacas.shape
    if (cantFilas > filaAOcupar and cantCol > columnaAOcupar):
      if self.butacas[filaAOcupar, columnaAOcupar] == None:
        self.butacas[filaAOcupar, columnaAOcupar] = Espectador(dni, edad)
      else:
        raise Exception("El asiento ya fue ocupado")
    else:
      raise Exception("No existe la fila y/o la columna en esta sala")

  def obtenerFila(self, nroFila):
    return self.butacas[nroFila]

  def asientosVaciosFila(self, fila):
    cantFilas, cantCol = self.__butacas.shape
    cantidadFilasVacias = 0
    filaABuscar = self.obtenerFila(fila)
    for butaca in filaABuscar:
      if butaca == None:
        cantidadFilasVacias = cantidadFilasVacias + 1
    return cantidadFilasVacias

  def gananciaTotal(self) -> int:
    ganancia = 0
    for fila in self.butacas:
        for butaca in fila:
            if butaca != None:
                ganancia += butaca.valorEntrada()
    return ganancia

class Espectador:

  def init(self, dni, edad):
    self.dni = dni
    self.edad = edad

  def repr(self):
    return "ocupado"

  def edad(self):
    return self.__edad

  def valorEntrada(self, valorEntrada, tipoSala):
    pass
