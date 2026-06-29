# Árboles - Guía Visual Definitiva (Modalidad Cátedra)

> [!NOTE]
> **Dashboard de Repaso:** ¡Foco especial en esta clase para el Parcial 2! Aquí se concentra la mayor dificultad teórica y práctica. 

## 🌳 1. Conceptos Básicos y Definiciones
- **Árbol Binario de Búsqueda (ABB):** La regla de oro es que **todo lo menor va a la izquierda** y **todo lo mayor va a la derecha**. NO admite duplicados.
- **Grado:** Cantidad de hijos de UN nodo (0, 1 o 2). Un nodo de grado 0 es una **Hoja**.
- **Peso:** Cantidad TOTAL de nodos en el árbol.
- **Altura:** Cantidad de enlaces desde un nodo dado hasta la hoja más lejana. (Altura de una hoja = 0).
- **Profundidad:** Cantidad de **enlaces** desde la Raíz hasta un nodo dado. (Profundidad de la raíz = 0). *¡Duda resuelta!*

---

## 🛠️ 2. El "Secreto" de la Cátedra (Patrón de Diseño)
En esta cátedra, **TODOS** los ejercicios de árboles se resuelven aplicando el mismo patrón de dos pasos:
1. **El Wrapper (Clase `ABB`):** Es el método público que no recibe nodos. Solo valida `if not self.estaVacio():` y delega la responsabilidad a la raíz: `return self.__raiz.miMetodoNodo()`.
2. **La Recursividad (Clase `__NodoArbol`):** Es el método privado donde ocurre la magia real. Se llama recursivamente a los subárboles `izquierdo` y `derecho`.

---

## 🧩 3. Segmentación: Tipos de Ejercicios y "Machetes"

### A. Segmento "Cálculos" (Peso, Altura, Conteo)
*Estos métodos devuelven un número entero y acumulan resultados de ambos lados.*

- **Machete Peso/Conteo:** `return 1 + lo_de_la_izq + lo_de_la_derecha`
- **Machete Altura:** `return 1 + max(altura_izq, altura_der)`

```python
# Ejemplo de Conteo (Peso) en __NodoArbol
def pesoNodo(self):
    peso = 1 # Me cuento a mí mismo (la raíz de este subárbol)
    if self.tieneIzquierdo():
        peso += self.izquierdo.pesoNodo()
    if self.tieneDerecho():
        peso += self.derecho.pesoNodo()
    return peso
```

### B. Segmento "Búsquedas" (Buscar Dato, Máximo, Mínimo)
*Aquí es vital usar la propiedad del ABB para **evitar recorrer todo el árbol**. Si busco un 10 y estoy en un 20, **solo** voy a la izquierda.*

- **Búsqueda Simple (Cualquier valor):** Comparar el dato buscado con el dato actual (`self.dato`). Si es igual, lo encontré. Si es menor, voy a la izquierda. Si es mayor, voy a la derecha. (¡Siempre retornar lo que devuelve la llamada recursiva!).
- **Mínimo:** Ir todo a la izquierda hasta que `tieneIzquierdo()` sea `False`.
- **Máximo:** Ir todo a la derecha hasta que `tieneDerecho()` sea `False`.

```python
# Ejemplo de Búsqueda Simple (Cualquier valor)
def buscarNodo(self, datoBusc):
    if self.dato == datoBusc:
        return self
    elif datoBusc < self.dato and self.tieneIzquierdo():
        return self.izquierdo.buscarNodo(datoBusc)
    elif datoBusc > self.dato and self.tieneDerecho():
        return self.derecho.buscarNodo(datoBusc)
    return None # Si llego acá, no estaba en el árbol
    
# Ejemplo de Máximo
def maximoNodo(self):
    if self.tieneDerecho():
        return self.derecho.maximoNodo()
    return self # Si no hay derecha, yo soy el máximo.
```

### C. Segmento "Recorridos Acumulativos" (Listas)
*Ejercicios donde te piden devolver una lista con los elementos (pares, impares, mayores a X, ordenados).*

> [!IMPORTANT]  
> **Regla de Oro:** ¡NUNCA instanciar la lista `[]` adentro de la función recursiva! La lista se crea en el Wrapper (`ABB`) y se pasa **por parámetro** a `__NodoArbol`.

```python
# En la clase ABB
def listaDePares(self):
    listaPares = [] # Se crea acá
    if not self.estaVacio():
        self.__raiz.listaDeParesNodo(listaPares) # Se pasa por referencia
    return listaPares

# En la clase __NodoArbol
def listaDeParesNodo(self, lista):
    # Recorrido IN-ORDER (Garantiza que la lista quede ordenada de menor a mayor)
    if self.tieneIzquierdo():
        self.izquierdo.listaDeParesNodo(lista)
        
    if self.dato % 2 == 0:
        lista.append(self.dato) # In-Place append!
        
    if self.tieneDerecho():
        self.derecho.listaDeParesNodo(lista)
```

### D. Segmento "Modificaciones Críticas" (Eliminar)
Para que el ABB no se rompa al eliminar un nodo con 2 hijos, hay que reemplazarlo por el:
- **Predecesor:** El máximo del subárbol izquierdo (El más grande de los más chicos).
- **Sucesor:** El mínimo del subárbol derecho (El más chico de los más grandes).

---

## 📝 4. Ejercitación Obligatoria (Simulacro Parcial 2)

A continuación, 3 ejercicios con estructura idéntica a la que tomarán en el parcial. **¡Intentá resolverlos por tu cuenta en los archivos correspondientes!**
*(Además, tenés una batería completa de 14 ejercicios en [Ejercicios_de_2do_parcial.ipynb](file:///Users/leanarguello/Documents/Personal/Universidad/tecnicatura-universitaria-en-programacion/2do-a%C3%B1o/1er-cuatrimestre/estructura-de-datos/Practicas%20Parcial%202/Ejercicios_de_2do_parcial.ipynb) que subiste para practicar).*

### Ejercicio 1: Mapas / Diccionarios
**Enunciado:** Crear una función que reciba una lista de palabras y devuelva un diccionario donde la clave sea la longitud de la palabra (int) y el valor sea un *Set* (conjunto) con las palabras que tienen esa longitud. Validar que la lista no sea nula.

### Ejercicio 2: LinkedList (Listas Enlazadas)
**Enunciado:** Agregar un método a la clase `Lista` que reciba un número entero `N` y elimine todos los nodos cuyo valor sea múltiplo de `N`. (Ojo con perder las referencias de la lista, y asegurate de recorrer hasta el final usando punteros auxiliares `anterior` y `actual`).

### Ejercicio 3: Árboles (¡El más importante!)
**Enunciado:** Implementar el método `invertirArbol()` en la clase `ABB`. Este método debe convertir el árbol en su imagen especular (es decir, para **cada nodo**, su hijo izquierdo pasa a ser el derecho, y viceversa). 
*Hint:* Es un método del segmento de "Modificaciones", por lo que vas a necesitar el Wrapper y el método recursivo en `__NodoArbol`. Solo necesitas variables temporales para hacer el "swap" de `self.izquierdo` y `self.derecho`.