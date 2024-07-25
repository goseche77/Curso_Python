
cadena1 = "Hola,soy,Gustavo"
cadena2 = "Bienvenido,al,servicio,de,TI"

# Dato . Nombre del Metodo y los parentesis

# Convierte a Mayusculas
resultado = cadena1.upper()

# Convierte a Minusculas
resultado1 = cadena1.lower()

# 1era Letra en Mayusculat
resultado2 = cadena1.capitalize()

# Buscamos una cadena en otra cadena / Si devuelve el valor -1 es porque no hay coincidencias
resultado3 = cadena1.find("T")

# Buscamos una cadena en otra cadena / Si no hay coincidencias no arroja una excepcion
resultado4 = cadena2.index("T")

# Si es numerico devolvemos True, sino devolvemos False
resultado5 = cadena1.isnumeric()

# Si es alfanumerico devolvemos True, sino devolvemos False. PAra que la busqueda sea efectiva no debe haber espacios.
resultado6 = cadena1.isalpha()

# # Contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias 
resultado7 = cadena1.count("t")

# Contamos cuantos caracteres tiene una cadena / Len no es metodo es una funcion, por lo tanto primero va la funcion y luego el Dato
resultado8 = len(cadena1)

# Verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
resultado9 = cadena1.startswith("H")

# Verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
resultado10 = cadena2.endswith("o")

# Reemplaza un pedazo de la cadena dada, por otra dada, es decir, si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2.
resultado11 = cadena1.replace("Hola" , "Hola, llegaste?")

# Separar cadenas con la cadena que le pasemos 
resultado12 = cadena1.split(",")

print(resultado12 [2])