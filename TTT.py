#Minijuego de tres en raya

def inicializar_tablero():
    return [" "] * 10  

#Función para mostrar el tablero
def mostrar_tablero(tablero):
    print(f"""
    {tablero[1]} | {tablero[2]} | {tablero[3]}
    ---------
    {tablero[4]} | {tablero[5]} | {tablero[6]}
    ---------
    {tablero[7]} | {tablero[8]} | {tablero[9]}
    """)

#Función para verificar si alguien ha ganado
def verificar_ganador(tablero):
    combinaciones_ganadoras = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  #Filas
        (1, 4, 7), (1, 5, 8), (3, 6, 9),  #Columnas
        (1, 5, 9), (3, 5, 7)              #Diagonales
    ]
    for x, y, z in combinaciones_ganadoras:
        if tablero[x] == tablero[y] == tablero[z] != " ":
            return tablero[x]  #Define el jugador ganador ('X' o 'O')
    return None

#Función para gestionar los turnos de los jugadores
def jugar_tres_en_raya():
    jugador_actual = "X"  # El jugador X comienza
    
    while True:  #Bucle para reiniciar cuando haya un ganador
        tablero = inicializar_tablero() 
        while " " in tablero: 
            mostrar_tablero(tablero)
            print(f"Turno del jugador {jugador_actual}")
            
            try:
            
                posicion = int(input("Elige una posición (1-9): "))
                if 1 <= posicion <= 9:  #Verificar que la posicion sea correcta
                    if tablero[posicion] == " ":
                        tablero[posicion] = jugador_actual
                        #Verificar si alguien ha ganado
                        ganador = verificar_ganador(tablero)
                        if ganador:
                            mostrar_tablero(tablero)
                            print(f"¡El jugador {ganador} ha ganado!")
                            jugador_actual = ganador  #El ganador comienza la siguiente partida
                            break  
                        # Cambiar el turno
                        jugador_actual = "O" if jugador_actual == "X" else "X"
                    else:
                        print("Posición ocupada. Elige otra.")
                else:
                    print("Posición inválida. Elige un número entre 1 y 9.")
            except (ValueError, IndexError):
                print("Entrada inválida. Elige un número entre 1 y 9.")
        
        #Preguntar si se quiere jugar otra partida
        otra_partida = input("¿Quieres jugar otra partida? (s/n): ").strip().lower()
        if otra_partida == "s":
            continue
        elif otra_partida == "n":
            print("¡Gracias por jugar!")
            break
        else:
            print("Entrada inválida. Por favor, elige 's' para sí o 'n' para no.")

#Volver al juego
jugar_tres_en_raya()
