
diccionario = {
    "nombre" : "Gustavo",
    "apellido" : "Oseche",
    "sueldo" : 500
    
}

#recorriendo diccionario con items() para obtener las claves
for key in diccionario.items():
    key
    print(f'la clave es: {key}')

#recorriendo diccionario con items() para obtener la clave y el valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f'la clave es: {key} el valor es: {value}')
    
    