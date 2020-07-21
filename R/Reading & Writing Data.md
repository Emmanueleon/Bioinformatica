# Reading & Writing Data

Una de las principales funcionalidades de R es la **importación** de datos con los que querramos trabajar o evaluar para distintos fines. Para ello R cuenta con diferentes tipos de comandos para realizar la importación de los datos al entorno de R, a continuación se mencionan algunos de ellos: 

* **`read.table(), read.csv()`**: Estas funciones nos ayudan a importar o leer datos tabulares. 
* **`readLines`**: Esta función permite leer lineas de un archivo de texto. 
* **`source()`**: Permite la lectura de archivos de código de R. 
* **`dget()`**: Sirve para leer archivos de R que hayan sido analizadas en archivos de texto.  
* **`load()`**: Permite la lectura de espacios de trabajo guardados. 
* **`unserialize()`**: Sirve para leer objetos de R sencillos de manera binaria. 

De manera inversa nosotros también podemos realizar la **exportación** de los datos con las siguientes funciones que son análogas a las funciones previas. 

* **`write.table(), write.csv()`**: Estas funciones nos ayudan a exportar datos tabulares. 
* **`writeLines`**: Esta función permite importar lineas a un archivo de texto. 
* **`dump()`**: Permite guardar archivos de código de R. 
* **`dput()`**: Sirve para guardar archivos de R que hayan sido analizadas en archivos de texto.  
* **`save()`**: Permiteguardar espacios de trabajo. 
* **`serialize()`**: Sirve para guardar objetos de R sencillos de manera binaria. 

## Reading Data Files
Una de las funciones más utilizadas en R es la función **`read.table`**, utilizada para la lectura de tablas de datos.Algunos de los argumentos más importantes de la función son:

* `file=""`, es el nombre y la ruta donde se encuentra el archivo.
* `header=TRUE o FALSE`, indica si el archivo tiene una línea de encabezado. 
* `sep=""`, indica como se encuentran separadas las columnas, pueden ser por espacios (read. table), comas (read.csv), semicomas.
* `colClasses`, un vector de tipo caracter que indica la clase de cada columna en el dataset. 
* `nrows=`, el número de filas en el dataset. 
* `comment.char=`, un caracter string que indica el caracter de comentario. 
* `skip=`, indica el número de líneas a saltarse desde el principio.
* `stringAsFactors`, ¿las variables de clase caracter deben ser codificadas como de clase factor?. 


## Memory Requirements
Para poder valorar si el equipo es capaz de trabajar con tablas con gran cantidad de datos se puede realizar el siguiente ejercicio:


```{r}
x <- 1500000 # Número de filas
y <- 120     # Número de columnas

bytes <- x*y* 8 # 8 bytes/numeric
print(bytes)
MB <- bytes/2**20 # 2^20 bytes/MB
GB <- MB/1000
paste(GB, "Gigabytes")
```
