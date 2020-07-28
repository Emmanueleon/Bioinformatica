# Colecciones

## Listas
### Asignamos posiciones a los valores con []
names=["Brenda", "Leandro", "Luis", "Ivonne"]
scores=[]    #Pueden ser listas vacías
print(names)
print(scores)


### Operaciones que se pueden realizar en listas

names.append("Emmanuel")   # .append() permite añadir un elemento a la lista, solo UN elemento, seguido del último valor
names.insert(4, "Manuel")  # .insert() permite añadir un elemento a la lista en la posición seleccionada
names.sort()               # .sort() ordena la lista 
print(len(names))          # len() permite obtener el número de datos en la lista
print(names)

### Más operaciones que se pueden realizar en 
names.extend("Beatriz")    # .extend añade una secuencia de datos al final 
names.remove("Emmanuel")   # .remove() elimina el dato 
names.reverse()            # .reverse() ordena la lista de manera inversa 
scores.clear()             # .clear borra la lista
print(names)
print(scores)

### Subsetting

un_nombre=names[7]   # Subsetting de la posición 0 en la lista name
print(un_nombre)

tres_nombres=names[9:12]  # La última posición no la cuenta, es decir la posición 12 no la cuenta
print(tres_nombres)


### Conjuntando con condiciones
nombre=input("Inserta tu nombre: ")
if nombre in names:                     #Puedo declarar la lista previamente, no necesito poner la lista aquí
    print("Si esta tu nombre")
else: 
    print("No esta tu nombre")

## Arreglos
from array import array   # Esto permite la creación del arreglo 
scores=array("d")   # en este arreglo se pondrán valores de tipo decimal (double, "d")
scores.append(98)  
scores.append(100)
print(scores)   # esto me dará las características de mi elemento, un arreglo de decimales con tales valores


## Diferencias entre arreglos y listas 
### Los arreglos solo guardan tipos de datos simples como números, todos deben de ser del mismo tipo (como los vectores en R).
### Las listas almacenan cualquier cosa,cualquier tipo de dato (similar a R). 

## Diccionarios
### Asignamos claves a valores con {}
# Primera forma
persona1= {"primera": "Brenda"}  # primero la clave : y el elemento del diccionario
persona1["last"]="Vargas"        # es la forma de añadir al último elemento otro elemento más (como .append en listas)
print(persona1)
print(persona1["primera"])       # Subsetting de la clave

# Segunda forma
persona2={"nombre": "Emmanuel", "apellido": "Cervantes"}
print(persona2)
print(persona2["apellido"])


## Diferencias entre diccionarios y listas 
### Los  diccionarios guardan pares (clave/valor), el orden no está garantizado. Se utiliza {}
### Las listas inician en cero y el orden está garantizado. Se utiliza []


## Listas con diccionarios
personas= [persona1, persona2]
print(personas)

#### Subsetting
print(personas[1])  # Busca la posición 1 del diccionario 
print(personas[1]["apellido"])  # Del diccionario en la posición 1 busca el apellido

## Más colecciones 

### Tuples 
# Una vez creados no se pueden cambiar (son inmutables).
# Son útiles cuando no se quiere modificar o agregar o eliminar datos
calificaciones= ("Cero", 1, 2, "3")


### Sets
# Son como diccionarios, no tienen un orden pero a diferencia del diccionario tampoco tienen tienen una clave
empty_set=set()  # set vacío
new_set={"Mónica", "Berenice", "Eduardo"}

