from Juego import Juego

def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Iniciar juego de cifrado")
    print("2. Iniciar juego ordenar")
    print("3. Salir")
    print("======================")

def main():
    juego = Juego()
    valor=True
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            juego.iniciar_juego()
        elif opcion == "2":
            juego.iniciar_ordenado()
        elif opcion == "3":
            juego.salir()
            valor=False
        else:
            print("Opción inválida. Intenta de nuevo.\n")

main()
