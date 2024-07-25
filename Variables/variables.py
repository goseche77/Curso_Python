# Definiendo una variable

nombre = "Gustavo"

# Definiendo una variable con camelcase / no se recomienda

nombreCompleto = "Gustavo Oseche"

# Definiendo una variable con snake_case

nombre_completo = "Gustavo Oseche"

# Concatenar con +

nombre = "Gustavo"
bienvenido = "Hola " + nombre + " Como estas?"

# print(bienvenido)


# Concatenar f-strings - delante del dato

nombre = "mario"
bienvenido = f"Hola  {nombre}  Como estas?"

# print(bienvenido)

# Eliminar con del #

nombre = "mario"
bienvenido = f"Hola  {nombre}  Como estas?"
del bienvenido

# print(bienvenido)

# Operadores de pertenencia (in y not in)#

nombre = "Gustavo"
bienvenido = f"Hola  {nombre}  Como estas?"

print("Gustavo" in bienvenido) #True
print("Gustavo" not in bienvenido) #false