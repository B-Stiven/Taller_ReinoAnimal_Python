from seresVivos import seres


class animal(seres):
    def __init__(self, pluricelulares, eucariotas, alimentaciónheterótrofa, respiraciónaeróbica, reproducciónsexual, capacidaddesplazamiento):
        self.pluricelulares = pluricelulares
        self. eucariotas = eucariotas
        self.alimentaciónheterótrofa = alimentaciónheterótrofa
        self.respiraciónaeróbica = respiraciónaeróbica
        self.reproducciónsexual = reproducciónsexual
        self.capacidaddesplazamiento = capacidaddesplazamiento

    def PasaAcadena(self):
        return print("Organización celular:", self.pluricelulares, "Tipología celular:", self.eucariotas, "Nutrición:", self.alimentaciónheterótrofa, "Respiracion:", self.respiraciónaeróbica, "Reproducción:", self.reproducciónsexual, "Locomoción:", self.capacidaddesplazamiento)
