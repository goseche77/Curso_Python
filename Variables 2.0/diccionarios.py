# Creando diccionarios con dict()
diccionario = dict(nombre="Gustavo",apellido="Oseche")

# LAs listas no pueden ser claves y usamos frozenset para ingresar conjuntos
diccionario = {frozenset(["Oseche","rancio"]): "Muy bien"}

# Creando diccionarios con FromKeys
diccionario = dict.fromkeys(["nombre","apellido","sueldo"])

print(diccionario["apellido"])