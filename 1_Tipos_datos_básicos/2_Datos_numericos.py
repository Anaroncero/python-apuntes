# Funciones predefinidas que trabajan con números:-------------
# Funciones predefinidas
print(abs(-7))    #valor absoluto           # Salida: 7
print(divmod(7, 2))  #cociente y resto      # Salida: (3, 1)
print(hex(255))         #hexadecimal        # Salida: '0xff'
print(pow(2, 3))         #potencia          # Salida: 8
print(round(7.567, 1))     #redondea        # Salida: 7.6
print(" ")   

# Conversión de tipos----------------------------
a = int(7.2)
print(a)                           # Salida: 7
print(type(a))                     # Salida: int
print(" ")   

a = int("345")
print(a)                           # Salida: 345
print(type(a))                     # Salida: int
print(" ")   

b = float(1)
print(b)                           # Salida: 1.0
print(type(b))                     # Salida: float
print(" ")   

b = float("1.234")
print(b)                           # Salida: 1.234
print(type(b))                     # Salida: float
print(" ")   

# Intento de conversión inválido
try:
    a = int("123.3")              # Esto generará un error
except ValueError as e:
    print(e)                      
print(" ")   


# Otras operaciones con el módulo math---------------------
import math

# Raíz cuadrada
resultado = math.sqrt(9)
print(resultado)                  # Salida: 3.0
print(" ")   

# Otras funciones del módulo math
print(math.pi)                    # Salida: 3.141592653589793
print(math.factorial(5))          # Salida: 120 (5!)


