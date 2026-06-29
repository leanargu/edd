# 🚀 Clase 7: Recursividad en Estructuras de Datos

Cuando aplicamos recursividad a vectores o matrices, el secreto está en **cómo particionamos la estructura** en cada llamada para que sea cada vez más pequeña.

## 🔪 Técnica Maestro: Slicing en Python
El slicing es la herramienta fundamental para "achicar" estructuras sin usar contadores manuales.

- **`v[1:]` (Cola):** Saca el primer elemento. Se usa para recorridos de izquierda a derecha.
- **`v[:-1]` (Frente):** Saca el último elemento. Se usa para recorridos de derecha a izquierda.
- **`v[1:-1]` (Interior):** Saca ambos extremos. Clave para algoritmos de simetría (**Palíndromos**).

---

## 📋 Generalización de Algoritmos (Machete)

### 1. El Recorrido Lineal (Suma, Máximo, Búsqueda Simple)
Procesamos la "cabeza" y delegamos el resto.
```python
def procesar(v):
    res = None
    # CASO BASE: Estructura vacía o con 1 solo elemento
    if len(v) == 0: 
        res = 0
    elif len(v) == 1: 
        res = v[0]
    else:
        # CASO RECURSIVO: Operar v[0] con el resultado de procesar el resto
        res = v[0] + procesar(v[1:])
    return res
```

### 2. El Patrón de Búsqueda Binaria (Divide y Vencerás)
Es mucho más eficiente porque reduce el problema a la mitad en cada paso.
1.  Calcular el `medio = len(v) // 2`.
2.  Si `v[medio]` es el dato, ¡Encontrado!
3.  Si `dato < v[medio]`, busco en la mitad izquierda: `v[:medio]`.
4.  Si `dato > v[medio]`, busco en la mitad derecha: `v[medio+1:]`.
**⚠️ Importante:** El vector DEBE estar ordenado.

### 3. El Patrón "In-Place" (Modificación del Vector)
Cuando el algoritmo debe alterar los elementos del vector original (visto en el ejercicio `vir`).
```python
def vir(v):
    if len(v) > 1:
        # 1. Realizar lógica de intercambio (Swap) si corresponde
        if v[1] < v[0]:
            v[0], v[1] = v[1], v[0]
        
        # 2. Seguir con el resto del vector
        vir(v[1:])
```

---

## 🏁 Casos Especiales para el Parcial

### 🧩 Recursividad en Matrices
Para recorrer una matriz de forma recursiva, tratamos las filas como si fueran elementos de un vector.
- Caso Base: `matriz.shape[0] == 0` (No quedan filas).
- Caso Recursivo: Procesar la fila actual `matriz[0]` (puede ser con un bucle o otra función recursiva) y luego llamar con `matriz[1:]`.

### 🔤 Recursividad en Strings
Se comportan exactamente igual que los vectores. 
- *Inversión:* `res = invertir(cadena[1:]) + cadena[0]`
- *Filtrado:* `res = (cadena[0] if cumple else "") + filtrar(cadena[1:])`

---

## 🛠️ Checklist de Errores (Evitá el 2)
- [ ] **¿Mi caso base realmente corta?** Chequeá `len(v) == 0` o `len(v) == 1`.
- [ ] **¿Estoy pasando una versión reducida en la llamada recursiva?** Si pasás `v` en vez de `v[1:]`, se tilda.
- [ ] **¿Puse el `return` en la llamada recursiva?** Sin `return`, el resultado de las llamadas hijas nunca le llega a la madre.
- [ ] **¿Manejé los `None`?** Si la estructura es de objetos (TDA), siempre preguntar `if v[0] is not None:` antes de acceder a sus métodos.
