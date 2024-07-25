#Abrimos el archivo con with open
with open("archivos\\archivo.txt", encoding = "UTF-8") as archivo:

    #Leemos el archivo
    contenido = archivo.read()
    
    #Mostrando el archivo
    print(contenido)
    
