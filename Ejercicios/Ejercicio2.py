'''Para jugar al PUM los N jugadores se sientan en circulo y van diciendo números consecutivos
a partir del 1 (1, 2, 3, ...). Para el juego se escoge un número X menor que 10 (por ejemplo 7)
y a la persona a la que le corresponda decir un múltiplo de ese número (en el caso del 7: 7,
14, 21, 28, ...), debe decir, en vez del número, la palabra PUM. Escriba un programa que
muestre, a partir del número de jugadores N y del número escogido para el PUM, X, el
desarrollo del juego para los primeros 500 números, indicando el número del jugador y lo
que dijo. Por ejemplo, si son 3 jugadores y X es el 4 el juego comenzaría así:'''


rondas = 500
numeroJugadores = int(input("Ingrese la cantidad de Jugadores: "))
numeroPUM = int(input("Ingrese el número escogido para el PUM: "))
jugador = 1

#Se establece un ciclo definido entre 1 y el numero de rondas
for i in range (1, rondas +1):
    
    #Se pregunta si la iteracion corresponde con un multiplo del numero PUM y se asigna a la variable jugada en caso de que sea si la palabra PUM, sino la jugada
    #corresponde al numero de la ronda
    if (i % numeroPUM == 0):
        jugada = "--PUM--"
    else: jugada = i

    print(f"Jugador {jugador}         {jugada}")

    #luego de mostrar en pantalla, se pasa al siguiente jugador
    jugador +=1

    #se establece una condicion para que se reinicie la ronda desde el primer jugador
    if jugador > numeroJugadores:
        jugador = 1
    
    


    



