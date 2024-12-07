
# <center>LISTAS</center>

# | DEFINICIÓN
Una lista es una colección ordenada de elementos que pueden ser de cualquier tipo de dato (números, cadenas, objetos, etc.). En muchos lenguajes de programación, las listas son estructuras mutables, lo que significa que se pueden modificar después de su creación.

## <center>CARACTERÍSTICAS</center>

- **Ordenadas:** Los elementos en una lista mantienen un orden específico, lo que permite acceder a ellos mediante índices.
- **Indexadas:** Cada elemento tiene un índice asociado que representa su posición en la lista, comenzando generalmente desde 0.
- **Mutables:** Las listas permiten añadir, eliminar o modificar elementos después de haber sido creadas.
- **Heterogéneas:** Pueden contener elementos de diferentes tipos.
- **Capacidad Dinámica:** Las listas pueden crecer o disminuir en tamaño según sea necesario.
- **Facilidad de Iteración:** Son fáciles de recorrer mediante bucles.

## SINTAXIS

Para crear una lista en Python, se utilizan corchetes “[ ]”, y los elementos se separan por comas. Aquí tienes la sintaxis básica:

```py
lista = ["Elemento 1", "Elemento 2", "Elemento 3"]
```

## CREACIÓN DE LISTAS

Aquí hay algunos ejemplos de cómo crear listas en Python:

```py
# Lista vacía
lista_vacia = []

# Listas con varios tipos de datos
lista_mixta = [1, "Texto", 3.14, True]

# Lista anidada (lista dentro de otra lista)
lista_anidada = [[1, 2], [3, 4], [5, 6]]
```

## OPERACIONES COMUNES

1. Acceso a Elementos

Puedes acceder a los elementos de una lista utilizando índices:

```py
frutas = ["manzana", "banana", "cereza"]
print(frutas[0]) # Salida: manzana
```

2. Modificación de Elementos

Puedes cambiar el valor de un elemento específico:

```py
fritas[1] = "kiwi"
print(frutas) # Salida: ['manzana', 'kiwi', 'cereza']
```

3. Agregar Elementos

```py
frutas.append("naranja") # Agrega al final
frutas.insert(1, "mango") # Inserta en la posición 1
```

Puedes añadir elementos al final de la lista con el método **‘append()’** o insertar en una posición específica con **‘insert()’**:

4. Eliminar Elementos

Puedes eliminar elementos usando **‘remove()’** (por valor) o **‘pop()’** (por índice):

```py
frutas.remove("kiwi") # Eliminar el primer elemento que coincide con 'kiki'
print(frutas) # Salida: ['manzana', 'mango', 'cereza', 'naranja']

fruta_eliminada = frutas.pop(0) # Elimina y devuelve el primer elemento
print(fruta_eliminada) # Salida: manzana
print(frutas) # Salida: ['mango', 'cereza', 'naranja']
```

5. Recorrer una Lista

Puedes usar un bucle ‘for’ para iterar sobre los elementos de una lista:

```py
for fruta in frutas:
	print(fruta)
```

6. Longitud de la Lista

Para obtener la cantidad de elementos en una lista, utiliza la función **‘len()’**:

```py
print(len(frutas)) # Salida: 3 (dependiendo del contenido actual)
```

## EJERCICIOS

1) En este ejemplo se muestran varias operaciones con listas:

```py
# Cerar una lista de frutas
frutas = ["manzana", "banana", "cereza"]

# Agregar más frutas
frutas.append("naranja")
frutas.insert(1, "kiwi")

# Imprimir todas las frutas
print("Lista de frutas:")
for fruta in frutas:
	print(fruta)

# Modificar una fruta
frutas[0] = "pera"

# Eliminar una fruta
frutas.remove("banana")

# Imprimir la lista y su longitud
print("\nLista final de frutas:")
print(frutas)
print("Número total de frutas:", len(frutas))
```

2) Ejemplo: Gestión de una Lista de Libros

```py
# Crear una lista de libros
libros = ("1984", "El Principito", "Cien años de soledad")

# Agregar un libro
libros.append("Orgullo y prejuicio")

# Eliminar un libro
libros.remove("El Principito")

# Imprimir la lista final de libros
print("Lista de libros:")
for libro in libros:
	print(libro)
```

**Salida Esperada**

Al ejecutar el código, deberías ver:

```plain
Lista de libros:
1984
Cien años de soledad
Orgullo y prejuicio
```

