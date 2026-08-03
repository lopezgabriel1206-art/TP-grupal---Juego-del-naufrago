import random

class Tablero:
    def __init__(self):
        pass

    def mostrar_tablero(self, tablero):
        ancho = 4
        columnas = len(tablero[0])

        encabezado = "".join(f"{j:<{ancho}}" for j in range(columnas))
        print("   " + encabezado)
        print("  +" + "-" * (ancho * columnas))

        for i, fila in enumerate(tablero):
            valores = "".join(f"{valor:<{ancho}}" for valor in fila)
            print(f"{i:<2}| {valores}")

    def crear_nuevo_tablero(self):
        tablero = []
        for i in range(5):
            fila = []
            for j in range(5):
                fila.append(0)
            tablero.append(fila)
        return tablero

    def crear_nuevo_tablero_con_naufragos(self, naufragos_a_colocar: int):
        tablero = self.crear_nuevo_tablero()

        if naufragos_a_colocar > 25 or naufragos_a_colocar < 0:
            raise ValueError("No se pueden colocar más de 25 naufragos en un tablero de 5x5.") 
        
        for i in range(0, naufragos_a_colocar):
            x = random.randint(0, 4)
            y = random.randint(0, 4)
            if tablero[x][y] == 0:
                tablero[x][y] = 1  # Colocar un naufrago

        return tablero