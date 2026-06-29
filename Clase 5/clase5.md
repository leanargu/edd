# TDA (Tipos de Datos Abstractos)

- Problemas asociados a objetos.
- La información no aparece plana en datos simples.
- Es un proceso de abstracción.

## Estructura de Datos
Conjunto de elementos organizados.
**Colecciones:** No pensadas para representar un objeto particular. ¿Qué pasa si no usamos ninguna colección?

- **Lado del usuario:** Programador que usa un TDA sin conocer su implementación, solo sabe qué problema resuelve.
- **Lado del desarrollador:** Programador que dada una especificación, crea un TDA.

### Interface
Conjunto de operaciones (funciones) creadas por el desarrollador que permiten utilizar el TDA:
- Creación (constructor).
- Modificación.
- Lectura/Acceso.

**Ocultamiento:** El usuario sabe qué puede hacer, pero no cómo lo hace internamente.
**Encapsulamiento:** El usuario no puede modificarlo ni acceder a su interior directamente.

### Proceso de Modelado
- **Especificación:** ¿Para qué se va a usar? ¿Dónde?
- **Modelo:** ¿Qué elementos necesito para modelar el objeto?
- **Implementación:** ¿Cómo guardo esos elementos tecnicamente? ¿Qué tipos de variables uso?
- **Operaciones:** ¿Qué necesito que se haga con la estructura? (Interfaz).

---

## Sintaxis y Clases en Python

### Creación de una Clase
```python
class Aula:
    # Constructor
    def __init__(self, lugares: int, tiene_aire: bool, tiene_pantalla: bool):
        self.lugares = lugares
        self.alumnos = 0
        self.tiene_aire = tiene_aire
        self.tiene_pantalla = tiene_pantalla
        self.materia = ""
        self.nombreDocente = ""

    # Representación (ToString)
    def __repr__(self) -> str:
        return f"Cant. Lugares: {self.lugares} (Alumnos: {self.alumnos})"

    # Igualdad (Equal)
    def __eq__(self, otra_aula) -> bool:
        return self.lugares == otra_aula.lugares

    def ingresar_estudiantes(self, cantidad: int) -> None:
        if self.alumnos + cantidad <= self.lugares:
            self.alumnos += cantidad
        else:
            raise Exception("Capacidad excedida")

# Uso
aula1 = Aula(50, True, True)
```

---

## 🛠️ Funciones Primitivas (Métodos Mágicos / Dunder Methods)
Al momento de construir clases, es fundamental tener en cuenta este orden de funciones primitivas para definir el comportamiento de nuestros objetos.

### 1. Representación y Creación
Son fundamentales para inicializar el objeto y para su visualización.
- `__init__(self, ...)`: El constructor. Es donde asignás los valores iniciales de los atributos del objeto.
- `__str__(self)`: Define qué se ve cuando hacés `print(objeto)`. Debe retornar un string amigable y legible para el usuario final.
- `__repr__(self)`: Orientado al desarrollador. Debe ser un string que aporte información técnica precisa, ideal para debugging.

### 2. Comparación (Sobrecarga de operadores)
Ideales para la lógica de negocios (ej. comparar si dos aulas tienen la misma capacidad).
- `__eq__(self, other)`: Define el comportamiento del operador igualdad (`==`).
- `__ne__(self, other)`: Define el comportamiento del operador distinto (`!=`).
- `__lt__(self, other)`: Define el "menor que" (`<`). Útil si querés que una lista de tus objetos se pueda ordenar nativamente con `.sort()`.

### 3. Aritmética (Sobrecarga matemática)
Se usan mucho cuando manejás modelos con valores numéricos o acumulables.
- `__add__(self, other)`: Permite usar el operador de suma (`+`) entre objetos.
- `__sub__(self, other)`: Permite usar el operador de resta (`-`).
- `__mul__(self, other)`: Permite usar el operador de producto (`*`).

### 4. Manejo de Contenedores
Permiten que tu objeto se comporte como una estructura de datos nativa (lista o diccionario).
- `__len__(self)`: Para que funcione la función `len(objeto)`.
- `__getitem__(self, key)`: Para acceder a datos usando corchetes: `objeto[key]`.
- `__contains__(self, item)`: Para permitir el uso del operador `in`.

---

## 🧠 El uso de `self` en Python
`self` es una referencia a la **instancia actual de la clase**. Permite acceder a los atributos y métodos asociados a ese objeto específico.

**¿Cuándo conviene recibir o no el `self`?**
- **Métodos de Instancia (Siempre reciben `self`):** Si la función necesita acceder o modificar atributos del objeto (ej. `self.alumnos`), obligatoriamente el primer parámetro debe ser `self`.
- **Invocación interna:** Cuando llamas a un método de la clase desde *otro* método de la misma clase, se hace mediante `self.metodo()`. En este caso, **no hace falta volver a pasar el `self` como argumento** a la función interna, porque Python lo inyecta automáticamente.
  *Ejemplo:*
  ```python
  class Ejemplo:
      def metodo_interno(self):
          print("Ejecutado")

      def metodo_externo(self):
          # Llama al método interno usando self., sin pasarle 'self' en los paréntesis.
          self.metodo_interno() 
  ```
- **Métodos Estáticos (`@staticmethod`):** Si la función no interactúa con ningún dato de la instancia (no usa `self.nada`), se le puede colocar el decorador `@staticmethod` y definirla sin recibir `self`. Es como una función suelta empaquetada dentro de la clase por cuestiones de orden.