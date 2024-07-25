# Palabra = fooziman
# Output = [F,0,0,Z,1,M,@,N]

def mayusucula(palabra):
    result  = palabra.upper()
    return result

def sustitucion(palabra):
    palabra = palabra.replace('o','0')
    palabra = palabra.replace('i','1')
    palabra = palabra.replace('a','@')
    return palabra

def hack_10():
    result = "fooziman"
    result = list(result)
    result = map(sustitucion, result)
    result = list(result)
    result = map(mayusucula, result)
    result = list(result)
    return result

print(hack_10())













