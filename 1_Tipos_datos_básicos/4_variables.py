#Creación de una variable------------------
var = 5 
print(var)          #Imprime: 5
print(type(var))    #Imprime: #int

# Cambiando el tipo de variable
var = "hola"
print(var)  # Imprime: hola
print(type(var))  # Imprime: str

# Borrado de variables
a = 5
print(a)

# Borrar la variable a
del a

# Intentar acceder a la variable a despues de borrarla
try: 
    print(a)
except NameError as e:
    print(e)



# Modificacion de una variable--------------------
a = 5
print(a)  # Imprime: 5

# Cambiando el valor de 'a'
a = 8
print(a)  # Imprime: 8

# Incrementando el valor de 'a'
a = a + 1
print(a)  # Imprime: 9

# Usando un operador de asignación
a += 1
print(a)  # Imprime: 10

# Otros operadores de asignación-----------------------
b = 10

# Usando diferentes operadores de asignación
b -= 2  # b = b - 2
print(b)  # Imprime: 8

b *= 3  # b = b * 3
print(b)  # Imprime: 24

b /= 4  # b = b / 4
print(b)  # Imprime: 6.0

b %= 5  # b = b % 5
print(b)  # Imprime: 1.0

b **= 2  # b = b ** 2
print(b)  # Imprime: 1.0

b //= 1  # b = b // 1
print(b)  # Imprime: 1.0