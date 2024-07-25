diccionario = {
    "nombre" : 'Gustavo',
    "apellido" : 'Oseche',
    "Subs" : 200

}

# Keys devuelve las claves y sirve tambien para iterar
claves1 = diccionario.keys()

# obteniendo un elemento get() (si no encuentra nada el programa continua) arroja "none" en vez de una excepcion    
claves2 = diccionario.get('nombre')

# Elimina todos los elementos del diccionario
# claves3 = diccionario.clear()

# Eliminando un elemento del diccionario
diccionario.pop("apellido")

# Obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)
