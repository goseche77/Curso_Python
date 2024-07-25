
frutas = ["cambur", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = 'Hola Gustavo'
numeros = [2, 5, 7, 9, 10, 12, 15, 21]

# Evitando que se coma una ciruela con la sentencia continue
for fruta in frutas:
    if fruta == "ciruela":
        continue
    print(f"me voy a comer una: {fruta}")
    
# Evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"me voy a comer una: {fruta}")
    
    if fruta == "pera":
        break
    
else:
    print("end")
    
# recorrer (iterar) una cadena de texto
for letra in cadena:
    print(letra)
    
# for en una misma linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)