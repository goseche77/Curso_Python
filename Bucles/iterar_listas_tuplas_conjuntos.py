
animales = ["Tiburon", "pez", "gato", "perro", "loro", "cocodrilo"]
numeros = [4, 17, 30, 38, 55, 56]

# Recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')

# Prueba GO
for numero in numeros:
    print(f'Cada numero representa la edad de un familiar: {numero}')

# recorriendo la lista y multiplicando el valor por 7
for numero in numeros:
    resultado = numero * 7
    print(resultado)

#Iterar dos listas del mismo tamaño al mismo tiempo con zip()
for numero,animal in zip(numeros,animales):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')
    
# Bucle aplicado en rango de numeros, con range()
for num in range(51):
    print(num)
    
# Forma correcta de recorrer una lista con su indice 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} el valor es: {valor}')
    
# Usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual {numero}')
else:
    print('Se termino el bucle')
    
# todo lo anterior funciona exactamente igual para tuplas y conjuntos  