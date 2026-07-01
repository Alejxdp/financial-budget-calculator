class Eyden:
    def __init__ (self, nombre, altura, peso):
        self.nombre = nombre
        self.altura = altura
        self.peso = peso

    def correr(self, distancia, velocidad):
        print(f"{self.nombre} corrio una {distancia} a una velocidad de {velocidad}")
    
    def mostrar_atributos (self):
        print(f"Nombre: {self.nombre}, Altura: {self.altura}, Peso: {self.peso}kg")

print("--- INICIANDO SIMULACION ---")
corredor = Eyden("Eyden", altura = 1.72, peso = 70)
corredor.mostrar_atributos()
corredor.correr("carrera de 100m", "20")