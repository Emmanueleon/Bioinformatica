# Data types

## Strings: Cadenas de caracteres
primer_nombre= "Emmanuel"
segundo_nombre= "Cervantes Monroy"

print("Hola"+ " "+ primer_nombre + " "+ segundo_nombre)

### Modificaciones de strings
oracion= "El nombre de mi perro es Keisy"
print(oracion.upper())  #.upper() cambia todas las letras a mayúscula
print(oracion.lower())  #.lower() cambia todas las letras a minúscula
print(oracion.capitalize()) #.capitalize() cambia todos los inicios de palabras en mayúscula
print(oracion.count("e"))  #.count() cuenta la letra asignada, p.e "e".

nombre= input("¿Cuál es tu nombre?: ")
apellido= input("¿Cuál es tu apellido?: ")
print("Hola"+" "+ nombre.capitalize()+ " "+ apellido.capitalize())

### Formatear strings
print("Hola, {} {}".format(nombre,apellido)) #.format permite darle el acomodo que deseamos
print("Hola, {1} {0}".format(nombre,apellido)) #.format permite darle el acomodo que deseamos
print(f"Hola, {apellido} {nombre}") # SOLO en python3, ponemos la función f previo a escribir el código (más sencillo)


## Integer & Float: Números

### Suma (+)
print(12+4)
### Resta (-)
print(12-4)
### Multiplicación (*)
print(12*4)
### División (/)
print(12/4)
### Exponente (**)
print(12**4)
### División entera (//)
print(12//4)
### Módulo (%)
print(12%4)


## Concatenando clases
### Números a strings 
dias=28
# print("Febrero tiene"+ dias) # Esto genera un error debido a la clase de los objetos 
print("Febrero tiene" + " " + str(dias) + " " + "días") # str() sirve para cambiar de número a string

### Strings a números
first_num = input("Enter first number: ")
second_num=input("Enter second number: ")
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))




