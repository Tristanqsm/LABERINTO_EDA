def imprimeLab(Laberinto):
    
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

#Se crea una funcion que valide que el movimiento se encuentra dentro del laberinto
def dentroLaberinto(xR, yR):
    
    if (xR<5 and yR<5): #Si las coordenadas no sobrepasan el 5, esta dentro del laberinto
        return 1
    
    else:
        print("\nCoordenada invalida")
        return 0

#Se crea una funcion que valide que las coordenadas a mover no choquen con paredes y esten dentro del laberinto 
def coordenadasValidas(x, y, Laberinto):
    
    if(dentroLaberinto(x, y)):
        if (Laberinto[y][x] != "X"): #Si en las coordenadas no hay una x, se puede mover
            return 1
        else:
            print("\nCoordenada invalida")
            return 0
    else:
        print("\nCoordenada invalida")
        return 0
    
    
#La funcion vidaRaton actualiza constantemente la cantidad de vida del raton cada que avanza una casilla    
def vidaRaton(vida):
    
    vida = vida - 1
    return vida

#La funcion queso aumenta la vida del raton, en caso de haberse comido el queso 
def queso(vida):
    
    vida = vida + 10
    return vida

#moverRaton nos ayuda a visualizar donde se encuentra el raton, modificando las listas del laberinto, segun las coordenadas que pida el usuario
def moverRaton(Laberinto):
    
    print("\nIngrese las coordenas para mover al raton")
    x = int(input("x = "))
    y = int(input("y = "))
    
    if (coordenadasValidas(x, y, Laberinto)): #Si ambas son iguales es por que retornan un 1, lo que quiere decir que es posible moverse alli
        
        Laberinto[y][x] = "R"
        return Laberinto
    else:
        print("No es posible realizar el movimiento\n")
        return Laberinto
    
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
    renglon = renglon[3:]
    Laberinto = []
    for r in renglon:
        L = r.strip().split()
        Laberinto.append(L)
    Laberinto = [list(sublista[0]) for sublista in Laberinto]
    
#Se agregan los quesos al laberinto
    Laberinto[yQ1][xQ1] = "Q"
    Laberinto[yQ2][xQ2] = "Q"
    Laberinto[yQ3][xQ3] = "Q"
    Laberinto[yQ4][xQ4] = "Q"
        
#Se solicita la vida con la que iniciara el raton y se almacenara en la variable vidaR

    vidaR = int(input("¿Cuanta vida tiene el raton?\n"))
        
#Se llama a la funcion mover Raton para pedir las coordenadas en las que iniciara y verificar que pueda estar alli

    Laberinto = moverRaton(Laberinto)

#Se muestra el laberinto inicial

    imprimeLab(Laberinto)
    
    
    '''
    print(f"Las coordenadas del raton son:", "(",xR, ", ",yR, ")")
    print(f"Las coordenadas de la salida son:", "(",xS, ", ",yS, ")")
    print(f"Las coordenadas de los quesos son:")
    print(f"La vida que otorga un queso es:", vQ)
    print(f"La vida del raton es:", vR)
    imprimeLab(xR, yR, xS, yS, Laberinto)
    '''

except FileNotFoundError:
    print("\nERROR    ::EL ARCHIVO NO SE ENCONTRO::\n") 
   
