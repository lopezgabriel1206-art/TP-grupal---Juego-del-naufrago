import random
from Models.radar import Radar
from Models.tablero import Tablero

def main():
    objetivo = 4
    tableroManager = Tablero();
    tablero_jugador = tableroManager.crear_nuevo_tablero()
    tablero_juego = tableroManager.crear_nuevo_tablero_con_naufragos(objetivo);
    intentos = 20
    radar = Radar()

    while intentos > 0:
        print(f"\nTe quedan {intentos} intentos\nTu tablero:\n")
        tableroManager.mostrar_tablero(tablero_jugador)
        print("\nIngrese las coordenadas para buscar un naufrago (0-4):")

        x = int(input("Ingrese la coordenada x (0 - 4): "))
        while x > 4 or x < 0:
            x = int(input("[ERROR] Ingrese la coordenada x: "))

        y = int(input("Ingrese la coordenada y (0 - 4): "))
        while y > 4 or y < 0:
            y = int(input("[ERROR] Ingrese la coordenada y: "))

        print()
        # Usar match-case como switch
        match (tablero_juego[x][y], tablero_jugador[x][y]):
            case (1, _):
                print("¡Has encontrado un naufrago!")
                tablero_jugador[x][y] = 1
                tablero_juego[x][y] = 0
                objetivo -= 1
            case (_, -1):
                print("Ya buscaste en esa posición y no había naufrago.")
            case (_, 1):
                print("Ya encontraste un naufrago en esa posición.")
            case _:
                print("No hay naufrago en esa posición.")
                tablero_jugador[x][y] = -1
                print("\nRadar de la zona:")
                radar.mostrar_radar(tablero_juego, x, y)

        #mostrar_tablero(tablero_jugador)
        intentos -= 1

        if objetivo == 0:
            print("¡Felicidades! Has encontrado todos los naufragos.")
            break
    

main()
 