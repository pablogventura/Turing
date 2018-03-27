class TM(object):
    """
    Clase para las maquinas de turing
    """
    def __init__(self):
        pass
    def avanzar(self):
        pass
    def correr(self):
        while not self.is_halted():
            self.avanzar()
    def is_halted(self):
        pass
