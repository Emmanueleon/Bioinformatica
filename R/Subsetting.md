# Subsetting 

## Basics
En R una de las funciones básicas es la exploración de los datos, esto se puede realizar mediante operadores que pueden ser utilizados para extraer subconjuntos de datos de los objetos, entre ellos se encuentran:

* [], siempre regresa un objeto de la misma clase que el original
```{r}
x <- c("a", "b", "c", "d")
x[2]
x[2:4]
```
Con esto también se pueden utilizar símbolos aritméticos:
```{r}
x <- c("a", "b", "c", "d")
x[x>"a"]
x[x=="c"]
x[x!="d"]
```
y lógicos:

```{r}
x <- c("a", "b", "c", "d")
u <- x > "a"
e <- x=="b"
u
e
```

## List
Para poder extraer listas se pueden utilizar los siguientes elementos:

* [[]], extrae elementos de una lista o de un data frame.
* $ se utiliza para extaer elementos de una lista o de un data frame por el nombre.

```{r}
x <- list(foo=1:4, bar=0.6, baz="hello") # dos elementos en la lista 
name <- "foo"

x[1]    # Utilizando el corchete simple, solo extraígo el primer elemento que es la lista 

x[[name]]  # Se utiliza para extraer elementos de diferentes clases utilizando índices

x$bar   # Utilizando el $ puedo específicar que lista es la que requiero

x[c(1, 3)]  # Sirve para extraer múltiples listas

```

### Listas anidadas
El doble corchete puede tomar una secuencia entera
```{r}
x <- list(a=list(10,12,14), b=c(3.14, 2.81))

x[[c(1,3)]]  # Busco del elemento 1(lista a), el dato 3 

x[[c(2, 1)]] # Busca el elemento 2 (lista b), el dato 1

```

## Matrices
También se puede realizar un *subsetting* de las matrices de la mima manera convencional (i,j), donde i es el renglón y j la columna. En las matrices se puede dejar un espacio para que el subsetting sea o toda la fila o toda la columna
```{r}
x <- matrix(1:6, 2,3)
x[1,2]  # De la fila 1 el elemento 2
```
En las matrices se puede dejar un espacio para que el subsetting sea o toda la fila o toda la columna

```{r}
y <- x[1,] # Muestra toda la fila 1
print(y)
is.matrix(y)
z <- x[,2, drop=FALSE] # Muestra todo el renglón 2
print(z)
is.matrix(z)

x[1,]
x[1, ,drop=FALSE]
```
**Nota**: Por default cuando R arroja el resultado del elemento de la matriz lo devuelve como un vector de longitud 1 y no como una matriz 1x1. Para poder solucionar esto se puede utilizar el parámetro **`drop=FALSE`**.

## Names
También se puede realizar un subsetting de nombres utilizando **`[[]]`** o **`$`**. El objetivo de este subsetting es aminorar el tiempo en buscar los objetos, utilizando simplemente la palabra. 
De manera que el resultado se vea en la línea de comando. 
```{r}
x <- list(aardvark=1:5, beast=0.6, beat=1)
x$a
x[["a"]]
x[["a", exact=FALSE]]
x[["beast", exact=FALSE]]
```
**Nota**: Para poder utilizar el doble corchete es necesario utilizar el parámetro **`exact=FALSE`**. 

## Removing missing values (NA)
Quitar los NA's es una operación muy común, sobre todo cuando se tienen datos reales. Para poder solventar los NA's:

1. Se crea un vector **lógico** para poder localizarlos con la función **`is.na()``**.
2. Pedimos a R que haga un subsetting del objeto x mostrando todos los datos diferentes al objeto **`bad`**.

```{r}
x <- c(1, 2, 3, NA, 5, NA, 7)
bad <- is.na(x)
print(bad)
x[!bad] 
```

* Se puede realizar para múltiples vectores utilizando la función **`complete.cases()`**. 
```{r}
x <- c(1, 2, 3, NA, 5, NA, 7)
y <- c("a", "b", NA, "d", "e", NA, NA)

good <- complete.cases(x,y)  
x[good]
y[good]

```
**Nota**: Los objetos deben de tener la misma longitud

* Para utilizarlo en data frames
```{r}
airquality[1:6,]
good <- complete.cases(airquality)
airquality[good,][1:6,]

```
