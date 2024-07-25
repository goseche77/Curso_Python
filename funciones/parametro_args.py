#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([5,7,9,10,15,20,50])

print(resultado2)

#lo mismo que arriba pero utilizando el operador * como argumento *Args
def suma(nombre,*numeros):
    return(f'{nombre}, la suma de tus numeros es: {sum(numeros)}')

resultado = suma("Gustavo",5,7,9,10,15,20,50)
# print(resultado)