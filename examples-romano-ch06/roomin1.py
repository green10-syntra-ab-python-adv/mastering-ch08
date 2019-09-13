class Foto:
    def __init__(self, interieur, beschrijving):
        self.interieur = interieur
        self.beschrijving = beschrijving

class Interieur:
    def __init__(self, verhaal):
        self.verhaal = verhaal
        self.fotos = list()
    def foto_toevoegen(self, beschrijving):
        foto = Foto(self, beschrijving)
        self.fotos.append(foto)
    def bewaren(self):
        print("Interieur", self.verhaal, "is bewaard met", self.fotos.count(), "foto's")

        
        
