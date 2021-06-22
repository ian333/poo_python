def potencia_cubo(numero):
    """
    Esta funcion regresa un numero elevado al cubo
    """
    return numero**3


def presentarse(nombre):
    return f'Me llamo {nombre}'


def estudiemos_juntos(nombre):
    return f'Hey estudiemos juntos python {nombre}'


def consume_funciones(funcion_a_llamar):
    return funcion_a_llamar("Sebastian")


def funcion_mayor():
    print("Esta es una función mayor y su mensaje de salida.")

    def librerias():
        print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

    def frameworks():
        print("Algunos frameworks de Python son: Django, Dash y Flask.")

    frameworks()
    librerias()


if __name__ == "__main__":
    print(consume_funciones(presentarse))
    print(consume_funciones(estudiemos_juntos))
    funcion_mayor()
