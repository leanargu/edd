def suma_de_arrays(arr1, arr2, arr3):
    if len(arr1) == 0:
        arr3 = []
    else:
        arr3 = [arr1[0] + arr2[0]] + suma_de_arrays(arr1[1:], arr2[1:], arr3[1:])
    return arr3

print(suma_de_arrays([2,3,4],[1,2,3],[0,0,0]))