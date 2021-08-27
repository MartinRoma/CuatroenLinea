#Dimensiones Tablero

d = [6,7]

#Función Generadora de Tablero

def GenerarTableroVacio():
    tablero = []
    for y in list(range(d[1])):
        fila = []
        for x in range(d[0]):
            fila.append(0)
        tablero.append(fila)
    return tablero

tab = GenerarTableroVacio()

print(tab)
