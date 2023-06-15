
# "try" nos ayudara a mandar un mensaje de error si el archivo no le logro abrir
try:
    archivo = open('ArchivoRaton.txt')
    renglon = archivo.readlines()

    Linea1 = renglon[0]
    coordenadasRaton = [Linea1[:1], Linea1[2:3] ]
    coordenadasSalida = [Linea1[4:5], Linea1[6:7]]

    Linea2 = renglon[1]


    Linea3 = renglon[2]


    


except FileNotFoundError:
    print("El archivo no se encontro") 



"""
# Nombre del archivo de texto
nombre_archivo = "ArchivoRaton.txt"

# Leer la línea del archivo de texto
with open(nombre_archivo, "r") as archivo:
    linea = archivo.readline()

# Separar la línea por letras y guardarlas en una lista
lista_letras = list(linea)

# Imprimir la lista de letras
print(lista_letras)
"""