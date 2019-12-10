import random

# ===================================
# CREAR MAZO DE CARTAS
# ===================================

def crear_cartas():
    global mazo
    global lista_num
    for i in range(2):
        for i in range(10):
            mazo.append([str(i), "azul"])
            mazo.append([str(i), "verde"])
            mazo.append([str(i), "amarillo"])
            mazo.append([str(i), "rojo"])
    for i in range(2):
        mazo.append(["+2", "azul"])
        mazo.append(["+2", "verde"])
        mazo.append(["+2", "amarillo"])
        mazo.append(["+2", "rojo"])
        mazo.append(["pierde turno", "azul"])
        mazo.append(["pierde turno", "verde"])
        mazo.append(["pierde turno", "amarillo"])
        mazo.append(["pierde turno", "rojo"])
    for i in range(4):
        mazo.append(["+4", "comodín"])
        mazo.append(["cambia color", "comodín"])
    for i in range(10):
        lista_num.append(str(i))

# ================================================
# ELEGIR CARTA
# ==============================================

def elegir_carta():
    global mano_n
    global carta_actual
    global jugador_actual
    print("Te toca jugar jugador %d"%(jugador_actual+1))
    print("La carta actual es: %s %s"%(carta_actual[0],carta_actual[1]))
    print("Elige una carta de tu mano.")
    print("0) Coger carta")
    for i in range(len(mano_n)):
        print("%s) %s %s" % (i + 1, mano_n[i][0], mano_n[i][1])) # [0]=numerica o especial - [1]=color
    if len(mano_n)==2:
        uno()
    return int(input())  # eligiremos la carta "i" y se analizara


# ============================================================
# ANALIZAMOS LA JUGADA Y LAS CARTAS ACTUALES Y SIGUIENTES
# ==============================================================

def analisis():
    global carta_siguiente
    global carta_actual
    global acumulado
    global carta_elegida
    global lista_num
    global mano_n
    global jugando
    opcion = elegir_carta()
    if opcion == 0:
        coger_carta()
    else:
        carta_elegida = opcion - 1
        carta_siguiente = mano_n[carta_elegida]
        if acumulado > 0:
            concatenar_cartas()
        elif carta_actual[1] == "comodín":
            carta_actual_comodin()
        elif carta_siguiente[0] in lista_num:
            carta_numerica()
        elif carta_siguiente[0] == "+2":
            carta_mas_dos()
        elif carta_siguiente[0] == "pierde turno":
            carta_pierde_turno()
        elif carta_siguiente[1] == "comodín":
            carta_comodin()
    if len(mano_n) == 0:
        print("========================================================")
        print("========Enhorabuena jugador %d! Eres el ganador!========"%(jugador_actual+1))
        print("========================================================")
        jugando = False

# ===========================================
# CONCATENAR CARTAS
# ===========================================

def concatenar_cartas():
    global acumulado
    global carta_actual
    global carta_siguiente
    global color_actual
    global carta_elegida
    global mano_n
    if carta_actual[0] == "+2":
        if carta_siguiente[0] == "+2":
            del mano_n[carta_elegida]
            carta_actual = carta_siguiente
            acumulado += 2
            print("Se han acumulado %d cartas por el momento"%(acumulado))
            color_actual = carta_actual[1]
        elif carta_siguiente[0] == "+4":
            del mano_n[carta_elegida]
            carta_actual = carta_siguiente
            opcion = cambia_color()
            color_actual = colores[opcion - 1]
            print("Se ha cambiado a color %s"%(color_actual))
            acumulado += 4
            print("Se han acumulado %d cartas por el momento"%(acumulado))
        else:
            print("No puedes usar esa carta. Puedes encadenar un +4 o un +2 de color %s"%(color_actual))
            analisis()
    elif carta_actual[0] == "+4":
        if carta_siguiente[0] == "+2" and carta_siguiente[1] == color_actual:
            del mano_n[carta_elegida]
            carta_actual = carta_siguiente
            acumulado += 2
            print("Se han acumulado %d cartas por el momento"%(acumulado))
        elif carta_siguiente[0] == "+4":
            del mano_n[carta_elegida]
            opcion = cambia_color()
            color_actual = colores[opcion - 1]
            print("Se ha cambiado a color %s"%(color_actual))
            acumulado += 4
            print("Se han acumulado %d cartas por el momento"%(acumulado))
        else:
            print("No puedes usar esa carta. Puedes encadenar un +4 o un +2 de color %s"%(color_actual))
            analisis()

# ===============================================
# SI LA CARTA ACTUAL ES UN COMODÍN
# ================================================

def carta_actual_comodin():
    global carta_siguiente
    global color_actual
    global carta_elegida
    global mano_n
    global acumulado
    global pierde_turno
    global carta_actual
    if carta_siguiente[1] == color_actual:
        if carta_siguiente[0] in lista_num:
            del mano_n[carta_elegida]
            carta_actual = carta_siguiente
        elif carta_siguiente[0] == "+2":
            del mano_n[carta_elegida]
            carta_actual = carta_siguiente
            acumulado += 2
            print("Se han acumulado %d cartas por el momento"%(acumulado))
        elif carta_siguiente[0] == "pierde turno":
            del mano_n[carta_elegida]
            carta_actual = carta_siguiente
            pierde_turno = True
    elif carta_siguiente[1] == "comodín":
        carta_comodin()
    else:
        print("La carta tiene que ser de color %s"%(color_actual))
        analisis()

# ======================================
# SI LA CARTA ES NUMÉRICA.
# ======================================

def carta_numerica():
    global carta_siguiente
    global color_actual
    global carta_actual
    global mano_n
    global carta_elegida
    if carta_actual == carta_siguiente:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
    elif carta_actual[0] != carta_siguiente[0] and carta_actual[1] == carta_siguiente[1]:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
    elif carta_actual[0] == carta_siguiente[0] and carta_actual[1] != carta_siguiente[1]:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        color_actual = carta_actual[1]
    else:
        print("Las cartas tienen que coincidir en color o en número. Vuelve a intentarlo.")
        analisis()

# =====================================
# SI LA CARTA ES UN +2
# =====================================

def carta_mas_dos():
    global carta_actual
    global carta_siguiente
    global acumulado
    global color_actual
    global turno
    global carta_elegida
    if carta_actual == carta_siguiente:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        acumulado += 2
        print("Se han acumulado %d cartas por el momento"%(acumulado))
    elif carta_actual[0] != carta_siguiente[0] and carta_actual[1] == carta_siguiente[1]:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        acumulado += 2
        print("Se han acumulado %d cartas por el momento"%(acumulado))
    elif carta_actual[0] == carta_siguiente[0] and carta_actual[1] != carta_siguiente[1]:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        acumulado += 2
        print("Se han acumulado %d cartas por el momento"%(acumulado))
        color_actual = carta_actual[1]
    else:
        print("Las cartas tienen que coincidir en color o en número. Vuelve a intentarlo.")
        analisis()

# =====================================
# SI LA CARTA ES UN PIERDE TURNO
# ======================================

def carta_pierde_turno():
    global carta_actual
    global carta_siguiente
    global acumulado
    global color_actual
    global turno
    global carta_elegida
    global pierde_turno
    if carta_actual == carta_siguiente:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        pierde_turno = True
    elif carta_actual[0] != carta_siguiente[0] and carta_actual[1] == carta_siguiente[1]:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        pierde_turno = True
    elif carta_actual[0] == carta_siguiente[0] and carta_actual[1] != carta_siguiente[1]:
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        color_actual = carta_actual[1]
        pierde_turno = True
    else:
        print("Las cartas tienen que coincidir en color o en número. Vuelve a intentarlo.")
        analisis()

# =================================
# SI LA CARTA ES UN COMODÍN
# ==================================

def carta_comodin():
    global carta_actual
    global carta_siguiente
    global acumulado
    global color_actual
    global carta_elegida
    if carta_siguiente[0] == "+4":
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        opcion = cambia_color()
        color_actual = colores[opcion - 1]
        print("Se ha cambiado a color %s"%(color_actual))
        acumulado += 4
        print("Se han acumulado %d cartas por el momento"%(acumulado))
    elif carta_siguiente[0] == "cambia color":
        del mano_n[carta_elegida]
        carta_actual = carta_siguiente
        opcion = cambia_color()
        color_actual = colores[opcion - 1]
        print("Se ha cambiado a color %s"%(color_actual))

# ===================================
# CAMBIAR COLOR
# ===================================

def cambia_color():
    global colores
    print("Elije un color.")
    for i in range(len(colores)):
        print("%s) %s" % (i + 1, colores[i]))
    opcion = int(input())
    while (opcion<1) or (opcion>4):
        opcion = int(input("Error. Elije un color\n"))
    return opcion

# =================================
# COGER CARTA
# =================================

def coger_carta():
    global acumulado
    global mazo
    global mano_n
    if acumulado > 0:
        for i in range(acumulado):
            carta_nueva = random.randint(0, len(mazo)-1)
            mano_n.append(mazo[carta_nueva])
            del mazo[carta_nueva]
    else:
        carta_nueva = random.randint(0, len(mazo)-1)
        mano_n.append(mazo[carta_nueva])
        del mazo[carta_nueva]
    acumulado = 0

# ====================================
# PRIMERA CARTA ALEATORIA NUMÉRICA
# ====================================

def primera_carta():
    global mazo
    global carta_actual
    carta = random.randint(0,len(mazo)-1)
    while mazo[carta][0] not in lista_num:
        carta = random.randint(0,len(mazo)-1)
    carta_actual = mazo[carta]
    del mazo[carta]

# ===========================================
# REPARTIR 7 CARTAS A CADA JUGADOR
# =============================================

def repartir_cartas():
    global mazo
    global jugadores
    for i in range(len(jugadores)):
        for j in range(7):
            carta = random.randint(0,len(mazo)-1)
            jugadores[i].append(mazo[carta])
            del mazo[carta]

# =====================================
# JUGADOR NO DICE UNO
# =====================================
def uno():
    global mano_n
    global mazo
    global jugadores
    if len(mano_n)==2:
        palabramagica=input("La palabra magica es: ")
        if palabramagica!="uno":
            for i in range(2):
                carta = random.randint(0, len(mazo) - 1)
                jugadores[i].append(mazo[carta])
                del mazo[carta]

# ===================================
# ASIGNACIÓN DE TURNOS
# ===================================

def asignar_turno():
    global turno
    global jugadores
    global pierde_turno
    global mano_n
    global jugador_actual
    if pierde_turno == True:
        turno += 1
        if turno > len(jugadores)-1:
            turno = 0
        pierde_turno = False
    turno += 1
    if turno > len(jugadores)-1:
        turno = 0
    mano_n = jugadores[turno]
    jugador_actual = turno

# ===================================
# CREAR JUGADORES
# ===================================

def crear_jugadores():
    global jugadores
    opcion = elegir_jugadores()
    for i in range(opcion):
        jugadores.append([])
    random.shuffle(jugadores)

# ===================================
# NUMERO DE JUGADORES
# ===================================

def elegir_jugadores():
    num_jugadores = int(input("¿Cuantos jugadores sois?(2~8)\n"))
    while (num_jugadores<2) or (num_jugadores>8):
        num_jugadores = int(input("Por favor ingresa un numero de jugadores entre 2 y 8\n"))
    return num_jugadores

# ===================================
# MENU PRINCIPAL
# ===================================

def menu_principal():
    #global listajugadores
    global opcion
    while (opcion != "start") and (opcion != "salir"):
        opcion = input("Por favor escribe start para jugar o salir si no deseas jugar\n")
        opcion = opcion.lower()
        if (opcion == "start"):
            listajugadores = jugadores()
        elif (opcion == "salir"):
            print("Hasta otra!")

# ===================================
# PROGRAMA PRINCIPAL
# ===================================

#------------ VARIABLES GLOBALES -------------

listajugadores = []
mazo = []
colores = ["azul", "amarillo", "rojo", "verde"]
acumulado = 0
turno = 0
lista_num = []
pierde_turno = False
jugadores = []
jugador_actual = 0
carta_actual = []
carta_siguiente = []

#----------- Empieza el programa -----------

crear_jugadores()
crear_cartas()
repartir_cartas()
primera_carta()
jugando = True
jugador_actual = 0
mano_n = jugadores[0]
analisis()
while jugando:
    asignar_turno()
    analisis()
