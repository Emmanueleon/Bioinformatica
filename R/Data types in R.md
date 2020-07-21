# Data Types in R

En R todos los elementos que se manejen se llaman objetos y existen diferentes tipos de datos: 

* Atomic classes
* Vectors, lists
* Factors
* Missing values
* Data frames
* Names

## Atomic classes
Los objetos pueden ser de diferentes clases: 

* Character: Son letras o palabras
* Numeric: Son números enteros
* Integer: Son números con decimales
* Complex: Son números complejos como i
* Logical: Son operadores lógicos como TRUE o FALSE

Además los objetos en R pueden tener o no tener *atributtes*, algunos ejemplos son:

* names, dimnames
* dimensions (matrices)
* class
* lenght


## Vector & lists
Un vector es una fila que  pueede contener objetos, estos deben de ser de la misma clase.

La manera en que se pueden crear vectores de objetos es utilizando la función de concatenación, **`c()`**.
También se puede utilizar la función **`vector("clase de objeto", lenght=10)`**.

**Nota**: Cuando se mezclan objetos en un mismo vector ocurre la *coerción* de los objetos, de manera que todos los elementos en el vector son de la misma clase.

El usuario puede especificar esa coerción (***explicit coercion***) utilizando la función **`as.*`**, donde * es el tipo de clase al cuál quiere convertir el objeto.

Ejemplo
```{r, }
x <-  0:6
class(x)
as.numeric(x)
as.logical(x)
as.character(x)

```

No siempre es posible convertir un objeto de cierta clase a otra clase, el resultado de esta coerción resultara en NA.

```{r}
x <- c("a", "b", "c")
class(x)
as.numeric(x)
as.logical(x)
```

El único vector que puede contener diferentes objetos es *list*

```{r}
x <-list ("a", 2, 3.4, TRUE, 4i) 
class(x)
print(x)
```

## Matrix 
Las matrices son vectores con un atributo de dimensión. Posee un numero de filas y un número de columnas **`(nrow, ncol)`**.

```{r}
m <- matrix(c(2,4, 5, 18), nrow = 2, ncol = 2)
print(m)
dim(m)
attributes(m)
```

Otras formas de crear matrices son: 
1. Creando el vector y luego dandole dimensión a ese vector (debe tener la misma dimensión que el vector)
```{r}
m <-  1:10
dim(m) <- c(2,5)
print(m)
```
2. Uniendo filas **`rbind()`** o columnas **`cbind()`** (deben tener la misma dimensión que el vector)
```{r}
x <- 1:3
y <- 10:12
cbind(x,y)
rbind(x,y)
```

## Factors
Los factores son un tipo especial de vectores, son utilizados para representar cierto tipo de valores categóricos. Los factores pueden ser ordenados (p.e. ranks) o no ordenados (p.e. sexo) y se pueden crear con la función **`factor()`**. 
```{r}
x <- factor (c("blue", "yellow", "red", "green", "red", "green", "green"))
levels(x)
table(x)   # Tabla de frecuencias
unclass(x) # Da un código a cada factor
```

R asigna el orden de los factores de manera alfabética, no siempre es lo deseado de manera que lo podamos controlas con el parámetro **`levels()`** dentro de la función **`factor()`**:

```{r}
x <- factor (c("blue", "yellow", "red", "green", "red", "green", "green"), 
             levels= c("yellow", "red", "blue", "green"))
unclass(x) 
```

## Missing Values
Los NA's son valores faltantes, para poder comprobar si un objeto tiene algun valor faltante se utiliza la función **`is.na()`**, puede tener su propia clase.

```{r}
x <- c(1, 3, 1, NA, 6, NA, 89)
is.na(x)
```

## Data Frames
Los dataframes son utilizados para almacenar datos tabulares, a diferencia de las matrices, los data frames pueden almacenar diferentes clases de objetos en cada columna (como las listas), además  tienen un atributo especial llamado **`row.names`** y se pueden llamar utilizando las funciones **`read.table()`** o **`read.csv()`**, también pueden ser convertido en matriz utilizando el parámetro **`data.matrix()`**, sin embargo esto coercionará la clase de objetos que se encuentran en la tabla. 

```{r}
x <- data.frame(Número=1:4, Valor=c(TRUE, FALSE, TRUE, FALSE))
x
nrow(x)
ncol(x)
class(x)
class(x$Número)
class(x$Valor)
```

## Names 
Los objetos en R pueden tener nombres, algo muy útil cuando se esta creando código. 
```{r}
x <- 1:5
names(x)
names(x) <- c("Número", "Asignación", "ID", "Medición", "Atributo")
x
```
