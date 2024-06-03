def imprimir_menu():
    while True:
        print("\n¡Bienvenido al juego de ajedrez!")
        print("1. Fichas Blancas")
        print("2. Fichas Negras")
        print("3. Terminar juego")
        print("4. volver al menu")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("\n¡Buena suerte!")
            break
        elif opcion == "2":
            print("\n¡Que gane el mejor!")
            break
        elif opcion == "3":
            print("\n¡Hasta luego! Gracias por jugar.")
            break
        elif opcion == "4":
            print("\n¡volver al menú.")
            break
        else:
            print("\nOpción no válida.")

imprimir_menu()