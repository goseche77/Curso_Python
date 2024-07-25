#import modulo_saludar as m_saludar

#Desde ese modulo, importamos dos funciones y les cambiamos el nombre con "as"
from modulo_saludar import saludar as saludar_normal ,saludar_raro as saludos_r

#Creamos las variables con los saludos
saludo = saludar_normal("Gustavo")
saludo_raro = saludos_r ("Mario")

#mostramos los saludos
print(saludo)
print(saludo_raro)