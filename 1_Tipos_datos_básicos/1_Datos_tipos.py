# Literales:-------------------------------
# Literales numéricos
# Enteros
entero1 = 3
entero2 = -23

# Reales
real1 = 12.3
real2 = 45.6
real3 = 10.0
real4 = .001

print(entero1, " ",entero2, " ",real1," ", real2, " ",real3, " ",real4)



# Literales cadenas:-------------------------------
# Cadenas simples
cadena1 = 'Hola!'
cadena2 = "Muy bien"
# Cadenas multilínea
cadena3 = '''Podemos \n
ir al cine'''

print(cadena1)
print(cadena2)
print(cadena3)



# Variables:-------------------------------
var = 5
print(var)

nombre = "Ana"
edad = 23
es_estudiante = True

print(nombre, " ", edad, " ",es_estudiante)



# Expresiones:-------------------------------
a = 5
b = 10

resultado1 = a + 7 
resultado2 = (a**2) + b
print(resultado1) 
print(resultado2)



# Operadores:-------------------------------
# Operadores Aritméticos
suma = 5 + 3
resta = 10 - 2
multiplicacion = 4 * 2
division = 2 / 2
divisionEntera = 9 // 2
resto = 7 % 3
potencia = 2 ** 3

print(suma, " ", resta, " ", multiplicacion," ",  division, " ", divisionEntera," ",  resto, " ", potencia)
    
# Operadores de comparación
print(5 == 5)   #true
print(5 != 3)   #true
print(5 < 3)    # Falso
print(5 >= 5)   # Verdadero
print(5 <= 3)   # Falso

# Operadores Lógicos
a = True
b = False

print(a and b)  # Falso
print(a or b)   # Verdadero
print(not a)    # Falso



# Tipos de datos:-------------------------------
# Tipos numéricos
entero = 5
real = 5.5

# Tipos booleanos
booleano = True

# Tipo lista
lista = [1, 2, 3]


# Tipo tupla
tupla = (1, 2, 3)

# Tipo cadena
cadena = "Hola"

# Tipo diccionario
diccionario = {"clave": "valor"}

# Usando la función type()
# Saber el tipo de una variable
print(type(entero))      # <class 'int'>
print(type(real))        # <class 'float'>
print(type(cadena))      # <class 'str'>
print(type(lista))       # <class 'list'>
print(type(tupla))       # <class 'tuple'>
print(type(diccionario))  # <class 'dict'>

