with open("archivos\\archivo.txt", "a", encoding='UTF-8') as archivo:
    
    for i in range(5):
        archivo.write(f'Linea {i+1} agregada\n')