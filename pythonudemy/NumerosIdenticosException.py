#clase que detecta excepciones de numeros identicos
class NumerosIdenticosException(Exception):
    def __init__(self, mensaje):
        self.messaje = mensaje
