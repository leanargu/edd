# Clase 4: Colecciones y Arreglos (NumPy)

En esta clase profundizamos en el concepto de **Colecciones** y nos enfocamos en la implementación práctica de **Arreglos** (vectores y matrices) utilizando la librería `NumPy`.

---

## 📦 Colecciones
Una **colección** es un tipo de variable que contiene múltiples elementos bajo un mismo nombre.

### Clasificación General
1.  **Según el tipo de elementos:**
    *   **Homogéneas:** Todos los elementos son del mismo tipo (ej. todos `int`).
    *   **Heterogéneas:** Pueden contener diferentes tipos de datos.
2.  **Según su organización:**
    *   **Ordenadas:** Cada elemento tiene una posición (índice) definida.
    *   **Desordenadas:** No hay un orden garantizado.
3.  **Según el almacenamiento:**
    *   **Estáticas:** Tamaño fijo definido en tiempo de compilación/inicialización (contiguas en memoria).
    *   **Dinámicas:** Su tamaño puede variar durante el *runtime* (enlazadas).

---

## 🏗️ Estructura de Datos
Definimos una **Estructura de Datos** como la combinación de:
*   Un **conjunto de elementos** organizados de una forma específica.
*   Un **conjunto de operaciones** que se pueden realizar sobre ellos.
*   Un criterio de **eficiencia y uso** de recursos.

---

## 🔢 Arreglos (Arrays)
Los arreglos son la estructura de datos más básica. Sus características principales son:
*   **Homogéneos:** Todos sus elementos son del mismo tipo.
*   **Estáticos:** Una vez creados, su tamaño no cambia.
*   **Ordenados:** Se accede a ellos mediante un índice numérico.

### 🛠️ Declaración y Creación (NumPy)
Para trabajar con arreglos en Python, utilizamos `import numpy as np`.

| Operación | Sintaxis | Descripción |
| :--- | :--- | :--- |
| **Ceros** | `np.zeros(5, int)` | Crea un vector de 5 enteros inicializados en 0. |
| **Vacío** | `np.empty(5, int)` | Reserva memoria pero contiene "basura" (más rápido). |
| **Lleno** | `np.full(5, 7)` | Crea un vector lleno con el valor especificado (ej. 7). |
| **Manual** | `np.array([1, 2, 3])` | Crea un arreglo con valores ya definidos. |

#### Matrices (Bidimensionales)
```python
# Creación de una matriz de 5x5 inicializada en 0
matriz = np.zeros((5, 5), int)

# Propiedades de tamaño
total_elementos = len(vector)     # Cantidad de elementos (Vectores)
dimensiones = matriz.shape       # Retorna (filas, columnas)
cant_filas = len(matriz)         # Número de filas
cant_cols = len(matriz[0])       # Número de columnas
```

### 🔄 Recorrido de Arreglos
Existen dos formas principales de recorrer un arreglo:

1.  **Por elementos (Directo):**
    ```python
    for elemento in vector:
        print(elemento)
    ```
2.  **Por índices (Usando `range`):**
    ```python
    for i in range(len(vector)):
        print(vector[i])
    
    # Recorrido inverso
    for i in reversed(range(len(vector))):
        print(vector[i])
    ```

---

## 🛠️ Algoritmos Fundamentales
Lógicas clave implementadas en la práctica (`clase4.py`) para manipular datos manualmente.

### 1. Inversión (In-place Logic)
Para invertir sin usar funciones nativas, se crea un nuevo arreglo y se recorre el original de forma inversa:
*   `nuevo_indice = largo - i - 1`

### 2. Desplazamientos (Shifting)
*   **A la derecha:** El elemento `i` pasa a `i+1`. El último elemento vuelve a la posición `0`.
*   **Inserción:** Para insertar en `K`, se desplazan todos los elementos desde `K` hacia la derecha. El último elemento se pierde.

### 3. Eliminación (Deletion)
*   Se elimina el elemento en la posición `K` y los elementos a su derecha se desplazan hacia la izquierda.
*   Se suele completar el espacio vacío al final con un `0` o valor nulo.

---

## 📈 Eficiencia y Complejidad
Es fundamental analizar cuánto "cuesta" cada operación:
*   **Acceso por índice:** $O(1)$ - Instantáneo.
*   **Búsqueda/Recorrido:** $O(n)$ - Proporcional a la cantidad de elementos.
*   **Eliminar Apariciones:** Si se usa un desplazamiento por cada coincidencia, la complejidad puede llegar a **$O(n^2)$** (Bucle dentro de bucle).

---

## ⚠️ Detalles Técnicos y Errores Comunes
*   **Pasaje por Referencia:** Los arreglos NO se copian automáticamente al asignarlos (`a = b` hace que ambos apunten a lo mismo). Usar `.copy()` para duplicar.
*   **Índices Negativos:** Python permite `vector[-1]` para el último elemento, pero hay que tener cuidado de no perder la lógica de la estructura de datos pura.
*   **TypeError:** Intentar meter un `string` en un arreglo de `int` definido con NumPy.

*   **Nota de Cursada:** No profundizamos en arreglos multidimensionales (más de 2D) en esta cursada.
