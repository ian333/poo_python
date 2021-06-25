class Rectangulo:
    def __init__(self, base, altura):
        """
        definimos las variables de la clase
        """
        self.base = base
        self.altura = altura

    def area(self):
        """
        Esta clase calcula el area
        """
        print(f"Esto es un Rectangulo de {self.base,self.altura}")
        return self.base*self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)
        print(f"Esto es un cuadrado de {lado}")

if __name__ == "__main__":
    rectangulo= Rectangulo(3,5)
    print(rectangulo.area())

    cuadrado=Cuadrado(5)
    print(cuadrado.area())
    
    pass
