
class Personaje:
    def __init__(self, nombre, fuerza, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.vida = vida

    def atacar(self, enemigo):
        print(f"Estado actual -> Nombre: {self.nombre} atacó a {enemigo} con fuerza de {self.fuerza}")

    def mostrar_estado(self):
        print(f"Estado actual -> Nombre: {self.nombre}, Vida: {self.vida}")

print("--- INICIANDO SIMULACION ---")

heroe = Personaje("Ragnar",fuerza=45, vida=100)

heroe.mostrar_estado()
heroe.atacar("Un duende enemigo")