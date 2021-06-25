def funcion_decoradora(funcion):
    def wrapper():
        print("Este es el último mensaje...")
        funcion()
        print("Este es el primer mensaje ;)")
    return wrapper

# def zumbido():
#    print("Buzzzzzz")
#
#zumbido = funcion_decoradora(zumbido)


@funcion_decoradora
def zumbido():
    print("Buzzzzzz")


class Millas():
    """
    Esta clase convierte los kilometros a millas
    """
    def Conversion_a_kilometros(self):
        """
        Esta funcion convierte los kilometros a millas 
        """
        return(self._distancia*1.609344)
    
    def __init__(self):
        """
        En la funcion __init__ es el constructor y aqui se definen las variables de la clase con el estilo
        self.variable
        """
        self._distancia = 0

    # Metodo getter
    @property
    def distancia(self):
        """
        asignamos la funcion distancia
        """
        pass
    @distancia.getter
    def distancia(self):
        """
        Esta funcion devuelve la distancia
        """
        print("Llamada del metodo getter")
        return self._distancia
    @distancia.setter    
    def distancia(self, recorrido):
        """
        funcion para definir el valor de _distancia 
        """
        print(f"Llamada al metodo Setter y el valor de recorrido es {recorrido}")
        self._distancia = recorrido
    @distancia.deleter  
    def distancia(self):
        """
        Funcion para eliminar el atributo _distancia 
        """
        del self._distancia
        

    #distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)


if __name__ == "__main__":
    zumbido()
    avion = Millas()
    avion.distancia = 200
    print(avion.distancia)
    print(avion.Conversion_a_kilometros())

