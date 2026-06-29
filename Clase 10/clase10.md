# LinkedList - Estructuras dinámicas

- No dinamica
  - Especifica al compilar cuanta memoria reserva para coleccionar objetos
- Dinamica
  - El espacio que ocupa en memoria cambia dinamicamente en tiempo de ejecucion
  - Los elementos no pueden ocupar memoria contigua
  - Estan dispersos en la memoria pero mantienen su orden
### Solucion

- Estructura de nodos unidos con referencias (punteros) uno a continuacion del otro
  - Se guarda el dato, y la referencia hacia el próximo nodo

### Estructuras lineales (1 previo y 1 siguiente)
- Listas
  - Solo sabe donde esta el primer nodo.
- Pilas
- Colas
### No lineales (>= 1 previos y >= 1 siguientes)
- Árboles
- Grafos


### Operaciones

- Crear
- Obtener elemento de una posición
- Tamaño
- EstaVacia
- InsertarDato
  - Al final
  - En una posicion

#### Recorridos escenciales
- Recorrer
  - Hasta el final
    - Creo variable aux 
    - La voy corriendo al proximo desde el primero hasta el ultimo (nodo.siguiente == None)
    - NO modificar el primer nodo de la lista
  - Hasta posicion determinada

### Notas de la clase
Visitar -> aux = Nodo

