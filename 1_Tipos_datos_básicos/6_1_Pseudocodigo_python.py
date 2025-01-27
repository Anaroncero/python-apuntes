
'''
En pseudocódigo:

Definir nombre Como Cadena;
Escribir "Dime tu nombre:";
Leer nombre;
'''
nombre = input("Dime tu nombre: ")




'''
Leer números enteros
En pseudocódigo:

Definir numero Como Entero;
Escribir "Dime un número entero:";
Leer numero;
'''
numero = int(input("Dime un numero entero: "))




'''
Leer números reales
En pseudocódigo:

Definir numero Como Real;
Escribir "Dime un número real:";
Leer numero;
'''
numero = float(input("Dime un número real: "))




'''
Escribir una variable en pantalla
En pseudocódigo:

Escribir "Hola ",nombre;
'''
print("Hola " + nombre)




'''
Escribir sin saltar a otra línea
En pseudocódigo:

Escribir Sin Saltar var," ";
'''
var = "ana"
print(var, " ", end="")




'''
Asignar valor a una variable
En pseudocódigo:

numero <- 7;
'''
numero = 7




'''
Por ejemplo para incrementar el valor de una variable, 
en pseudocódigo:

num <- num + 1
'''
num = 2
num = num + 1
# O así:
num += 1




'''
Calcular la parte entera de una división
En pseudocódigo:

trunc(7/2)
'''
resultado = 7 // 2




'''
Calcular la raíz cuadrada
En pseudocódigo:

raiz(9)
'''
import math
resultado = math.sqrt(9)




'''
Obtener el carácter de una cadena
En pseudocódigo:

subcadena(cadena,0,0)
'''
cadena = "ana"
caracter = cadena[0]




'''
Unir dos cadenas de caracteres

'''
cadena1 = "hola "
cadena2 = "caracola"
cadena3 = cadena1 + cadena2




'''
Convertir una cadena a Mayúsculas
Lo veremos con detenimiento en las próximas unidades, pero vamos a usar el método de cadena upper:
'''
cadena = cadena.upper()

