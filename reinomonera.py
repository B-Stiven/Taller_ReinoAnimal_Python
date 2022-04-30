from seresVivos import seres


class monera(seres):
    def __init__(self, heterotrofas, aerobias):
        self.heterotrofas = heterotrofas
        self. aerobias = aerobias

    def PasaacadEna(self):
        return print("Nutrición:", self.heterotrofas, "Respiración:", self.aerobias)
