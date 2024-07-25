# Creando una lista con list()
lista = list([38,30,4,True])

# devuelve la cantidad de elementos de la lista
resultado = len(lista)

# Agregando un elemento a la lista / solo se trabaja con la lista
resultado2 = lista.append(2)

# Agregando un elemento a la lista en un indice especifico
lista.insert(0,2040)

# Agregando varios elementos a la lista. Es necesario colocarle corchetes
lista.extend([30])

#Eliminando un elemento de la lista por su indice 
#-1 para eliminar el ultimo, -2 para el penultimo, y asi sucesivamente
lista.pop() 

# removiendo un elemento de la lista por su valor 
lista.remove(True)

#Eliminando todos los elementos de la lista
#lista.clear()

# Ordenando la lista de forma ascendente (si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#Invirtiendo los elementos de una lista
lista.reverse()

#verificamos si un elemento esta en la lista
elemento_encontrado = lista.index(4)

print(resultado2)

