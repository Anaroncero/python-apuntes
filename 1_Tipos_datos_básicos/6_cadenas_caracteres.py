# 3.Formateando Cadenas de Caracteres----------------
'''Podemos formatear cadenas utilizando 
%'''

print("%d %f %s" % (2, 2.5, "texto"))  # Imprime: 2 2.500000 texto

print("El producto %s cantidad=%d precio=%.2f" % ("cesta", 23, 13.456))  
# Imprime: El producto cesta cantidad=23 precio=13.46


# 4.Uso de f-strings para Formateo---------------
producto = "cesta"
cantidad = 23
precio = 13.456

print(f"El producto {producto} cantidad={cantidad} precio={precio:.2f}")  
# Imprime: El producto cesta cantidad=23 precio=13.46


# Definición de cadenas-------------------
cad1 = "Hola"
cad2 = '¿Qué tal?'
cad3 = '''Hola,
    que tal?'''

print(cad1)  # Imprime: Hola
print(cad2)  # Imprime: ¿Qué tal?
print(cad3)  # Imprime: Hola, que tal?

# Operaciones básicas con cadenas--------------------
# Concatenancion Cadenas
resultado_concatenacion = "hola " + "que tal"
print(resultado_concatenacion)  # Imprime: hola que tal

# Repetición de cadenas
resultado_repeticion = "abc" * 3
print(resultado_repeticion)  # Imprime: abcabcabc

# Indexación
cadena = "josé"
print(cadena[0])  # Imprime: j
print(cadena[3])  # Imprime: é

# Longitud de una cadena
longitud = len(cadena)
print(longitud)  # Imprime: 4


# Comparación de cadenas----------------
print("a" > "A")  # Imprime: True
print("informatica" > "informacion")  # Imprime: True
print("abcde" > "abcdef")  # Imprime: False
