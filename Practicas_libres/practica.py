
# alimentos = 120

# if alimentos >= 105:
#     print("te pasaste del presupuesto")
    
# else:
#     print("todo esta en orden")

ingreso_mensual = 1500
gasto_mensual = 500
    
if ingreso_mensual > 0:
    if ingreso_mensual - gasto_mensual < 0:
        print("estamos en deficit")
    elif ingreso_mensual - gasto_mensual > 600:
        print("todo esta bien")
    else:
        print("debemos revisar el presupuesto, estamos gastanto mucho")