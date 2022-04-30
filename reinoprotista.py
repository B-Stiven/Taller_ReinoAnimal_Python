from seresVivos import seres


class protista(seres):
    def __init__(self, procariotas, unicelulares):
        self.procariotas = procariotas
        self.unicelulares = unicelulares

    def PasaaCadena(self):
        return print(" Tipología celular:", self.procariotas, " Organización celular:", self.unicelulares)
