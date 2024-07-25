#Ejercicio 1
# a) Diferencia en porcentaje entre el curso actual y:
# - El mas rapido de otros cursos
# - El mas lento de otros cursos
# - El promedio de otros cursos

# b) Porcentaje de Material inservible que se reduce en:
# - El promedio de los cursos
# - El curso actual (este curso)

# c) Ver 10 horas de este curso, a cuantas de otros cursos equivale? y al reves?

# Promedio de duracion:
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencia de duracion:
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

# Calculando el % de tiempo vacio:
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


# Mostrando las diferencias de duracion (Ejericio A)
print("----------------------------------------------------------------------------")
print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f'El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f'El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio')
print("----------------------------------------------------------------------------")
# Mostrando la cantidad de espacion vacios que se remueven (Ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimina el {tiempo_vacio_dalto}% de tiempo vacio')
print("----------------------------------------------------------------------------")
# Mostrando diferencias si los cursos duraran 10 horas

print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso')
print("----------------------------------------------------------------------------")