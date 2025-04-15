class Juego:
    def __init__(self):
        self.jugando = False
        self.contador = 0

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego!")
        print("El juego ha comenzado..")
        self.cifrar()
        print("¡Gracias por jugar!\n")
    def iniciar_ordenado(self):
        self.jugando = True
        self.ordenamiento()
    def ordenamiento(self):
        lista_num = [24,65,4,7,27,82,58,-200,-100,-50]
        lista_final = []
        while lista_num:
            elemento_maximo = lista_num[0]
            for numero in lista_num:
                if numero < elemento_maximo:
                    elemento_maximo = numero
            lista_final.append(elemento_maximo)
            lista_num.remove(elemento_maximo)
        print(f"La lista ordenada es: {lista_final}")

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
        self.contador += 1
        print("")
        print(f"Llevas {self.contador} palabras cifradas")
        print("")

   

    def salir(self):
        print(f"\nHasta luego. ¡Vuelve pronto!")


  
    


