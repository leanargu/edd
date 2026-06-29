def incluido_al_final(a1, a2) -> bool:
    esta_incluido = False
    if len(a2) == 0:
        esta_incluido = True
    else:
        if len(a1) == len(a2):
            esta_incluido = a1 == a2
        else:
            esta_incluido = incluido_al_final(a1, a2[1:])
    return esta_incluido

print(incluido_al_final([2,5,1], [3,4,2,5,1]))