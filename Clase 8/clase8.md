# Pilas, Colas y Listas - Guía Visual (Clase 8)

> [!NOTE]
> **Dashboard de Repaso:** Según lo acordado, las Pilas y Colas no son tema evaluable práctico en el Parcial 2, pero los conceptos teóricos y el comportamiento en memoria son fundamentales.

## 📋 1. TDA Lista (Python nativo)
Sintaxis básica y operaciones elementales en Python:
`lista = []` o `lista = list()` o `lista = [1, 2, 3, 4]`

```python
# Operaciones más usadas
lista.append(dato)           # Agregar al final
lista.insert(pos, dato)      # Insertar en posición
lista.pop()                  # Elimina y retorna el último elemento
lista.remove(elemento)       # Elimina el elemento por valor
lista.count(elemento)        # Cuenta repeticiones
lista.index(dato)            # Obtener posición
elemento in lista            # Operador de pertenencia (ej: if x in lista)
lista1 = lista1 + lista2     # Concatenar
sublista = lista[inicio:fin] # Slicing
```

---

## 🥞 2. TDA Pila (Stack) - Estructura LIFO
**LIFO (Last In, First Out):** El último elemento que entra es el primero que sale. (Imaginá una pila de platos).

### Operaciones Estándar:
- `pila.push(elemento)`: Apila un elemento en el tope.
- `pila.pop()`: Saca y retorna el elemento del tope.
- `pila.top()`: Muestra qué elemento está en el tope sin sacarlo.

---

## 🛒 3. TDA Cola (Queue) - Estructura FIFO
**FIFO (First In, First Out):** El primero que entra es el primero que sale. (Imaginá la fila del supermercado).
No está permitido "colarse" (insertar elementos en posiciones intermedias).

### Operaciones Estándar:
- `queue.queue(elemento)`: Encola al final.
- `queue.deque()`: Desencola del frente.
- `queue.top()`: Muestra el elemento que está al frente (próximo a salir).

---

## ⚠️ 4. Python: Rebinding vs In-Place (¡Clave para Exámenes!)

Al pasar estructuras de datos (como listas, pilas o árboles) a una función, es vital entender cómo Python maneja las variables en memoria:

### In-Place (Modificación Directa - ✅ SE MANTIENE)
Usar métodos propios de la estructura u operadores de asignación en índices **modifica el objeto original en memoria**.
```python
def agregar_elemento(lista):
    lista.append(4)      # IN-PLACE: El objeto original cambia.
    lista[0] = "Cambio"  # IN-PLACE: El objeto original cambia.

mi_lista = [1, 2, 3]
agregar_elemento(mi_lista)
# mi_lista ahora es ["Cambio", 2, 3, 4]
```

### Rebinding (Reasignación - ❌ SE PIERDE FUERA DE LA FUNCIÓN)
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
