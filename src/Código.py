#Dimensiones Tablero

d = [7,6]

#Función Generadora de Tablero

def GenerarTableroVacio(d):
    tablero = []
    for y in range(d[1]):
        fila = []
        for x in range(d[0]):
            fila.append(0)
        tablero.append(fila)
    return tablero

tab = GenerarTableroVacio(d)

#Función que dibuja el tablero
def DibujarTablero(tab):
    for fila in tab:
        for celda in fila:
            if celda == 0:
                print('  ', end='')
            else:
                print(' %s' % celda, end='')
        print('')



#Función para ver si algún jugador ganó
def PartidaTerminada(tab,col,jug,fila):
    c = 1
    if col>=1 and tab[fila][col-1]==jug:
        c=c+1
        if col>=2 and tab[fila][col-2]==jug:
            c=c+1
            if col>=3 and tab[fila][col-3]==jug:
                return True
    if col<=5 and tab[fila][col+1]==jug:
        c=c+1
        if col<=4 and tab[fila][col+2]==jug:
            c=c+1
            if col<=3 and tab[fila][col+3]==jug:
                return True
    if c>=4:
        return True
    else:
        c = 1
        if fila>=1 and tab[fila-1][col]==jug:
            c=c+1
            if fila>=2 and tab[fila-2][col]==jug:
                c=c+1
                if fila>=3 and tab[fila-3][col]==jug:
                    return True
        if fila<=4 and tab[fila+1][col]==jug:
            c=c+1
            if fila<=3 and tab[fila+2][col]==jug:
                c=c+1
                if fila<=2 and tab[fila+3][col]==jug:
                    return True
        if c>=4:
            return True
        else:
            c = 1
            if fila>=1 and col>=1 and tab[fila-1][col-1]==jug:
                c=c+1
                if fila>=2 and col>=2 and tab[fila-2][col-2]==jug:
                    c=c+1
                    if fila>=3 and col>=3 and tab[fila-3][col-3]==jug:
                        return True
            if fila<=4 and col<=5 and tab[fila+1][col+1]==jug:
                c=c+1
                if fila<=3 and col<=4 and tab[fila+2][col+2]==jug:
                    if fila<=2 and col<=3 and tab[fila+3][col+3]==jug:
                        return True
            if c>=4:
                return True
            else:
                c = 1
                if fila<=4 and col>=1 and tab[fila+1][col-1]==jug:
                    c=c+1
                    if fila<=3 and col>=2 and tab[fila+2][col-2]==jug:
                        c=c+1
                        if fila<=2 and col>=3 and tab[fila+3][col-3]==jug:
                            return True
                if fila>=1 and col<=5 and tab[fila-1][col+1]==jug:
                    c=c+1
                    if fila>=2 and col<=4 and tab[fila-2][col+2]==jug:
                        c=c+1
                        if fila>=3 and col<=3 and tab[fila-3][col+3]==jug:
                            return True
                if c>=4:
                    return True
                else:
                    return False
#Función para colocar fichas
#El chiquito es filas
def PonerFicha(tab,col,jug):
    col = col-1
    if tab[0][col]!=0:
        print("Error no podés poner una ficha en una columna llena")
        print("Error en la columna número ",col+1)
        return tab,None,None
    else:
        for c, celda in enumerate(tab):
            if tab[c][col]!=0 :
                fila = c-1
                tab[fila][col] = jug
                return tab,fila,col
        fila = len(tab)-1
        tab[fila][col] = jug
        return tab,fila,col

#Esta función recorre la lista de jugadas para armar el juego
def Juego(tab,jugadas):
    if type(jugadas)!=list:
        print("Error la lista de jugadas es de tipo inválido")
        return None
    else:
        for i, n  in enumerate(jugadas):
            if type(n)!=int or n>d[0] or n<1:
                print("Error todas las jugadas deben ser numeros enteros del 1 al ",d[0])
                break
            else:
                if i%2==0:
                    jug=1
                    tab,fila,col=PonerFicha(tab,n,jug)
                else:
                    jug=2
                    tab,fila,col=PonerFicha(tab,n,jug)
                if col==None:
                    break
                elif PartidaTerminada(tab,col,jug,fila):
                    print("\nEl jugador Número ",jug,"ganó")
                    break
        DibujarTablero(tab)


#Juego(tab,[1,1,1,1,1,1,1,2]) #Juego con error de columna
#Juego(tab,[1,2,2,3,3,4,3,4,4,6])  #Juego incompleto
#Juego(tab,[1,2,3,8]) #Juego con error de fila
#Juego(tab,5) #El tipo de la lista de jugadas es inválido
#Juego(tab,[1,2,3,4,4.0,5]) #Error de tipo dentro de la lista
Juego(tab,[1,2,2,3,3,4,3,4,4,6,4,4]) #Juego ganador con una jugada de más
