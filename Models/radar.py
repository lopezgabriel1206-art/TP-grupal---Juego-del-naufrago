class Radar:
    def __init__(self):
        pass

    def mostrar_radar(self, tablero, x, y):
        if not (0 <= x < 5 and 0 <= y < 5):
            raise ValueError("Coordenadas fuera de rango. Deben estar entre 0 y 4.")

        ancho = 4
        columnas = 5

        encabezado = "".join(f"{j:<{ancho}}" for j in range(columnas))
        print("   " + encabezado)
        print("  +" + "-" * (ancho * columnas))

        for fila in range(5):
            valores = ""
            for columna in range(5):
                if fila == x or columna == y:
                    valor = tablero[fila][columna]
                    celda = "N" if valor == 1 else str(valor)
                else:
                    celda = "·"
                valores += f"{celda:<{ancho}}"
            print(f"{fila:<2}| {valores}")