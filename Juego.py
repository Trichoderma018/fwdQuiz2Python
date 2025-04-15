class Juego:
    def __init__(self):
        self.jugando = False

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego!")
        print("El juego ha comenzado..")
        self.cifrar()
        print("¡Gracias por jugar!\n")

    def cifrar(self):
        mensaje_cifrado=""
        mensaje = input("Ingrese la palabra a cifrar: ")
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        desplazamiento = 1
        for caracter in mensaje.lower():
            if caracter in alfabeto:
                #Encuentra la posicion en el alfabeto
                posicion = alfabeto.find(caracter)
                #Nueva posicion despues del desplazamiento
                nueva_posicion = (posicion + desplazamiento) % len(alfabeto)
                #Agregar el caracter cifrado al mensaje
                mensaje_cifrado += alfabeto[nueva_posicion]
            else:
                #Para caracteres que no estan en el alfabeto
                mensaje_cifrado += caracter
        print("")
        print("El mensaje cifrado es: ")
        print(mensaje_cifrado)
        print("")

    def salir(self):
        print(f"\nHasta luego. ¡Vuelve pronto!")


  
    


