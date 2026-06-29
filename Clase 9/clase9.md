# Diccionarios (Mapas) - Guía Visual (Clase 9)

> [!NOTE]
> **Dashboard de Repaso:** ¡Tema seguro de Parcial 2! Suele tomarse un ejercicio de agrupar o clasificar datos en un diccionario usando como valores listas o conjuntos (`sets`).

## 🔑 1. Conceptos Clave
- **Clave-Valor (K, V):** Los diccionarios almacenan datos asociados a una clave única, en lugar de una posición o índice.
- **Claves Únicas e Inmutables:** No puede haber dos claves iguales. Además, el tipo de dato de la clave no puede modificarse (ej. podés usar `int`, `str`, o `tuplas`, pero NO `listas`).
- **Hashing:** Es el proceso que permite buscar datos de manera ultra-rápida ($O(1)$) calculando en qué lugar de memoria va cada elemento basándose en su clave.

> [!TIP]
> **Curiosidad: Función de Hashing Realista**
> Python utiliza funciones hash nativas optimizadas. Así se ve un hashing básico usando la función nativa `hash()`:
> ```python
> clave = "Lean"
> indice = hash(clave) % 100 # % 100 limita el índice a 0-99
> print(f"La clave '{clave}' va al índice: {indice}")
> ```

---

## 🛠️ 2. Operaciones Básicas del TDA Diccionario
*Asumiendo que usamos la interfaz teórica dada en clase para TDA Diccionario:*

| Operación | Descripción |
| :--- | :--- |
| `dic = Diccionario()` | **Constructor:** Inicializa el diccionario vacío. |
| `dic.get(clave)` | **Obtener:** Retorna el valor asociado a la clave (o nulo si no existe). |
| `dic.insert(clave, valor)` | **Insertar:** Agrega la dupla al diccionario. Si la clave ya existe, no la pisa (es inmutable en algunas cátedras). |
| `dic[clave] = valor` | **Operador Llave:** Versión mutable, pisa el valor si la clave ya existe. |
| `dic.remove(clave)` | **Eliminar:** Borra la clave y su valor asociado. |
| `dic.contains(clave)` | **Pertenece:** Retorna `True` si la clave existe. |

---

## 🧩 3. Segmentación: Patrones de Ejercicios

### A. Patrón de Búsqueda y Recorrido
Para imprimir, sumar o modificar valores recorriendo el diccionario, SIEMPRE iteramos sobre las claves (`keys`).

```python
# Machete de Recorrido Estándar
for clave in diccionario.keys():
    valor_actual = diccionario.get(clave)
    print(f"Clave: {clave} -> Valor: {valor_actual}")
```

### B. Patrón de Agrupación (Listas como Valores)
Este es el ejercicio de parcial por excelencia: Agrupar elementos que comparten una característica (ej. Palabras por longitud, Alumnos por nota).

```python
# Machete: Diccionario con listas en los values
notas = Diccionario()

def agregar_nota_a_alumno(nombre_alumno, nueva_nota):
    if not notas.contains(nombre_alumno):
        notas.insert(nombre_alumno, []) # Inicializamos la lista vacía si es la primera vez
    
    # Agregamos a la lista existente
    lista_actual = notas.get(nombre_alumno)
    lista_actual.append(nueva_nota)
```

### C. Patrón de Agrupación Única (Conjuntos/Sets como Valores)
Si el parcial pide que en la agrupación **"no haya elementos repetidos"**, usamos un Conjunto (`Set`) en vez de una Lista.

- **Set vs Lista:** `set()` guarda de manera constante sin repetidos y no tiene orden. Las listas mantienen orden de inserción y permiten repetidos.
- **Tuplas:** Son la alternativa ideal para claves compuestas (ej. `(nombre, apellido)`) porque son inmutables.
