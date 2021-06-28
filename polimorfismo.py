class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def avanza(self):
        print("Ando caminando")
        
class Ciclista(Persona):
    def __init__(nombre):
        """
        Esta es una clase que representa un ciclista 
        """
        super().__init__(nombre)

    def avanza(self):
        """
        docstring
        """
        print("Ando moviendome en bicicleta")