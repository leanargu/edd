class Propiedad:
    def __init__(self,
                 calle: str, numero: int, localidad: str,
                 ano_construccion: int, ambientes: int
                 ):
        self.__calle = calle
        self.__numero = numero
        self.__localidad = localidad
        if ano_construccion < 1870:
            raise Exception()
        self.__ano_construccion = ano_construccion
        self.__ambientes = ambientes

    def __repr__(self):
        return f"{self.__calle} {self.__numero} ({self.__localidad})"

    def propiedad(self):
        return self.__localidad

    #GEMINI: Mientras estemos dentro de la clase, se puede invocar a atributos privados si el tipo de argumento es el tipo de la clase. Explicalo mejor con tus palabras
    def mismaLocalidad(unaPropiedad, otraPropiedad):
        return unaPropiedad.__localidad == otraPropiedad.__localidad

    def mismaCalle(unaPropiedad, otraPropiedad):
        return unaPropiedad.__calle == otraPropiedad.__calle

    """
    mayorNumeración: Operación que recibe dos propiedades 
    y si están en la misma calle de la misma localidad, retorna la propiedad que posee mayor 
    numeración. 
    Si están calles o en localidades diferentes debe lanzar una excepción.
    """

    def mayorNumeración(unaPropiedad, otraPropiedad):
        if (not Propiedad.mismaCalle(unaPropiedad, otraPropiedad) or
                not Propiedad.mismaLocalidad(unaPropiedad,otraPropiedad)):
            raise Exception("Las propiedades deben estar en la misma calle o localidad")

        return Propiedad.__mayorNumeracion(otraPropiedad, unaPropiedad)

    def __mayorNumeracion(otraPropiedad, unaPropiedad):
        mayor = unaPropiedad
        if otraPropiedad.__numero > unaPropiedad.__numero:
            mayor = otraPropiedad
        return mayor

    def calculaImpuestoARBA(self):
        impuesto = 0

        if self.__ano_construccion < 1950:
            impuesto = self.__calcular_impuesto_antiguo()
        else:
            impuesto = self.__calcular_impuesto_actual()

        return impuesto

    def __calcular_impuesto_antiguo(self) -> int:
        impuesto = 0

        if 1 <= self.__ambientes <= 3:
            impuesto = 5
        elif 4 <= self.__ambientes <= 6:
            impuesto = 10
        else:
            impuesto = 25

        return impuesto

    def __calcular_impuesto_actual(self)-> int :
        impuesto = 0

        if 1 <= self.__ambientes <= 3:
            impuesto = 5
        else:
            impuesto = 35

        return impuesto

class Tiempo:
    def __init__(self, horas: int, minutos: int, seg: int):
        self.__horas = horas
        self.__minutos = minutos
        self.__seg = seg

    def __repr__(self) -> str:
        return f"{self.__horas}:{self.__minutos}:{self.__seg}"

    def tiempo_a_segundos(self) -> int:
        return self.__horas * 3600 + self.__minutos * 60 + self.__seg

    def tiempo_desde_segundos(segundos: int):
        horas = segundos // 3600
        segundos = segundos % 3600
        minutos = segundos // 60
        segundos = segundos % 60

        return Tiempo(horas, minutos, segundos)

    def __sub__(t1, t2):
        delta_en_seg = abs(Tiempo.tiempo_a_segundos(t1) - Tiempo.tiempo_a_segundos(t2))
        return Tiempo.tiempo_desde_segundos(delta_en_seg)

class Cronometro:
    def __init__(self):
        self.__tiempo_inicial: None
        self.__tiempo_final: None

    def __repr__(self) -> str:
        return f"Inicio: {self.__tiempo_inicial} - Fin: {self.__tiempo_final}"

    def comenzar(self, hora:int, minutos:int, seg:int):
        self.__tiempo_inicial = Tiempo(hora, minutos, seg)

    def finalizar(self, hora:int, minutos:int, seg:int):
        self.__tiempo_final = Tiempo(hora, minutos, seg)

    def tiempo_empleado(self) -> Tiempo:
        return self.__tiempo_inicial - self.__tiempo_final