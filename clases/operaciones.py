class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes
    
    
    #Regresar True si el número es par False en caso contrario
    def esPar(self, numero):
        if numero % 2 == 0:
            return True
        else:
            return False
    
