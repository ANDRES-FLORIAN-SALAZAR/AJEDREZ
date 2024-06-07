def imprimir_menu():
    while True:
        print("\n¡Bienvenido al juego de ajedrez!")
        print("1. Fichas Blancas")
        print("2. Fichas Negras")
        print("3. volver al menu")
        print("4. Terminar juego")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n¡Buena suerte!")
            break
        elif opcion == "2":
            print("\n¡Que gane el mejor!")
            break
        elif opcion == "3":
            print("\n¡volver al menú.")
            break
        elif opcion == "4":
            print("\n¡Hasta luego! Gracias por jugar.")
            break
        else:
            print("\nOpción no válida.")
    return opcion
            


imprimir_menu()
