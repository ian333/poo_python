class Lavadora:
    """
    docstring
    """

    def __init__(self):
        pass

    def lavar(self, temperatura="Caliente"):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        """
        docstring
        """
        print(f'Llenando el tanque con agua en {temperatura}')

    def _anadir_jabon(self):
        """
        docstring
        """
        print("Añadiendo Jabon")

    def _lavar(self):
        print("Lavando la ropa")

    def _centrifugar(self):
        print("Centrifucando la Ropa")


if __name__ == "__main__":
    lavadora=Lavadora()
    lavadora.lavar()