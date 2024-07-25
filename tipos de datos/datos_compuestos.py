# Creando una lista (se puede modificar)
lista = ["Gustavo Oseche", "goseche", True,1.78 ]

# Creando una lista (no se puede modificar)
tupla = ("Gustavo Oseche", "goseche", True,1.78)

# esto es valido
# lista[3] = "Maquina"

# esto no es valido
# tupla[3] = "Maquina"

# print(lista[3])

# creando un conjunto (set) (no se accede a elementos por su indice, no alamacena datos duplicados, muestra la informacion de forma desordenada)

conjunto = {"Gustavo Oseche","goseche",True,1.78}

#print(conjunto[3]) -> no puede acceder al elemento

# print(conjunto)

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    
    'nombre' : "Gustavo Oseche",
    'canal' : "goseche",
    'esta_emocionado' : True,
    'altura' : 1.78,
    'dato_duplicado' : "Gustavo Oseche"
    
}

print(diccionario['altura'])
print(lista[2])