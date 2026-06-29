def producto(n: int, m:int) -> int:
    res = None
    if m == 0:
        res = 0
    else:
        res = n + producto(n,m-1)
    return res

def fibonacci(pos: int) -> int:
    res = None
    if pos == 0:
        res = 0
    elif pos == 1:
        res = 1
    else:
        res = fibonacci(pos - 1) + fibonacci(pos - 2)
    return res

"""
1 cuando n = 0
1 cuando n = 1
N * (n-1)
"""
def factorial(n: int) -> int:
    res = None
    if n == 0:
        res = 1
    elif n == 1:
        res = 1
    else :
        res = n * factorial(n-1)
    return res

"""
dia 1 -> 2 gotas
dia >1 -> 2 gotas  + (dia - 1)

Dia 4
2 + 2 (dia3) + 2 (dia2) + 2
"""
def canilla(dia: int) -> int:
    res = None
    if dia == 1:
        res = 2
    else:
        res = 2 + canilla(dia - 1)
    return res

"""
Suma triangular
N = 1 -> 1
N > 1 -> N + suma(N-1)
"""

def suma_triangular(n: int) -> int:
    res = None
    if n == 1:
        res = 1
    else:
        res = n + suma_triangular(n - 1)
    return res

"""
si cant_posteos <= 20 -> 1000
si cant_posteos > 20 -> 2 * calcular_seguidores(cant_posteos - 1) + 500
"""

def calcular_seguidores(cant_posteos: int) -> int:
    res = None
    if cant_posteos <= 20:
        res = cant_posteos * 1000
    else:
        res = (2 * calcular_seguidores(cant_posteos-1)) + 500
    return res


"""
# Si dia == 1 -> 100
# si dia es par -> 2 * colocar_baldosas(dia - 1)
# si dia es impar -> colocar_baldosas(dia - 2) + colocar_baldosas(dia - 1)
"""

def colocar_baldosas(dia: int) -> int:
    res = None
    if dia == 1:
        res = 100
    else:
        if dia % 2 == 0:
            res = 2 * colocar_baldosas(dia - 1)
        else:
            res = colocar_baldosas(dia - 1) + colocar_baldosas(dia - 2)

    return res

def calcular_total_baldosas(dia: int) -> int:
    res = None
    if dia == 1:
        res = colocar_baldosas(dia)
    else:
        res = colocar_baldosas(dia) + calcular_total_baldosas(dia - 1)
    return res

"""
12 -> Dia == 1
15 + algas(dia - 1) -> Dia > 1 <= 11
3 * algas(dia - 1) + 100 -> Dia > 11
"""

def algas(dia: int) -> int:
    res = None
    if dia == 1:
        res = 12
    elif dia > 1 and dia <= 11:
        res = 15 + algas(dia - 1)
    else:
        res = 3 * algas(dia - 1) + 100
    return res

def calcular_total_algas(dia: int) -> int:
    res = None
    if dia == 1:
        res = algas(dia)
    else:
        res = algas(dia) + calcular_total_algas(dia - 1)
    return res

"""
Escribir una función recursiva que calcule la potencia N de
un número M (M a la N), ambos números enteros positivos.
"""

def calculo_de_potencia(m: int, n: int) -> int:
    res = None
    if n == 1:
        res = m
    else:
        res = m * calculo_de_potencia(m, n-1)
    return res


"""
10
1 -> N=1
2 * N -> N es par
cucas(N-2) + cucas (N-1) -> N es impar
"""

def cucas(piso: int) -> int:
    res = None
    if piso == 1:
        res = 1
    elif piso % 2 == 0:
        res = 2 * piso
    else:
        res = cucas(piso - 2) + cucas(piso - 1)
    return res

def cucas_hasta_piso(piso: int) -> int:
    res = None
    if piso == 1:
        res = cucas(piso)
    else:
        res = cucas_hasta_piso(piso - 1) + cucas(piso)
    return res

def repetir_palabra(palabra: str, veces: int) -> int:
    res = None
    if veces == 1:
        return palabra
    else:
        res = palabra + repetir_palabra(palabra, veces - 1)
    return res

# Nos esta costando distinguir cuando te pide un total de un calculo hasta un
# dia especifico

def sueldo_en(sueldoBase, porc_amuento, mes_actual):
	res = 0
	if mes_actual == 1:
		res = sueldoBase
	else:
		res = porc_amuento * sueldo_en(sueldoBase, porc_amuento, mes_actual - 1)
	return res

print(sueldo_en(40_000, 1.02, 3))