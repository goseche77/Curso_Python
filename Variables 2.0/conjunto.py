# Creando un conjunto con set()
conjunto = set(["Dato 1"])

#colocando un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = frozenset(["dato 3"])
conjunto3 = {conjunto1, conjunto2, "dato5"}
print(conjunto3)

# Teoria de Conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5}

# Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# Verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

# Verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)