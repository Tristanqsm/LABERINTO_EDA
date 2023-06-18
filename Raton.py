"""
INTEGRANTES:
    - Sanchez Mayen Tristan Qesen
    - Hernandez Nativitas Sofia Alejandra
MAESTRO: Gabriel Castillo Hernandez

EXAMEN EDA - LABERINTO
"""

#La funcion "imprimeLab" imprimira el laberinto y colocara el raton, salida y quesos segun los datos leidos del archivo txt
def imprimeLab(xR, yR, xS, yS, Laberinto, Quesos):
    Laberinto[yR][xR] = 'R'
    Laberinto[yS][xS] = 'S'
    for n in Quesos:
        Laberinto[n[1]][n[0]] = 'Q'

    print("\nEl laberinto es: \n")
    for fila in Laberinto:
        for columna in fila:
            if columna == 'E':
                print(f'E', end = ' ')
            else:
                if columna == 'R':
                    print(f'R', end = ' ')
                else:
                    if columna == 'S':
                        print(f'S', end = ' ')
                    else:
                        if columna == 'Q':
                            print(f'Q', end = ' ')
                        else:
                            print(f'X', end = ' ')
        print()
    print()
    return

def posiblesCaminos(Laberinto, xR, yR):
    posiblesPasos = []

    #Arriba
    if yR > 0 and Laberinto[yR-1][xR] != 'X':
        posiblesPasos.append([xR, yR-1])
    
    #Derecha
    if xR < len(Laberinto[0]) - 1 and Laberinto[yR][xR+1] != 'X':
            posiblesPasos.append([xR+1, yR])

    #Abajo
    if yR < (len(Laberinto[0]) - 1) and Laberinto[yR+1][xR] != 'X':
        posiblesPasos.append([xR, yR+1])

    #Izquierda
    if xR > 0 and Laberinto[yR][xR-1] != 'X':
        posiblesPasos.append([xR-1, yR])
        
    return posiblesPasos

def resolucion(xR,yR, xS, yS, Laberinto, camino):
    
    posibleCamino = []
    
    if xR == xS and yR == yS:
        print("LOGRE SALIR!!")
        camino.append([xS, yS])
        print("Mi camino fue: ", camino)
        return
    
    coordenada = [xR, yR]
    
    #Con un try se busca si hay un bucle
    try:
        
        #En caso de ya haber pasado por ahi, encontramos el indice en el que esta el paso repetido
        indice = camino.index(coordenada) 
        
        #Usamos dos variables adicionales para almacenar el movimiento repetido
        xRep = xR
        yRep = yR
        
        #Encontramos el paso anterior al paso repetido y hacemos backtrack
        xR = camino[indice - 1][0]
        yR = camino[indice - 1][1]
        
        #Se vuelven a buscar los posibles caminos
        posibleCamino = posiblesCaminos(Laberinto, xR, yR)
        
        #Se remueve la coordenada repetida para salir del bucle
        posibleCamino.remove([xRep, yRep]) 
        
        #Se mueve a otra dirección 
        xR = posibleCamino[0][0]
        yR = posibleCamino[0][1]
        camino.append([xR, yR])
        resolucion(xR,yR,xS,yS, Laberinto, camino)
        
    except:
        posibleCamino = posiblesCaminos(Laberinto, xR, yR)
        
        xR = posibleCamino[0][0]
        yR = posibleCamino[0][1]
        camino.append([xR, yR])
        resolucion(xR,yR,xS,yS, Laberinto, camino)
    


#======== AQUI EMPIEZA EL PROGRAMA PRINCIPAL ========#
# "try" nos ayudara a mandar un mensaje de error si el archivo no le logro abrir
try:
    nombreArchivo = 'ArchivoRaton.txt'
    archivo = open(nombreArchivo)
    # "renglon" es una lista. Cada renglon del archivo txt es un elemento de la lista
    renglon = archivo.readlines()

# "Linea1" guarda el primer renglon del archivo txt, donde se encuentra las coordenadas del raton y las coordenadas de la salida
    Linea1 = renglon[0]

    #Coordenadas del raton:
    xR = int(Linea1[:1])
    yR = int(Linea1[2:3])

    #Coordenadas de la salida:
    xS = int(Linea1[4:5])
    yS = int(Linea1[6:7])

# "Linea2" guarda el segundo renglon del archivo txt, donde se encuentran las coordenadas de los quesos
    Linea2 = renglon[1]
    Quesos = []
    Coordenadas = Linea2.replace('(', '').replace(')', '').split()
    Coordenadas = list(map(int, Coordenadas))
    
    i = 0
    while i<7:
        x = Coordenadas[i]
        y = Coordenadas[i + 1]
        Quesos.append([x,y])
        i = i + 2

# "Linea3" guarda el tercer renglon del archivo txt, donde se encuentra la vida que otorgan los quesos y la vida del raton
    Linea3 = renglon[2]

    #Vida de los quesos:
    vQ = int(Linea3[0:2])

    #Vida del raton:
    vR = int(Linea3[3:5])


# "Laberinto" guarda la estructura del laberinto    
    renglon = renglon[3:]
    Laberinto = []
    for r in renglon:
        L = r.strip().split()
        Laberinto.append(L)
    Laberinto = [list(sublista[0]) for sublista in Laberinto]

#Datos leidos:
    camino = []
    print("\n============ L A B E R I N T O ============\n")
    print(f"Las coordenadas del raton son:", "(",xR, ", ",yR, ")")
    print(f"Las coordenadas de la salida son:", "(",xS, ", ",yS, ")")
    print(f"Las coordenadas de los quesos son:", Quesos)
    print(f"La vida que otorga un queso es:", vQ)
    print(f"La vida del raton es:", vR)
    
    imprimeLab(xR, yR, xS, yS, Laberinto, Quesos)
    
    resolucion(xR, yR, xS, yS, Laberinto, camino)

    archivo.close()
    print("\n\nARCHIVO CERRADO: ", archivo.closed)

#Si el archivo no se puede abrir se imprimira un mensaje de ERROR
except FileNotFoundError:
    print("\nERROR    ::EL ARCHIVO NO SE ENCONTRO::\n") 
