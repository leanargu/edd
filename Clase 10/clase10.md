# Listas Enlazadas (LinkedList) - Guía Visual (Clase 10)

> [!NOTE]
> **Dashboard de Repaso:** ¡Tema seguro de Parcial 2! Acá la clave absoluta es **no perder la referencia de la lista** al manipular los punteros (`siguiente`).

## 🧠 1. Conceptos Básicos: Dinámico vs Estático

- **Estructura Estática:** Reserva tamaño fijo en memoria al compilar (ej. un arreglo tradicional en C/Java).
- **Estructura Dinámica (LinkedList):** El espacio cambia en tiempo de ejecución. Los elementos no ocupan memoria contigua, están dispersos pero mantienen su orden mediante **referencias (punteros)**.

### Estructuras basadas en Nodos
Un "Nodo" es la unidad básica. Se compone de dos partes:
1. `dato`: La información a guardar (int, string, objeto).
2. `siguiente`: El puntero que señala la ubicación en memoria del próximo nodo de la lista.

> [!WARNING]
> La LinkedList (como clase) **solo sabe dónde está el primer nodo** (`self.__primero`). Si rompés ese enlace o lo reasignás mal, ¡perdías el acceso a toda la lista!

---

## 🧩 2. Segmentación: Tipos de Ejercicios y "Machetes"

### A. Segmento "Recorridos" (Búsquedas, Conteos, Imprimir)
*Ejercicios donde solo hay que leer datos o contar nodos, sin agregar ni borrar nada.*

> [!IMPORTANT]
> **Regla de Oro del Recorrido:** NUNCA uses `self.__primero` para recorrer. Siempre creá un puntero auxiliar (`aux`) para no perder el inicio de la lista.

```python
# Machete: Iterar hasta el final
def recorrer_lista(self):
    aux = self.__primero
    while aux is not None:
        # Hacer algo con aux.dato (visitar)
        print(aux.dato)
        
        # Moverse al siguiente (¡Clave!)
        aux = aux.siguiente
```

### B. Segmento "Modificaciones" (Insertar Nodos)
*Ejercicios donde hay que agregar un nodo en una posición específica, al principio o al final.*

> [!TIP]
> **Regla de Inserción Intermedia:** *Primero engancho el nuevo nodo al resto de la lista, y RECIÉN AHÍ engancho el anterior al nuevo*. (Si lo hacés al revés, perdés el resto de la lista).

```python
# Machete: Insertar en medio (Teniendo el 'aux' parado en la posición anterior)
nuevo_nodo = Nodo(dato)
# 1. El nuevo nodo apunta a lo que apuntaba el aux
nuevo_nodo.siguiente = aux.siguiente 
# 2. El aux ahora apunta al nuevo nodo
aux.siguiente = nuevo_nodo
```

### C. Segmento "Eliminaciones" (Borrar por valor, posición, pares)
*Ejercicios donde hay que saltarse nodos para eliminarlos de la cadena.*

Para eliminar un nodo, necesitás estar parado en el nodo **ANTERIOR** al que querés borrar, para poder "puentearlo".

```python
# Machete: Eliminar el nodo siguiente al 'aux'
# aux está parado en el anterior al que queremos borrar
if aux.siguiente is not None:
    nodo_a_borrar = aux.siguiente
    # Punteamos: el aux apunta al que le sigue al que vamos a borrar
    aux.siguiente = nodo_a_borrar.siguiente
```

**Caso Especial: Eliminar el primer elemento**
Siempre requiere un bloque `if` separado, porque modifica la raíz de la clase:
```python
if self.__primero.dato == dato_a_borrar:
    self.__primero = self.__primero.siguiente # El segundo nodo pasa a ser el primero
```

---

## 📝 3. Clasificación de Estructuras por Punteros

- **Lineales (1 previo y 1 siguiente máximo):**
  - Listas, Pilas, Colas.
- **No Lineales (Más de 1 previo o más de 1 siguiente):**
  - **Árboles:** 1 padre, múltiples hijos.
  - **Grafos:** Múltiples conexiones (nodos arbitrarios conectados).
