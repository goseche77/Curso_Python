numeros = [1,4,1,7,30,38,55]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
# print(numero_mas_alto)

# #encontrando el numero menor de una lista
numero_mas_bajo = min(numeros)
# print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.3456789,4)

#retorna False -> 0, vacio, False, none \ True -> distinto a 0, True, cadena, datos no vacios
resultado_bool = bool(-1)

#retorna True si todos los valores son verdaderos
resultado_all = all([123, 'true', [344,25]])

#Suma todo los valores de un iterable
suma_total = sum(numeros) 

print(suma_total)