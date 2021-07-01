import random

def busqueda_lineal(lista,objetivo):

    """
    Funcion que hace una busqueda lineal
    """
    match=False
    slot=0
    
    for elemento in lista:
        if elemento== objetivo:
            match=True
            break
        slot+=1
    return match, slot 

if __name__ == "__main__":
    size_list=int(input("De que tamaño sera la lista? "))
    match_number=int(input(" Que numero quieres encontrar? " ))

    lista=[random.randint(0,100) for i in range(size_list)]
    encontrado , slot = busqueda_lineal(lista,match_number)
    print(lista)
    print(f'El elemento {match_number} {"esta" if encontrado else "no esta"} en la lista en el slot {slot}')


    