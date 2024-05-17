import os

tablero = [
    ['to', 'ca', 'al', 'qu', 'ki', 'al', 'ca', 'to'],
    ['pe', 'pe', 'pe', 'pe', 'pe', 'pe', 'pe', 'pe'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE', 'PE'],
    ['TO', 'CA', 'AL', 'QU', 'KI', 'AL', 'CA', 'TO'],
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
                    tab[fila_final][columna_final] == '..'
                ) or (
                    # movimiento diagonal derecha
                    columna_final == columna+1 and
                    tab[fila_final][columna_final] == '..'
                ) or (
                    # movimiento diagonal izquierda
                    columna_final == columna-1 and
                    tab[fila_final][columna_final] == '..'
                )
            ):
        tab[fila_final][columna_final] = 'PE'
        tab[fila][columna] = '..'
    else:
        print('Movimiento no disponible')


def mover_caballo(
    tab,
    fila,
    columna,
    fila_final,
    columna_final
):

    ficha_destino = tab[fila_final][columna_final]
    caballo = tab[fila][columna]

    mover_caballo = False
    # movimientos izquierda
    if fila - 2 == fila_final:
        if columna + 1 == columna_final or columna - 1 == columna_final:
            if tab[fila_final][columna_final] == '..':
                mover_caballo = True
    # movimientos abajo
    elif fila - 1 == fila_final:
        if columna + 2 == columna_final or columna - 2 == columna_final:
            if tab[fila_final][columna_final] == '..':
                mover_caballo = True
    # movimientos derecha
    elif fila + 2 == fila_final:
        if columna + 1 == columna_final or columna - 1 == columna_final:
            if tab[fila_final][columna_final] == '..':
                mover_caballo = True
    # movimiento arriba
    elif fila + 1 == fila_final:
        if columna + 2 == columna_final or columna - 2 == columna_final:
            if tab[fila_final][columna_final] == '..':
                mover_caballo = True
    else:
        mover_caballo = False

    if mover_caballo:
        tab[fila_final][columna_final] = 'CA'
        tab[fila][columna] = '..'
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
                if tab[fila][columna] == '..':
                    mover_reina = True
                    break
        # movimientos derecha
        elif columna > columna_final:
            for i in range(columna_final+1, columna):
                if tab[fila][columna] == '..':
                    mover_reina = True
                    break
     # movimientos arriba
    elif columna == columna_final:
        if fila < fila_final:
            for i in range(fila+1, fila_final):
                if tab[fila][columna] == '..':
                    mover_reina = True
                    break
         # movimientos abajo
        elif fila > fila_final:
            for i in range(fila_final+1, fila):
                if tab[fila][columna] == '..':
                    mover_reina = True
                    break
    else:
        mover_reina = False
    if mover_reina:
        tab[fila_final][columna_final] = 'QU'
        tab[fila][columna] = '..'
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
                if tab[fila][i] == '..':
                    mover_torre = True
                    break

    # movimiento izquierda
        else:
            for i in range(columna - 1, columna_final - 1, -1):
                if tab[fila][i] == '..':
                    mover_torre = True
                    break
# movimiento vertical
    elif columna == columna_final:
        # movimiento arriba
        if fila > fila_final:
            for i in range(fila + 1, fila_final + 1, +1):
                if tab[i][columna] == '..':
                    mover_torre = True
                    break
        # movimiento hacia abajo
        else:
            for i in range(fila + 1, fila_final + 1, +1):
                if tab[i][columna] == '..':
                    mover_torre == True
                    break
    else:
        mover_torre = False
    if mover_torre:
        tab[fila_final][columna_final] = 'TO'
        tab[fila][columna] = '..'
    else:
        print('Movimiento no disponible')


def mover_rey(
    tab,
    fila,
    columna,
    fila_final,
    columna_final
):

    mover_rey = True

    if fila - 1 == fila_final and \
            (
                (
                    # movimiento al frente
                    columna_final == columna and
                    tab[fila_final][columna_final] == '..'
                ) or (
                    # movimiento diagonal derecha
                    columna_final == columna+1 and
                    tab[fila_final][columna_final] == '..'
                ) or (
                    # movimiento diagonal izquierda
                    columna_final == columna-1 and
                    tab[fila_final][columna_final] == '..'
                )
            ):
        tab[fila_final][columna_final] = 'KI'
        tab[fila][columna] = '..'
    else:
        print('Movimiento no disponible')


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


def leer_movimiento():
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
            leer_movimiento()

    else:
        print('movimiento no permitido')
        leer_movimiento()


def mover_ficha(tablero, pos, pos_obj):
    ficha_ini = tablero[pos[0]][pos[1]]
    ficha_obj = tablero[pos_obj[0]][pos_obj[1]]

    blancas = ('to', 'ca', 'al', 'qu', 'ki', 'pe')
    negras = ('TO', 'CA', 'AL', 'QU', 'KI', 'PE')
    espacio = ('..',)

    if (ficha_ini in blancas and ficha_obj in (negras + espacio)) or \
       (ficha_ini in negras and ficha_obj in (blancas + espacio)):

        if ficha_ini in ('TO', 'to'):
            mover_torre(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        elif ficha_ini in ('CA', 'ca'):
            mover_caballo(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        elif ficha_ini in ('QU', 'qu'):
            mover_reina(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])

        elif ficha_ini in ('KI', 'ki'):
            mover_rey(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])
        else:
            ficha_ini in ('PE', 'pe')
            mover_peon(tablero, pos[0], pos[1], pos_obj[0], pos_obj[1])


leer_movimiento()
imprimir_tablero(tablero)
