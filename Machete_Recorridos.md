# Machete: Recorridos de Arreglos y Matrices (Objetos)

Este machete combina los tipos de recorridos fundamentales con las **Reglas de Cursada** (Un solo `return`, Null-Safe y Validación de Límites).

---

## 📋 1. Recorrido de Arreglos (1D)

### A. Por Elemento (Solo Lectura)
Ideal cuando solo necesitamos consultar información. Incluye validación **Null-Safe**.
```python
def contar_cumplen_condicion(vector):
    contador = 0
    for objeto in vector:
        # Regla: Validar que no sea None antes de operar
        if objeto is not None and objeto.cumple_condicion():
            contador += 1
    return contador # Único punto de salida
```

### B. Por Índice (Lectura/Escritura)
Necesario para conocer la posición o modificar el vector. 
```python
def modificar_vector(vector):
    for i in range(len(vector)):
        # El índice 'i' está garantizado por el range, pero el contenido puede ser None
        if vector[i] is not None and vector[i].debe_modificarse():
            vector[i].aplicar_cambio()
```

---

## 📋 2. Recorrido de Matrices (2D)

### A. Por Elementos (Fila -> Elemento)
Útil para conteos o acumulaciones en toda la matriz de forma legible.
```python
def sumar_totales_matriz(matriz):
    acumulador = 0
    for fila in matriz:
        for objeto in fila:
            if objeto is not None:
                acumulador += objeto.get_valor()
    return acumulador
```

### B. Por Índices (Uso de While para Eficiencia y Único Return)
Fundamental para búsquedas donde queremos "cortar" el recorrido apenas encontramos algo, respetando la regla del **Single Return**.
```python
def buscar_coordenadas_objeto(matriz, valor_buscado):
    n_filas, n_cols = matriz.shape
    posicion = None # Variable de estado para el único return
    
    f = 0
    while f < n_filas and posicion is None:
        c = 0
        while c < n_cols and posicion is None:
            obj = matriz[f][c]
            if obj is not None and obj.get_id() == valor_buscado:
                posicion = (f, c) # Al asignar, los 'while' dejarán de iterar
            c += 1
        f += 1
    return posicion
```

---

## ⚠️ 3. Validación de Límites (Out of Bounds)

Siempre validar antes de acceder a una posición recibida por parámetro.
```python
def obtener_en_posicion(matriz, f, c):
    obj_encontrado = None
    n_f, n_c = matriz.shape
    
    # Regla: Validar límites de la matriz
    if 0 <= f < n_f and 0 <= c < n_c:
        obj_encontrado = matriz[f][c]
    else:
        print("Error: Índice fuera de los límites de la matriz.")
        
    return obj_encontrado
```

---

## 🧪 4. Patrones Comunes de Cálculo (Consolidados)

### Verificación (¿Existe alguno?)
```python
def hay_algun_disponible(vector):
    encontrado = False
    i = 0
    while i < len(vector) and not encontrado:
        if vector[i] is not None and vector[i].esta_disponible():
            encontrado = True
        else:
            i += 1
    return encontrado
```

### Promedio con Validación
```python
def promedio_edades(vector):
    resultado = 0
    suma = 0
    cantidad = 0
    
    for p in vector:
        if p is not None:
            suma += p.get_edad()
            cantidad += 1
            
    if cantidad > 0:
        resultado = suma / cantidad
        
    return resultado
```

---

## 🧠 5. Checklist para el Parcial
1.  **¿Tengo un solo `return` al final de la función?** (Si usaste `break` o `return` en el medio, cambialo por un `while` con booleano).
2.  **¿Validé `is not None`?** (Cualquier objeto en un arreglo/matriz puede ser nulo).
3.  **¿Validé los límites?** (Si recibís `f` o `c`, chequealos contra `shape`).
4.  **¿Usé métodos del objeto?** (Evitá `obj.__atributo`, usá `obj.get_atributo()`).

---

## 🌳 6. TDA, Listas Enlazadas y Árboles (Parcial 2)

### A. Listas Enlazadas: El Peligro del Bucle Infinito
Siempre, pero **siempre**, asegurate de avanzar tu puntero (`aux = aux.siguiente`) dentro de un `while`. 
*Cuidado al insertar nodos:* Si insertás un nodo y no lo saltás, en la próxima vuelta podrías volver a evaluarlo y entrar en un bucle infinito creando nodos sin parar.
```python
while aux.tiene_siguiente():
    if condicion:
        # 1. Crear nodo y engancharlo
        # 2. AVANZAR SALTEANDO EL NUEVO NODO
        aux = aux.siguiente.siguiente
    else:
        # Avanzar normal
        aux = aux.siguiente
```

### B. Árboles (ABB): Recursividad Limpia (Método en el Nodo)
En tu cursada aprendieron a resolver la recursividad creando un método en el Árbol que delega todo el trabajo a un método homónimo en el **Nodo**. 
¡Seguí esa misma estructura en el parcial para no fallar!

1. **Método en el Árbol (ABB):** Solo chequea si está vacío y llama a la raíz.
```python
def mi_metodo(self, params):
    if self.estaVacio():
        return 0 # o el valor base correspondiente
    return self.__raiz.mi_metodo(params)
```

2. **Método en el Nodo (`__NodoArbol`):** Toda la lógica recursiva y chequeo de hijos.
```python
def mi_metodo(self, params):
    resultado = ... # sumar mi propio dato si corresponde
    
    if self.tieneIzquierdo():
        resultado += self.izquierdo.mi_metodo(params)
    if self.tieneDerecho():
        resultado += self.derecho.mi_metodo(params)
        
    return resultado
```

### C. Diccionarios: Intersección vs Unión
- **Unión:** Sumar TODAS las claves de ambos diccionarios.
- **Intersección:** Sumar **SÓLO** las claves que comparten (están en el Diccionario 1 **Y** en el Diccionario 2). ¡No agregues claves que solo están en uno de los dos!

### D. Encapsulamiento en el Parcial (Papel)
Recordá que en el papel no hace falta pelear con el *name mangling* de Python. Accedés a los atributos privados de las clases usando sus dos guiones bajos de forma natural:
- Lista: `self.__primero`
- Árbol: `self.__raiz`
- Instanciar un nodo de lista: `self.__NodoLista(dato)`
