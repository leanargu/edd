# Clase 1: Introducción y Repaso

## 📅 Cronograma y Fechas Clave

### Exámenes Parciales
- **Parcial 1:** 11 de Mayo
  - Temas: Tipos de datos abstractos, Recursividad, Arreglos/Matrices, Pilas y colas dinámicas.
- **Parcial 2:** 6 de Julio
  - Temas: Diccionarios y conjuntos, Listas enlazadas, Árboles.
- **Recuperatorios:** 13 y 17 de Julio.

### Ciclo Semanal (Modalidad)
- **Fin de semana:** Habilitación de pestaña en campus (videos y ejercicios).
- **Lunes:** Teórico presencial.
- **Viernes:** Práctica virtual sincrónica.
- **Consultas:** Discord (asincrónico).

---

## 🧠 Conceptos Teóricos

### Variables en Memoria
`var $nombreVariable = 'aula'`  
Los datos se almacenan en formato **binario** en la memoria RAM.

### Tipos de Datos Primitivos
- `int`: Enteros numéricos con signo. Ej: `dias = 2`.
- `float`: Reales con decimales. Ej: `radio = 25.6`.
- `str`: Cadena de caracteres (símbolos y palabras). Ej: `dia_actual = 'Lunes'`.
- `bool`: Lógica booleana. Ej: `necesita_validacion = True`.

### Casteo (Conversión de Tipos)
Transformación manual de tipos de variables usando funciones nativas. En general, **no se operan** variables de distinto tipo sin castear.

*Ejemplo de error común:*
```python
dia = 'Lunes'
precio = 25.4
suma = dia + precio  # TypeError: can only concatenate str (not "float") to str
```

*Forma correcta:*
```python
suma = dia + str(precio)
```

---

## ⚙️ Operadores y Sintaxis

### Operadores Aritméticos
- `+` Suma | `-` Resta | `*` Producto | `/` División
- `//` División entera | `%` Módulo (resto)

**Usos comunes:** Bucles y contadores.  
*Nota:* Es fundamental limitar los loops para evitar **overflow** (ej. en `while`).

### Operadores de Comparación
- `<` Menor | `>` Mayor | `>=` Mayor o igual | `<=` Menor o igual | `==` Igual | `!=` Distinto

### Reglas de Sintaxis en Python
1. **Identación:** Obligatoria (reemplaza las llaves `{}`).
2. **Case Sensitive:** Las mayúsculas y minúsculas importan (`Variable != variable`).
3. **Punto y coma:** No se utiliza `;` al final de las sentencias.
4. **Comentarios:**
   - Una línea: `#`
   - Múltiples líneas: `"""` o `'''`
5. **Tipado Dinámico:** El lenguaje infiere el tipo de dato automáticamente.

---

## 🛤️ Estructuras de Control

### Bifurcaciones Lógicas (Condicionales)
- **Simple:** `if condicion:`
- **Excluyente:** `if / else`
- **Múltiple:** `if / elif / else`

### Estructuras Repetitivas (Bucles)
- **for:** Se utiliza cuando el límite es conocido.
- **while:** Se utiliza cuando el límite es desconocido o depende de una condición.

---

## 📦 Funciones (Divide y Vencerás)
Permiten separar el código repetitivo en bloques reutilizables.

```python
def sumar(a: int, b: int) -> int:
    resultado = a + b    
    return resultado
```

### Reglas de Parámetros e Invocación
Al invocar una función, se debe respetar:
1. **Cantidad** de parámetros.
2. **Orden** de los mismos (por defecto).
3. **Tipo de dato**.

#### Argumentos Nombrados (Keyword Arguments)
Permiten especificar el nombre del parámetro al invocar la función, lo que permite **alterar el orden** original definido en la declaración. Esto mejora la legibilidad, especialmente en funciones con muchos parámetros.

*Ejemplo mejorado (Cálculo de Interés):*
```python
def calcular_interes(capital: float, tasa: float, tiempo_anios: int) -> float:
    return capital * tasa * tiempo_anios

# Invocación tradicional (respetando el orden)
interes1 = calcular_interes(1000.0, 0.05, 2)

# Invocación con argumentos nombrados (orden alterado para claridad)
interes2 = calcular_interes(tasa=0.05, tiempo_anios=2, capital=1000.0)
```
*En este caso, aunque el orden cambie, el compilador sabe qué valor corresponde a cada parámetro gracias al nombre.*

### Scope de Variables (Encapsulamiento)
El alcance de las variables fluye **de afuera hacia adentro**:
- Las variables **globales** son accesibles desde cualquier parte.
- Las variables **locales** (definidas dentro de una función) son privadas a ese bloque.
- Python permite nombres compartidos: una variable local puede tener el mismo nombre que una global sin conflicto.

### Pasaje de Datos
- **Por Valor:** Se recibe una copia del valor (típico en tipos **primitivos**).
- **Por Referencia:** Se recibe el puntero exacto (típico en tipos **no primitivos** como Listas o Diccionarios). Python optimiza forzando el paso por referencia en estos casos.