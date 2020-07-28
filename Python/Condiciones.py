# Condiciones
## if : si , else: entonces
price=float(input("Costo del producto: "))
if price >= 1.00:
    tax=0.07
    print("Impuesto de"+ " "+ str(tax))
else: 
    tax=0
    print("No hay impuesto")

### Si el print es el mismo, se puede quitar de la identación:
if price >= 1.00:
    tax=0.07

else: 
    tax=0
print(tax)

### Cuidado comparando strings
mexicano=input("¿Eres mexicano? ")
if mexicano.lower()== "si":
    print("Oh mira un mexicano")
else: 
    lugar=input("Oh, ¿De dónde eres? ")
    print("Bienvenido a México")


## elif: sino múltiples caminos
providencia=input("¿De qué estado nos visitas?: ")
if providencia.lower()=="mexico":
   tax= 0.5
elif providencia.lower()== "cdmx": 
   tax= 0.5
elif providencia.lower()== "monterrey":
    tax=0.13
else: 
    tax=0.15
print(tax)


## or: o, condiciones similares (Una condición o abas se cumplen)
providencia=input("¿De qué estado nos visitas?: ")
if providencia.lower()=="mexico" or providencia.lower()== "cdmx": 
    tax= 0.5
elif providencia.lower()== "monterrey":
    tax=0.13
else: 
    tax=0.15
print(tax)

## in :  dentro de una lista, sirve para no poner demasiados or
providencia=input("¿De qué estado nos visitas?: ")
if providencia.lower() in("mexico", "cdmx", 
                           "hidalgo", "tlaxcala"):
    tax= 0.5
elif providencia.lower()== "monterrey":
    tax=0.13
else: 
    tax=0.15
print(tax)

## Condiciones anidadas
pais=input("¿De qué país nos visitas?: ")
if pais.lower()=="mexico" or pais.lower()== "méxico":
    providencia=input("¿De qué providencia nos visitas?:")

    if providencia.lower() in("mexico", "cdmx", 
                              "hidalgo", "tlaxcala"):
        tax= 0.5
    elif providencia.lower()== "monterrey" or providencia.lower()=="mty":
        tax=0.13
    else: 
        tax=0.15
else:
    tax=0.0
print(tax)


## AND, se deben de cumplir ambas condiciones, evita repetir tantas condiciones anidadas de if;
grade=float(input("Digite su calificación: "))
if grade >= .85:
    lowest_grade= float(input("¿Cuál fue tu calificación más baja?:"))
    
    if lowest_grade >= .70:
        print("Buen trabajo!")

else: 
    print("Sigue esforzandote")


grade=float(input("Digite su calificación: "))
if grade >= .85 and lowest_grade >= .70:
    print("Buen trabajo")

### Tanto or como AND son operadores que me permiten recordar los resultados de condición 
### para posteriores pasos en mi código, para ello se utilizan operadores booleanos (TRUE, FALSE)
grade=float(input("Digite su calificación: "))
if grade >= .85 and lowest_grade >= .70:
    cuadro_honor=True
else:
    cuadro_honor=False

# En algún lugar posterior en mi código 
if cuadro_honor:
    print("Felicidades")
