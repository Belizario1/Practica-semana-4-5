class Transporte:
    def entregar(self):
        pass

class Camion(Transporte):
    def entregar(self):
        return "Entrega por carretera"

class Barco(Transporte):
    def entregar(self):
        return "Entrega por mar"

class Avion(Transporte):  # Añadido un tercer transporte
    def entregar(self):
        return "Entrega por aire"

class Factory:
    @staticmethod
    def get_transporte(tipo):
        if tipo == "camion": return Camion()
        elif tipo == "barco": return Barco()
        elif tipo == "avion": return Avion()

t = Factory.get_transporte("avion")
print(t.entregar())