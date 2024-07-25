#Usando Open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("archivos\\archivo.txt",encoding="UTF-8")

#Leer archivo completo
# archivo = archivo.read()

#Leer una sola linea
linea = archivo.readline()

#Leer linea por linea
# lineas = archivo.readlines()

#Cerrar el archivo
archivo.close()

print(linea)

