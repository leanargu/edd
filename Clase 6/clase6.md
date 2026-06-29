# 🔄 Clase 6: Recursividad - Conceptos y Estrategias

La recursividad no es un "bucle con otro nombre", es una **filosofía de resolución de problemas** basada en la auto-referencia y la simplificación progresiva.

## 🧠 ¿Qué es la Recursividad?
Es una alternativa a la repetición (solución iterativa). Un problema se resuelve recursivamente si se puede dividir en sub-problemas de la misma naturaleza pero de menor tamaño.

### El Proceso de Recurrencia
1.  **Problema A:** Es el problema original (complejo).
2.  **División:** Se divide en partes B y C.
3.  **Identidad:** Si B es idéntico a A (pero más chico), el problema es recursivo.
4.  **Resolución:** Se resuelve B repitiendo el proceso hasta llegar a un caso trivial.

---

## 🛠️ Los dos pilares obligatorios
Toda función recursiva DEBE tener estos dos elementos. Si falta uno, el programa falla.

### 1. Caso Base (La condición de corte)
Es la solución explícita para la instancia más simple del problema. Sin esto, la función se llama a sí misma infinitamente hasta agotar la memoria (**Stack Overflow**).
*   *Ejemplo:* En un factorial, el caso base es `n=0` o `n=1`.

### 2. Caso Recursivo (La regla de recurrencia)
Es la lógica que une la solución del paso `N` con la solución del paso `N-1`. Es donde "achicamos" el problema.
*   *Ejemplo:* `Factorial(N) = N * Factorial(N-1)`.

---

## 🏗️ La Pila de Llamadas (Call Stack)
Es fundamental entender cómo funciona Python por dentro:
- Cada vez que una función se llama a sí misma, Python "pausa" la ejecución actual y abre una nueva "cajita" en la memoria (Stack).
- Las funciones no terminan hasta que el Caso Base devuelve un valor.
- En ese momento, la pila empieza a "desenrollarse": los valores vuelven hacia atrás completando las operaciones pendientes.

---

## ⚡ Patrones de Diseño para el Parcial
Aquí generalizamos los casos que vimos en la práctica:

### 📊 Patrón A: El Cálculo de Valor Único (Puntual)
Se usa para proyecciones o series matemáticas (Interés, Población, Bacterias).
```python
def calcular_valor(n):
    res = None
    # 1. Caso Base: El inicio de la serie
    if n == 1: 
        res = valor_inicial
    else:
        # 2. Caso Recursivo: Cómo llego a hoy usando ayer
        res = regla_matematica(calcular_valor(n - 1))
    return res
```

### 📈 Patrón B: La Acumulación (Totales)
Se usa cuando el enunciado pide el "Total hasta..." o "La suma de...". Requiere llamar a la función puntual y sumarle el acumulado.
```python
def calcular_total(n):
    res = None
    if n == 1:
        res = calcular_valor(1)
    else:
        # El total de hoy es lo de hoy + el total de ayer
        res = calcular_valor(n) + calcular_total(n - 1)
    return res
```

---

## ⚠️ Consideraciones de Performance
No todos los problemas deben ser recursivos.
- **Factorial/Suma:** Eficientes ($O(n)$).
- **Fibonacci:** Ineficiente en recursión simple ($O(2^n)$). Como tiene dos llamadas recursivas (`fib(n-1) + fib(n-2)`), recalcula lo mismo miles de veces.
  - *Conclusión:* Si el árbol de llamadas se ramifica mucho, la recursión puede ser costosa.

## 💡 Tips de Programación
- **Estado 'res':** Es buena práctica inicializar `res = None` al principio y asegurar que todos los `if/else` le asignen un valor antes del `return res` final. Esto evita errores de retorno accidental de `None`.
- **Validación de entradas:** Siempre verificar que los parámetros no sean negativos si la recursión resta (ej. `n-1`).
