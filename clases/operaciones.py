class Operaciones:
    def __init__(self):
        self.alejandroMontes = "Alejandro Montes"
        
    
    def saludoAlejandroMontes(self):
        return "Mi nombre es " + self.alejandroMontes

    def eliminarDuplicados(self, lista):
        return list(set(lista))
    '''
    def operacionesAsignada(self):
        #Realizar la operación asignada
    '''


   

    
    def ordenarLista(self, lista):
        return sorted(lista)    

    def esImpar(self,entero):
        numero = int(entero)
        if numero %2 != 0:
            return True
        else:
            return False   

    def contarPalabrasTexto(self, texto, palabra):
        texto=texto.lower()
        palabra=palabra.lower()
        palabras=texto.split()
        print("En el texto " + texto + ", la palabra "+palabra+" aparece "+str(palabras.count(palabra)) + " veces")
        return palabras.count(palabra)
