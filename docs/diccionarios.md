
# <center>DICCIONARIOS</center>

Los diccionarios son una estructura de datos fundamental en Python, utilizados para almacenar colecciones de datos en pares de clave y valor. Esta estructura permite acceder a los valores de manera eficiente utilizando las claves, lo que los hace muy útiles para organizar y manejar datos complejos.


## | DEFINICIÓN Y SINTAXIS

Un diccionario en Python se define utilizando llaves ‘{}’ y consiste en pares de clave y valor separados por comas. La sintaxis básica es la siguiente:

```py
mi_diccionario = {
	'clave1': 'valor1',
	'clave2': 'valor2',
	'clave3': 'valor3'
}
```

**Ejemplo:**

```py
estudiante = {
	'nombre': 'Juan',
	'edad': 20,
	'carrera': 'Ingeniería'
}
```

En este ejemplo, ‘nombre’, ‘edad’ y ‘carrera’ son las claves, mientras que ‘Juan’, ‘20’ e ‘Ingeniería’ son los valores correspondientes.

## <center>CARACTERÍSTICAS DE LOS DICCIONARIOS</center>

- **Mutables:** Puedes modificar los valores de un diccionario después de su creación.
- **Desordenados:** A partir de Python 3.7, los diccionarios mantienen el orden de inserción, pero no están diseñados para ser ordenados como listas.
- **Claves Únicas:** Cada clave en un diccionario debe ser única; si se asigna un nuevo valor a una clave existente, el valor anterior se sobrescribirá.

## OPERACIONES COMUNES

1. Acceso a Valores

Puedes acceder a un valor utilizando su clave:

```py
print(estudiante['nombre']) # Salida: Juan
```

También puedes usar el método **‘get()’** para evitar errores si la clave no existe:

```py
print(estudiante.get('edad')) # Salida: 20
```

2. Modificación de Valores

Para modificar el valor asociado a una clave, simplemente asigna un nuevo valor:

```py
estudiante['edad'] = 21
```

3. Agregar Nuevas Claves y Valores

Puedes añadir nuevos pares clave-valor de la siguiente manera:

```py
estudiante['promedio'] = 8.5
```

4. Eliminar Claves

Para eliminar una clave y su valor asociado, utiliza **‘del’** o el método **‘pop()’**:

```py
del estudiante['carrera']
# o
promedio = estudiante.pop('promedio')
```

5. Iterar sobre un Diccionario

Puedes recorrer un diccionario utilizando un bucle **‘for’**:

```py
form clave, valor in estudiante.items():
	print(f"{clave}: {valor}")
```

## EJERCICIOS

1. Este es un ejemplo completo que muestra cómo crear un diccionario, modificarlo y recorrerlo:

```py
# Crear un diccionario de estudiante
estudiante = {
	'nombre': 'Juan',
	'edad': 20,
	'carrera': 'Ingeniería'
}

# Acceder a valores
print(estudiante['nombre']) # Salida: Juan

# Modificar la edad
estudiante['edad'] = 21

# Agregar promedio
estudiante['promedio'] = 8.5

# Eliminar carrera
del estudiante['carrera']

# Imprimir el diccionario final
print("Información del estudiante:")
for clave, valor in estudiante.items():
	print(f"{clave}: {valor}")
```

**Salida Esperada**

Al ejecutar el código anterior, deberías ver:

```plain
Juan
Información del estudiante:
nombre: Juan
edad: 21
promedio: 8.5
```

**Gestión de Contactos:** Este ejemplo incluye la creación del diccionario, la adición de nuevos contactos, la modificación de un número de teléfono y la impresión de todos los contactos.

```py
# Crear un diccionario de contactos
contactos = {
	"Juan": "123-456-7890",
	"Ana": "987-654-3210",
	"Luis": "555-123-4567"
}

# Agregar un nuevo contacto
contactos["Carlos"] = "444-555-6666"

# Modificar el número de teléfono de Ana
contactos["Ana"] = "111-222-3333"

# Imprimir todos los contactos
print("Lista de contactos:")
for nombre, telefono, in contactos.items():
	print(f"{nombre}: {telefono}")
```

**Salida Esperada**

Al ejecutar el código, deberías ver:

```plain
lista de contactos:
Juan: 123-456-7890
Ana: 111-222-3333
Luis: 555-123-4567
Carlos: 444-555-6666
```

