
# <center>TUPLAS</center>

Las tuplas son una estructura de datos fundamental en programación, especialmente en lenguajes como Python. Se caracterizan por ser inmutables, lo que significa que una vez que se crean, sus elementos no pueden ser modificados. Esta propiedad las diferencia de las listas, que son mutables. 

## | DEFINICIÓN Y CREACIÓN

Una tupla es una colección ordenada de elementos que puede contener diferentes tipos de datos. Se definen utilizando paréntesis ‘( )’ y los elementos se separan por comas. Por ejemplo:

```py
tupla = (1, "texto", 3.14)
```

Además, se pueden crear tuplas sin paréntesis, simplemente separando los elementos con comas:

```py
tupla = 1, 2, 3
```

Para crear una tupla con un solo elemento, es necesario incluir una coma después del elemento:

```py
tupla_unica = (2,)
```

## <center>CARACTERÍSTICAS</center>

1. **Inmutabilidad:** Una vez creada, no se pueden cambiar los valores de una tupla. Intentar modificarla resultará en un error ‘TypeError’.
2. **Ordenadas:** Los elementos en una tupla tienen un orden definido y se accede a ellos mediante índices, comenzando desde cero.
3. **Heterogeneidad:** Las tuplas pueden contener elementos de diferentes tipos (números, cadenas, listas, etc.)

## OPERACIONES COMUNES

**Acceso a Elementos**

Se puede acceder a los elementos de una tupla utilizando índices:

```py
print(tupla[0]) # Imprime el primer valor
```

**Empaquetado y Desempaquetado**

Las tuplas permiten agrupar múltiples valores en una sola variable (empaquetado) y también extraer esos valores en variables individuales (desempaquetado):


```py
# Empaquetado
coordenada = (3, 4)

# Desempaquetado
x, y = coordenada
```

**Métodos**

Las tuplas tienen algunos métodos incorporados:

- **count(obj):** Cuenta cuántas veces aparece un objeto en la tupla.
- **index(obj[, start]):** Devuelve el índice del primer elemento que coincide con el objeto especificado. Si no se encuentra, genera un ‘ValueError’.

## USOS COMUNES

Las tuplas son útiles en varias situaciones:

- **Retorno de Múltiples Valores:** Se utilizan frecuentemente para devolver múltiples valores desde funciones.
- **Agrupación de Datos Relacionados:** Son ideales para agrupar datos que deben permanecer juntos, como coordenadas o registros de bases de datos.
- **Eficiencia:** En general, las tuplas son más eficientes en términos de memoria y rendimiento en comparación con las listas debido a su inmutabilidad

## EJERCICIOS

**1 – Retorno de Múltiples Valores desde una Función**

Las tuplas son ideales para devolver varios valores desde una función sin necesidad de crear una estructura de datos más compleja.

```py
def calcular_area_y_perimetro(base, altura):
	area = base * altura
	perimetro = 2 * (base + altura)
	return area, perimetro # Retorna una tupla

resultado = calcular_area_y_perimetro(5, 10)
print(f'Área: {resultado[0]}, Perímetro: {resultado[1]}')
```

**2 – Almacenamiento de Registros**

Se pueden utilizar tuplas para representar registros de datos. Por ejemplo, podrías usar tuplas para almacenar información sobre un empleado.

```py
empleado = ('Juan Pérez', 30, 'Desarrollador')
# Nombre, edad, cargo
prin(f'Nombre: {empleado[0]}, Edad: {empleado[1]}, Cargo: {empleado[2]}')
```

