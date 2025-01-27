# Leer y mostrar información por consola

# 1.Función Input: permite leer información por consola
nombre = input("Nombre: ")
print(nombre)

# Leer una edad 
edad = int(input("Edad: ")) #Pedir edad
print(edad) #Mostrar edad por consola



# 2.Función Print: mostrar información por consola
print(1, 2, 3) # Imprime: 1 2 3
print("Esto es una cadena") # Imprime: Esto es una cadena
print("Hola son las " + 6 + " de la tarde") #Concatenación


# 3.Formateando Cadenas de Caracteres
'''Podemos formatear cadenas utilizando 
%'''

print("%d %f %s" % (2, 2.5, "texto"))  # Imprime: 2 2.500000 texto

print("El producto %s cantidad=%d precio=%.2f" % ("cesta", 23, 13.456))  
# Imprime: El producto cesta cantidad=23 precio=13.46



# 4.Uso de f-strings para Formateo
producto = "cesta"
cantidad = 23
precio = 13.456

print(f"El producto {producto} cantidad={cantidad} precio={precio:.2f}")  
# Imprime: El producto cesta cantidad=23 precio=13.46
