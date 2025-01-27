# Tipo booleano en Python
# Dos valores: True, False


# False----------
'''
-Cualquier número igual a 0
-Cualquier secuencia vacia (lista, tupla o cadena)
-Cualquier diccionario vacio
'''


# Ejemplo con operadores de comparación
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a <= b)  # True
print(a >= b)  # False


# Operadores Booleanos
x = True
y = False

# Usando OR
resultado_or = x or y #verdadero o falso = verdadero
print(resultado_or)  # True

# Usando AND
resultado_and = x and y #verdadero y falso = falso
print(resultado_and)  # False

# Usando NOT
resultado_not = not x #no verdadero = falso
print(resultado_not)  # False


# Booleanos en estructuras de control
edad = 18

if edad >= 18:
    print("Tienes la mayoria de edad")
else:
    print("Eres menor de edad")