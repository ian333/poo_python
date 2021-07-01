class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
    
    def avanza(self):
        print("Ando caminando")
        
class Ciclista(Persona):
    
    def __init__(self,nombre):
        """
        Esta es una clase que representa un ciclista y se extiende a la funcion Persona 
        """
        super().__init__(nombre)

    def avanza(self):
        """
        Esta funcion imprime un mensaje
        """
        print("Ando moviendome en bicicleta")

def main():
    """
    Esta es la funcion principal por la cual correra nuestro programa
    """
    persona=Persona("David")
    persona.avanza()

    ciclista=Ciclista('Daniela')
    ciclista.avanza()
    

if __name__ == "__main__":
    main()