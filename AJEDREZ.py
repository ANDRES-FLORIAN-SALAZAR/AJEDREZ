import os
import fichas


tablero = [
    [fichas.TORRE_BLANCA, fichas.CABALLO_BLANCO, fichas.ALFIL_BLANCO, fichas.REINA_BLANCA,
        fichas.REY_BLANCO, fichas.ALFIL_BLANCO, fichas.CABALLO_BLANCO, fichas.TORRE_BLANCA],
    [fichas.PEON_BLANCO, fichas.PEON_BLANCO, fichas.PEON_BLANCO, fichas.PEON_BLANCO,
        fichas.PEON_BLANCO, fichas.PEON_BLANCO, fichas.PEON_BLANCO, fichas.PEON_BLANCO],
    [fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO,
        fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO],
    [fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO,
        fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO],
    [fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO,
        fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO],
    [fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO,
        fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO, fichas.ESPACIO],
    [fichas.PEON_NEGRO, fichas.PEON_NEGRO, fichas.PEON_NEGRO, fichas.PEON_NEGRO,
        fichas.PEON_NEGRO, fichas.PEON_NEGRO, fichas.PEON_NEGRO, fichas.PEON_NEGRO],
    [fichas.TORRE_NEGRA, fichas.CABALLO_NEGRO, fichas.ALFIL_NEGRO, fichas.REINA_NEGRA,
        fichas.REY_NEGRO, fichas.ALFIL_NEGRO, fichas.CABALLO_NEGRO, fichas.TORRE_NEGRA],
]


def imprimir_tablero(tablero):
    print('\n\n')
    print('    A ', '  B  ', ' C ', '  D ', '  E ', '  F ', '  G ', '  H ')
    print('   _______________________________________')
    for i, fila, in enumerate(tablero):
        print(i+1, end=' | ')
        for j in fila:
            print(j, end=' | ')
        print(f'{i+1}')
    print('   _______________________________________')
    print('    A ', '  B  ', ' C ', '  D ', '  E ', '  F ', '  G ', '  H ')


def mover_peon(
    tab,
    fila,
    columna,
    fila_final,
    columna_final
):

    if fila - 1 == fila_final and \
            (
                (
                    # movimiento al frente
                    columna_final == columna and
                    tab[fila_final][columna_final] == fichas.ESPACIO
                ) or (
                    # movimiento diagonal derecha
                    columna_final == columna+1 and
                    tab[fila_final][columna_final] == fichas.ESPACIO
                ) or (
                    # movimiento diagonal izquierda
                    columna_final == columna-1 and
                    tab[fila_final][columna_final] == fichas.ESPACIO
                )
            ):
        tab[fila_final][columna_final] = fichas.PEON_NEGRO
        tab[fila][columna] = fichas.ESPACIO
    else:
        print('Movimiento no disponible')

    if fila + 1 == fila_final and \
            (
                (
                    # movimiento al frente
                    columna_final == columna and
                    tab[fila_final][columna_final] == fichas.ESPACIO
                ) or (
                    # movimiento diagonal derecha
                    columna_final == columna+1 and
                    tab[fila_final][columna_final] == fichas.ESPACIO
                ) or (
                    # movimiento diagonal izquierda
                    columna_final == columna-1 and
                    tab[fila_final][columna_final] == fichas.ESPACIO
                )
            ):
        tab[fila_final][columna_final] = fichas.PEON_BLANCO
        tab[fila][columna] = fichas.ESPACIO

    else:
        print('Movimiento no disponible')


def movimiento_valido(ficha_inicial, ficha_objetivo):
    if ficha_inicial in fichas.BLANCAS and ficha_objetivo in (fichas.NEGRAS + (fichas.ESPACIO,)) or \
            ficha_inicial in fichas.NEGRAS and ficha_objetivo in (fichas.BLANCAS + (fichas.ESPACIO,)):
        return True
    return False


def mover_caballo(
    tab,
    fila,
    columna,
    fila_final,
    columna_final
):

    mover_caballo = False

    if ((abs(fila - fila_final) == 2 and abs(columna - columna_final) == 1) or
            (abs(fila - fila_final) == 1 and abs(columna - columna_final) == 2)) and \
            movimiento_valido(tab[fila][columna], tab[fila_final][columna_final]):
        mover_caballo = True

    if mover_caballo:
        tab[fila_final][columna_final] = tab[fila][columna]
        tab[fila][columna] = fichas.ESPACIO
    else:
        print('Movimiento no disponible')


def mover_reina(
        tab,
        fila,
        columna,
        fila_final,
        columna_final):

    mover_reina = True

    if fila == fila_final:
        # movimiento izquierda
        if columna < columna_final:
            for i in range(columna+1, columna_final):
                if tab[fila][columna] == fichas.ESPACIO:
                    mover_reina = True
                    break
        # movimientos derecha
        elif columna > columna_final:
            for i in range(columna_final+1, columna):
                if tab[fila][columna] == fichas.ESPACIO:
                    mover_reina = True
                    break
     # movimientos arriba
    elif columna == columna_final:
        if fila < fila_final:
            for i in range(fila+1, fila_final):
                if tab[fila][columna] == fichas.ESPACIO:
                    mover_reina = True
                    break
         # movimientos abajo
        elif fila > fila_final:
            for i in range(fila_final+1, fila):
                if tab[fila][columna] == fichas.ESPACIO:
                    mover_reina = True
                    break
    else:
        mover_reina = False
    if mover_reina:
        tab[fila_final][columna_final] = fichas.REINA_NEGRA
        tab[fila][columna] = fichas.ESPACIO
    else:
        print('Movimiento no disponible')

    mover_reina = True

    if fila == fila_final:
        # movimiento izquierda
        if columna < columna_final:
            for i in range(columna-1, columna_final):
                if tab[fila][columna] == fichas.ESPACIO:
                    mover_reina = True
                    break
        # movimientos derecha
        elif columna > columna_final:
            for i in range(columna_final-1, columna):
                if tab[fila][columna] == fichas.ESPACIO:
                    mover_reina = True
                    break
     # movimientos arriba
    elif columna == columna_final:
        if fila < fila_final:
            for i in range(fila-1, fila_final):
                if tab[fila][columna] == fichas.ESPACIO:
                    mover_reina = True
                    break
         # movimientos abajo
        elif fila > fila_final:
            for i in range(fila_final-1, fila):
                if tab[fila][columna] == fichas.ESPACIO:
                    mover_reina = True
                    break
    else:
        mover_reina = False
    if mover_reina:
        tab[fila_final][columna_final] = fichas.REINA_BLANCA
        tab[fila][columna] = fichas.ESPACIO
    else:
        print('Movimiento no disponible')


def mover_torre(
    tab,
    fila,
    columna,
    fila_final,
    columna_final
):

    mover_torre = True
    # movimiento horizontal
    if fila == fila_final:
        # movimiento derecha
        if columna < columna_final:
            for i in range(columna + 1, columna_final + 1, +1):
                if tab[fila][i] == fichas.ESPACIO:
                    mover_torre = True
                    break

    # movimiento izquierda
        else:
            for i in range(columna - 1, columna_final - 1, -1):
                if tab[fila][i] == fichas.ESPACIO:
                    mover_torre = True
                    break
# movimiento vertical
    elif columna == columna_final:
        # movimiento arriba
        if fila > fila_final:
            for i in range(fila + 1, fila_final + 1, +1):
                if tab[i][columna] == fichas.ESPACIO:
                    mover_torre = True
                    break
        # movimiento hacia abajo
        else:
            for i in range(fila + 1, fila_final + 1, +1):
                if tab[i][columna] == fichas.ESPACIO:
                    mover_torre = True
                    break
    else:
        mover_torre = False
    if mover_torre:
        tab[fila_final][columna_final] = fichas.TORRE_NEGRA
        tab[fila][columna] = fichas.ESPACIO
    else:
        print('Movimiento no disponible')

    mover_torre = True
    # movimiento horizontal
    if fila == fila_final:
        # movimiento derecha
        if columna < columna_final:
            for i in range(columna - 1, columna_final - 1, -1):
                if tab[fila][i] == fichas.ESPACIO:
                    mover_torre = True
                    break

    # movimiento izquierda
        else:
            for i in range(columna + 1, columna_final + 1, +1):
                if tab[fila][i] == fichas.ESPACIO:
                    mover_torre = True
                    break
# movimiento vertical
    elif columna == columna_final:
        # movimiento arriba
        if fila > fila_final:
            for i in range(fila - 1, fila_final - 1, -1):
                if tab[i][columna] == fichas.ESPACIO:
                    mover_torre = True
                    break
        # movimiento hacia abajo
        else:
            for i in range(fila - 1, fila_final - 1, -1):
                if tab[i][columna] == fichas.ESPACIO:
                    mover_torre = True
                    break
    else:
        mover_torre = False
    if mover_torre:
        tab[fila_final][columna_final] = fichas.TORRE_BLANCA
        tab[fila][columna] = fichas.ESPACIO
    else:
        print('Movimiento no disponible')


def mover_rey(
    tab,
    fila,
    columna,
    fila_final,
    columna_final
):

    mover_rey = False

    if (abs(fila - fila_final) <= 1 and abs(columna - columna_final) <= 1) and \
            movimiento_valido(tab[fila][columna], tab[fila_final][columna_final]):
        mover_rey = True

    if mover_rey:
        tab[fila_final][columna_final] = tab[fila][columna]
        tab[fila][columna] = fichas.ESPACIO
    else:
        print('Movimiento no disponible')


def mover_alfil(
        tab,
        fila,
        columna,
        fila_final,
        columna_final):

    if not (0 <= fila < len(tab) and 0 <= columna < len(tab[0])):
        print("Movimiento no valido")
        return

    # Verifica si el movimiento es en diagonal
    if abs(fila_final - fila) != abs(columna_final - columna):
        print("Movimiento no válido.")
        return

    # Verifica si todas las casillas entre la posición actual y la posición final están vacías
    delta_fila = 1 if fila_final > fila else -1
    delta_columna = 1 if columna_final > columna else -1

    for i in range(1, abs(fila_final - fila)):
        fila_intermedia = fila + i * delta_fila
        columna_intermedia = columna + i * delta_columna
        if tablero[fila_intermedia][columna_intermedia] != fichas.ESPACIO:
            print("movimiento no valido.")
            return

    # Realiza el movimiento
    tablero[fila_final][columna_final] = fichas.ALFIL_NEGRO
    tablero[fila][columna] = fichas.ESPACIO
    print("Movimiento valido.")

    if not (0 <= fila < len(tab) and 0 <= columna < len(tab[0])):
        print("Movimiento no valido")
        return

    # Verifica si el movimiento es en diagonal
    if abs(fila_final + fila) != abs(columna_final + columna):
        print("Movimiento no válido.")
        return

    # Verifica si todas las casillas entre la posición actual y la posición final están vacías
    delta_fila = -1 if fila_final > fila else +1
    delta_columna = -1 if columna_final > columna else +1

    for i in range(1, abs(fila_final - fila)):
        fila_intermedia = fila - i * delta_fila
        columna_intermedia = columna - i * delta_columna
        if tablero[fila_intermedia][columna_intermedia] != fichas.ESPACIO:
            print("movimiento no valido.")
            return

    # Realiza el movimiento
    tablero[fila_final][columna_final] = fichas.ALFIL_BLANCO
    tablero[fila][columna] = fichas.ESPACIO
    print("Movimiento valido.")


def pos2int(pos):
    f1 = int(pos[1])-1
    c1 = 'ABCDEFGH'.find(pos[0])
    f2 = int(pos[3])-1
    c2 = 'ABCDEFGH'.find(pos[2])

    return f1, c1, f2, c2


def clear_screen():
    comando = 'cls'
    if os.name != 'nt':
        comando = 'clear'

    os.system(comando)


def leer_movimiento(tablero):
    movimiento = input('ingrese el movimiento: ')
    movimiento = movimiento.upper()

    if len(movimiento) == 4:
        cols = 'ABCDEFGH'
        filas = '12345678'
        if movimiento[0] in cols and \
                movimiento[1] in filas and \
                movimiento[2] in cols and \
                movimiento[3] in filas:
            print('movimiento valido')
            f1, c1, f2, c2 = pos2int(movimiento)
            print(f'{movimiento[1]} : {f1} |{
                  movimiento[0]} : {c1}|{tablero[f1][c1]}')
            print(f'{movimiento[3]} : {f2} |{
                  movimiento[2]} : {c2}|{tablero[f2][c2]}')
            mover_ficha(tablero, (f1, c1), (f2, c2))

        else:
            print('movimiento no permitido')
            leer_movimiento(tablero)

    else:
        print('movimiento no permitido')
        leer_movimiento(tablero)


def mover_ficha(tablero, pos, pos_obj):
    ficha_ini = tablero[pos[0]][pos[1]]
    ficha_obj = tablero[pos_obj[0]][pos_obj[1]]

    if movimiento_valido(ficha_ini, ficha_obj):
        if ficha_ini in (fichas.TORRE_NEGRA, fichas.TORRE_BLANCA):
            mover_torre(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        elif ficha_ini in (fichas.CABALLO_NEGRO, fichas.CABALLO_BLANCO):
            mover_caballo(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        elif ficha_ini in (fichas.REINA_NEGRA, fichas.REINA_BLANCA):
            mover_reina(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        elif ficha_ini in (fichas.REY_NEGRO, fichas.REY_BLANCO):
            mover_rey(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        elif ficha_ini in (fichas.ALFIL_NEGRO, fichas.ALFIL_BLANCO):
            mover_alfil(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        elif ficha_ini in (fichas.PEON_NEGRO, fichas.PEON_BLANCO):
            mover_peon(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        else:
            print('Movimiento invalido')


imprimir_tablero(tablero)
leer_movimiento(tablero)
imprimir_tablero(tablero)
