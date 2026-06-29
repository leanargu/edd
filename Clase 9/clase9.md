# Diccionarios KV

## Funciones basicas
- Constructor
- get("key")
- insert("key", "value") -> Inmutable. No cambia el *value*
- ["key"] -> Mutable, si se pasa una key con el operador de llaves si se puede cambiar el *value*
- remove("key")
- contains("key")

## Caracteristicas
- Clave valor [key,value]
- Claves únicas

## Hashing
- Como puedo guardar elementos para encontrarlos de forma eficiente? No por posición(como en una lista), sino por elemento.
- Dato -> Función Hash(dato) -> Memoria
- Dato -> Función Hash(dato) -> Memoria

> [!NOTE]
> **Curiosidad: Función de Hashing Realista**
> Python utiliza internamente funciones de hash nativas optimizadas. Así se ve un hashing básico usando la función nativa `hash()`:
> ```python
> # hash() convierte el string en un entero único (para esa sesión)
> clave = "Lean"
> indice_memoria = hash(clave) % 100 # % 100 limita el índice a un rango de 0-99
> print(f"La clave '{clave}' se guardará en el índice: {indice_memoria}")
> # Salida esperada: La clave 'Lean' se guardará en el índice: 42 (por ejemplo)
> ```
> *En sistemas de criptografía (ej. contraseñas) se usan hashes más complejos como SHA-256 (`hashlib.sha256()`), los cuales siempre devuelven el mismo hash para el mismo dato.*

## Conjuntos que podrian formar el TDA Diccionario
- Set: guarda de manera constante (o1) sin repetidos utilizando una tabla de hash. Puede servir para la clave
- Conjunto de arrays no se puede, porque son mutables
- Conjunto de tuplas: Es lo mejor.
  - Esta ordenada porque guarda por posición
  - Es inmutable
  - Ej `dic = {("c1","v1"), ("c2","v2"), ("c3","v3")}`

## Recorrido

```
diccionario = Diccionario()
for clave in diccionario.keys():
    print(diccionario.get(clave))
```

## Usando conjuntos como values

```
notas = Diccionario()
notas["Lean"].append(9)
```

