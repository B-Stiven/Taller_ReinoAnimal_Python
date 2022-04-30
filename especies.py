from seresVivos import seres

class especie (seres):
    def __init__(self, Nutrición, Organizacióncelular, Tipologíacelular, Respiración, Reproducción, Locomoción, comunicacion ):
        self.comunicacion=comunicacion
        

    def pasaracadeNA(self):
        return self.comunicacion