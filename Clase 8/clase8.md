# Lists, stacks y queues

## List
`lista = [] / list() / [1,2,3,4]`

### Operaciones
Agregar al final:         lista.append(dato)
Eliminar ultimo elemento: lista.pop() //Retorna tambien?
Eliminar elemento:        lista.remove(elemento)
Contar elemento:          lista.count(elemento)
Concatenar listas:        lista1 = lista1 + lista2
Acceder elemento:         lista[pos]
sublista:                 lista[inicio:fin+1]
Agregar al final:         lista.append(dato)
Reemplazar elemento:      lista[pos] = nuevoDato
Insertar elemento:        lista.insert(posicion,dato)
Obtener posicion de elemento: lista.index(dato)
eliminar
operador in:              elemento in lista -> ej: `if not elemento in lista:`

# Stacks y queues dinámicas

## Stack
Apila cosas, puedo remover/agarrar solo el último elemento que inserté (top)

El ultimo que entra es el primero que sale
LIFO
Last in, first out

### Operaciones
Mete elemento en la pila:   pila.push(elemento) 
Saca el elemento del top:   pila.pop()
Muestra que hay en el top:  pila.top()

## Queues
Puede accederse desde atras o adelante. No esta permitido "colarse" (insertar en elementos intermedios)

El primero que entra es el primero que sale
FIFO
First in, first out

### Operaciones
Encolar:     queue.queue(elemento)
Desencolar:  queue.deque()
Tope:        queue.top()???

#### Para tener en cuenta
Parcial: Ejercicios de TDA con pilas y colas

---

## ⚠️ Python: Rebinding vs In-Place (¡Clave para Exámenes!)

Al pasar estructuras de datos (como listas o pilas) a una función, es vital entender cómo Python maneja las variables:

### 1. In-Place (Modificación Directa - ✅ SE MANTIENE)
Usar métodos propios de la estructura u operadores de asignación en índices **modifica el objeto original en memoria**.
```python
def agregar_elemento(lista):
    lista.append(4)      # IN-PLACE: El objeto original cambia.
    lista[0] = "Cambio"  # IN-PLACE: El objeto original cambia.

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista)
# mi_lista ahora es ["Cambio", 2, 3, 4]
```

### 2. Rebinding (Reasignación - ❌ SE PIERDE FUERA DE LA FUNCIÓN)
Usar el operador `=` para asignar un **nuevo objeto** a la variable local hace que apunte a otro espacio en memoria, rompiendo el vínculo con el objeto original.
```python
def vaciar_lista(lista):
    lista = []           # REBINDING: Crea una nueva lista en memoria.
    # El objeto original [1, 2, 3] NO se modifica.

mi_lista = [1, 2, 3]
vaciar_lista(mi_lista)
# mi_lista SIGUE SIENDO [1, 2, 3]
```
> [!IMPORTANT]
> **Regla de oro:** Si necesitas vaciar o reasignar completamente una estructura pasada por parámetro, usa sus métodos (ej. `lista.clear()`, o `pila.vaciar()`) y no el operador `=`, a menos que la función retorne esa nueva estructura y la pises en el scope principal (`mi_lista = vaciar_lista(mi_lista)`).
