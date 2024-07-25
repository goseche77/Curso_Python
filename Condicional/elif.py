
ingreso_mensual = 36000
gasto_mensual = 26001

#if anidados y else if (elif)

if ingreso_mensual > 20:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Todo esta bien")
    else:
        print("Estas gastando demasiado revisa los gastos")

    
# elif ingreso_mensual > 1000:
#     print("Estas bien  economicamente en latinoamerica")
    
# elif ingreso_mensual > 500:
#     print("Estas bien en Venezuela")
    
# elif ingreso_mensual > 200:
#     print("Estas bien en Bolivia")
    
# else:
#     print("bajo recurso economico")
