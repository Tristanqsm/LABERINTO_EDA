import string

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

# "Linea3" guarda el tercer renglon del archivo txt, donde se encuentra la vida que otorgan los quesos y la vida del raton

# "Laberinto" guardara la estructura del laberinto
    Laberinto = renglon[3:]
    
    print(Laberinto)

    """
    Laberinto = [
            list("EEEXEE"),
            list("EXXXEX"),
            list("EXEEEE"),
            list("EXEXXE"),
            list("EEEEXE"),
    ]
    
    print(f"Las coordenadas del raton son:", "(",xR, ", ",yR, ")")
    print(f"Las coordenadas de la salida son:", "(",xS, ", ",yS, ")")
    imprimeLab(xR, yR, xS, yS, Laberinto)
    """


except FileNotFoundError:
    print("\nERROR    ::EL ARCHIVO NO SE ENCONTRO::\n") 
   
