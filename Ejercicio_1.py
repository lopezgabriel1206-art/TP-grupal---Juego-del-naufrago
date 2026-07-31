import random

def main():
    objetivo = 4
    tablero_jugador = crear_nuevo_tablero()
    tablero_juego = crear_nuevo_tablero_con_naufragos(objetivo);
    intentos = 20

    while intentos > 0:
        print(f"Te quedan {intentos} intentos\n")
        mostrar_tablero(tablero_jugador)
        print("\nIngrese las coordenadas para buscar un naufrago (0-4):")

        x = int(input("Ingrese la coordenada x: "))
        while x > 4 or x < 0:
            x = int(input("[ERROR] Ingrese la coordenada x: "))

        y = int(input("Ingrese la coordenada y: "))
        while y > 4 or y < 0:
            y = int(input("[ERROR] Ingrese la coordenada y: "))

        if tablero_juego[x][y] == 1:
            print("¡Has encontrado un naufrago!")
            tablero_jugador[x][y] = 1
            tablero_juego[x][y] = 0
            objetivo -= 1
        else:
            print("No hay naufrago en esa posición.")
            tablero_jugador[x][y] = -1

        #mostrar_tablero(tablero_jugador)
        intentos -= 1

        if objetivo == 0:
            print("¡Felicidades! Has encontrado todos los naufragos.")
            break


def mostrar_tablero(tablero):
    for fila in tablero:
        for valor in fila:
            print(valor, end="\t")
        print()

def crear_nuevo_tablero():
    tablero = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(0)
        tablero.append(fila)
    return tablero

def crear_nuevo_tablero_con_naufragos(naufragos_a_colocar: int):

    tablero = crear_nuevo_tablero()

    if naufragos_a_colocar > 25 or naufragos_a_colocar < 0:
        raise ValueError("No se pueden colocar más de 25 naufragos en un tablero de 5x5.") 
    
    for i in range(0, naufragos_a_colocar):
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        if tablero[x][y] == 0:
            tablero[x][y] = 1  # Colocar un naufrago

    return tablero


def utilizar_radar(tablero, x, y):
    if x < 0 or x > 4 or y < 0 or y > 4:
        raise ValueError("Coordenadas fuera de rango. Deben estar entre 0 y 4.")

    
    

main()
 