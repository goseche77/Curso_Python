#Ejercicio 2
# a) Pedirle al usuario que diga cualquier texto real y:
# - Calcular cuanto tardaria en decir esa frase
# - Cuantas palabras dijo?

# b) Si se tarda mas de 1 minuto:
# - decirle "Detente, no es necesario colocar algo tan extenso"

# c) Dalto habla un 30% mas rapido: cuanto tardaria en decirlo?

frase = input("Dime una frase y te calculo cuanto tardarias si tuvieras que decirla ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo') 
print(f'Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos')
if cantidad_de_palabras > 120:
    print('Detente, no es necesario escribir tanto') 
