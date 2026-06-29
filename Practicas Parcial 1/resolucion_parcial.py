#[1,3,5,7,9,11]
#-> [3,5,7,9,11] -> ArrayAchicado, 3-1
#-> [5,7,9,11] -> ArrayAchicado, 5-3
#-> [7,9,11] -> ArrayAchicado, 7 - 5
#-> [9,11]-> ArrayAchicado, 9 - 7
#-> [11]
                                 #2
arr = [1,3,5,7,9,11]
diferencia_primeros_dos_elementos = arr[1] - arr[0]

def tiene_misma_diferencia_r(arr, diff=None):
    esDiff = False
    if(len(arr) < 2):
        esDiff = True
    else:
        diferencia = arr[1] - arr[0]
        if diff is None:
            esDiff = tiene_misma_diferencia_r(arr[1:],diferencia)
        else:
            esDiff = diff == diferencia and tiene_misma_diferencia_r(arr[1:],diferencia)

    return esDiff

def tiene_misma_diferencia(arr):
    esDiff = False
    if len(arr) > 2:
        esDiff = tiene_misma_diferencia_r(arr[1:])

    return esDiff

