class Juego:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        print("Aqui va el juego o los metodos de instancia donde vas a crear la logica del juego.")


        print("¡Gracias por jugar!\n")

    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")


  
    


