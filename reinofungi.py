from seresVivos import seres


class fungi(seres):
    def __init__(self, pluricelulares, aerobios, eucariotas, heterótrofos, reproducenmedianteesporas):
        self.pluricelulares = pluricelulares
        self. aerobios = aerobios
        self.eucariotas = eucariotas
        self.heterótrofos = heterótrofos
        self.reproducenmedianteesporas = reproducenmedianteesporas

    def PasaacaDena(self):
        return print("Organización celular:", self.pluricelulares,  "Respiración:", self.aerobios, "Tipología celular:", self.eucariotas, "Nutrición:", self.heterótrofos, "Reproducción:", self.reproducenmedianteesporas)
