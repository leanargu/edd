## Clase 2: Repaso y Funciones

En esta clase 2 arrancamos repasando los ejercicios de la clase 1 y luego nos enfocamos en el tema de funciones.

---

### Bucle `for` y la función `range()`

La función `range()` se utiliza frecuentemente junto con el bucle `for` para iterar sobre una secuencia de números. Admite hasta tres parámetros:
- **start** (opcional): El valor inicial de la secuencia. Por defecto es `0`.
- **stop** (obligatorio): El valor límite de la secuencia. La iteración se detiene *antes* de llegar a este número.
- **step** (opcional): El incremento entre cada número de la secuencia. Por defecto es `1`.

**Ejemplo Práctico:**
```python
# Imprime los números del 2 al 8, saltando de a 2
for i in range(2, 10, 2):
    print(i)
```

**Errores Comunes:**
- `TypeError`: Pasar un valor no entero a `range()` (ej. un `float` o un `string`).

---

### Funciones

Las **funciones** son bloques de código diseñados para realizar una tarea particular y devolver un resultado. Siguen el principio de **Divide and Conquer** (dividir y conquistar), permitiendo fragmentar un problema grande en problemas más chicos y manejables.

Pueden estar en cualquier lado del archivo del programa, o incluso en otros archivos.
*Por ejemplo:* `print()` es una función que el intérprete busca internamente y sabe cómo usarla.

#### Interacción con el Programa Principal
El programa principal es quien se encarga de llamar a las funciones.
- **Entrada:** Son los datos (*parámetros* o *argumentos*) que se envían desde el programa principal a la función.
- **Salida:** Son los datos (*valor de retorno*) que la función envía de vuelta al programa principal.

#### Definición de una Función
- El **nombre** de la función debe ser indicativo de lo que hace.
- Los **parámetros** son las variables que se usan como entrada.
- La **salida** se define como parte de la función usando la palabra reservada `return`. Aunque en Python no es estrictamente obligatorio restringir el tipo de dato, como **buena práctica** vamos a definir el tipo de retorno de la función (Type Hinting).

**Ejemplo Práctico (Saludo):**
```python
def generar_saludo(nombre: str) -> str:
    """Retorna un saludo personalizado."""
    return f"¡Hola, {nombre}!"

# Llamada en el programa principal
mensaje = generar_saludo("Estudiante")
print(mensaje)
```

#### Alcance de Variables (Scope)
El alcance o *scope* define desde dónde es accesible una variable:
- **Variables Locales:** Las variables declaradas *dentro* de una función solo existen allí. No pueden ser accedidas desde el programa principal (`main`) ni desde otras funciones.
- **Variables Globales:** Las variables declaradas en el programa principal pueden ser leídas por las funciones, pero **no es una buena práctica** modificarlas directamente dentro de ellas (salvo usando la palabra clave `global`, lo cual se desaconseja).

**Errores Comunes:**
- `NameError`: Intentar acceder a una variable local desde el programa principal o fuera de su scope.

---

### Tipos de Pasaje de Argumentos

- **Paso por Valor:** La función recibe una *copia* del valor. Las modificaciones dentro de la función **no afectan** a la variable original del programa principal.
  - *Se aplica a:* Tipos primitivos (`int`, `float`, `str`, `bool`).
- **Paso por Referencia:** La función recibe una *referencia* a la dirección de memoria del dato. Si se modifica la estructura de datos dentro de la función, la variable original **también se ve afectada**.
  - *Se aplica a:* Objetos complejos (`list`, `dict`, clases custom, etc.).

---

### Parámetros con Valor por Defecto

Python permite asignar **valores por defecto** a los parámetros al definir la función. Si no se provee ese argumento al momento de llamar a la función, se utilizará el valor por defecto.

**Ejemplo Práctico:**
```python
def sumaInt(num1: int = 0, num2: int = 0) -> int:
    return num1 + num2

print(sumaInt(5)) # num2 tomará el valor por defecto 0. Salida: 5
```

**Errores Comunes:**
- `SyntaxError`: Definir parámetros sin valor por defecto *después* de un parámetro que sí tiene valor por defecto (ej. `def func(a=1, b):` es inválido).

**Premisa de Cursada:**
- No se alienta a tener múltiples `return` dentro de una sola función. En algunos casos será más eficiente utilizar un bucle `while`.