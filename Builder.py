class Combo:
    def __init__(self):
        self.hamburguesa = None
        self.bebida = None
        self.papas = None

class Builder:
    def __init__(self):
        self.combo = Combo()
    
    def add_hamburguesa(self, tipo):
        self.combo.hamburguesa = tipo
        return self
    
    def add_bebida(self, bebida):
        self.combo.bebida = bebida
        return self
    
    def add_papas(self, papas):
        self.combo.papas = papas
        return self
    
    def build(self):
        return self.combo

combo = Builder().add_hamburguesa("Doble").add_bebida("Coca Cola").add_papas("Grandes").build()
print(vars(combo))