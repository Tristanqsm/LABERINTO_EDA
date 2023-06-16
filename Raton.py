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

#Comprueba que el raton no se salte casillas en la coordenada x
def movimientosX(xi, x):
    if xi == 0 and x == 1:
        return 1
    elif xi == 4 and x == 3:
        return 1
    elif xi + 1 == x or xi - 1 == x or x == xi:
        return 1
    else: 
        return 0
    
#Comprueba que el raton no se salte casillas en la coordenada y
def movimientosY(yi, y):    
    if yi == 0 and y == 1 :
        return 1
    elif yi == 4 and y == 3:
        return 1
    elif yi + 1 == y or yi - 1 == y or y == yi:
        return 1
    else: 
        return 0

#Se crea una funcion que valide que las coordenadas a mover no choquen con paredes, esten dentro del laberinto 
#y no haya saltos en los movimientos
def coordenadasValidas(xi, yi, x, y, Laberinto):
    
    if movimientosX(xi, x):
        if movimientosY(yi, y):
            if (Laberinto[y][x] != "X"): #Si en las coordenadas no hay una x, se puede mover
                return 1
        else:
            print("\nCoordenada invalida")
            return 0
    else:
        print("\nCoordenada invalida")
        return 0
    
#moverRaton nos ayuda a visualizar donde se encuentra el raton, modificando las listas del laberinto, segun las coordenadas que pida el usuario
def moverRaton(Laberinto, xi, yi):
    
    print("\nIngrese las coordenas para mover al raton") #Se piden las nuevas coordenadas
    x = int(input("x = "))
    y = int(input("y = "))
    
    if (coordenadasValidas(xi, yi, x, y, Laberinto)): #Si coordenadas validas retorna un 1, es posible moverse alli
        Laberinto[yi][xi] = "E" #Se borra al antiguo raton
        Laberinto[y][x] = "R"
        return (x, y)
    else:
        print("No es posible realizar el movimiento\n")
        return (xi, yi)

#
#def resolucion():
    #print


#======== AQUI EMPIEZA EL PROGRAMA PRINCIPAL ========#
# "try" nos ayudara a mandar un mensaje de error si el archivo no le logro abrir
try:
    archivo = open('ArchivoRaton.txt')
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
    for coordenada in Coordenadas:
        x, y = map(int, coordenada.split(','))
        Quesos.append([x,y])

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
    print(f"Las coordenadas del raton son:", "(",xR, ", ",yR, ")")
    print(f"Las coordenadas de la salida son:", "(",xS, ", ",yS, ")")
    print(f"Las coordenadas de los quesos son:", Quesos)
    print(f"La vida que otorga un queso es:", vQ)
    print(f"La vida del raton es:", vR)
    
#Laberinto inicial:    
    imprimeLab(xR, yR, xS, yS, Laberinto, Quesos)
    
#Se piden las nuevas coordenadas para mover al raton:
    (xR, yR) = moverRaton(Laberinto, xR, yR)
    imprimeLab(xR, yR) #Se actualiza el laberinto
    
    #resolucion()

#Si el archivo no se puede abrir se imprimira un mensaje de ERROR
except FileNotFoundError:
    print("\nERROR    ::EL ARCHIVO NO SE ENCONTRO::\n") 
   
