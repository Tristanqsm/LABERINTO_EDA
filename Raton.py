def imprimeLab(xR, yR, xS, yS, Laberinto):
    Laberinto[xR][yR] = 'R'
    Laberinto[xS][yS] = 'S'

    print("\nEl laberinto es: \n")
    for r in Laberinto:
        for c in r:
            if c == 'E':
                print(f'E', end = ' ')
            elif c == 'R':
                print(f'R', end = ' ')
            elif c == 'S':
                print(f'S', end = ' ')
            elif c == 'Q':
                print(f'Q', end = ' ')
            else:
                print(f'X', end = ' ')
        print()
    print()
    return


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
    
    # Coordenadas del primer queso:
    xQ1 = int(Linea2[0])
    yQ1 = int(Linea2[2])
    
    # Coordenadas del segundo queso:
    xQ2 = int(Linea2[4])
    yQ2 = int(Linea2[6])
    
    # Coordenadas del tercer queso:
    xQ3 = int(Linea2[8])
    yQ3 = int(Linea2[10])
    
    # Coordenadas del cuarto queso:
    xQ4 = int(Linea2[12])
    yQ4 = int(Linea2[14])


# "Linea3" guarda el tercer renglon del archivo txt, donde se encuentra la vida que otorgan los quesos y la vida del raton
    Linea3 = renglon[2]

    #Vida de los quesos:
    vQ = int(Linea3[0:2])

    #Vida del raton:
    vR = int(Linea3[3:5])
    
# "Laberinto" guardara la estructura del laberinto
    #"""
    renglon = renglon[3:]
    Laberinto = []
    for r in renglon:
        L = r.strip().split()
        Laberinto.append(L)
    Laberinto = [list(sublista[0]) for sublista in Laberinto]
    
    print(f"Las coordenadas del raton son:", "(",xR, ", ",yR, ")")
    print(f"Las coordenadas de la salida son:", "(",xS, ", ",yS, ")")
    print(f"Las coordenadas de los quesos son:")
    print(f"La vida que otorga un queso es:", vQ)
    print(f"La vida del raton es:", vR)
    imprimeLab(xR, yR, xS, yS, Laberinto)



except FileNotFoundError:
    print("\nERROR    ::EL ARCHIVO NO SE ENCONTRO::\n") 
   
