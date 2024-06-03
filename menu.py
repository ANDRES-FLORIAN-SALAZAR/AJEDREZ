def menu():
    while True:
        print("\n¡Bienvenido al juego de ajedrez!")
        print("1. Jugar con las Blancas")
        print("2. Jugar con las Negras")
        print("3. Terminar juego")
        print("4. volver al menu")
        opcion = input("Selecciona una opción (1/2/3/4/5): ")

        if opcion == "1":
            print("\nComienzan las Blancas. ¡Buena suerte!")
            break
        elif opcion == "2":
            print("\nComienzan las Negras. ¡Que gane el mejor!")
            break
        elif opcion == "3":
            print("\n¡Hasta luego! Gracias por jugar.")
            break
        elif opcion == "4":
            print("\n¡volver al menú.")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona 1, 2, 3, 4.")

menu()