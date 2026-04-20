def check_lists(lista1, lista2):
    """
    Verifica si ambas listas tienen el mismo elemento en la tercera posición.
    Si alguna de las listas no tiene un tercer elemento, retorna False.

    Args:
        lista1: Primera lista
        lista2: Segunda lista

    Returns:
        True si ambas listas tienen el mismo tercer elemento, False en caso contrario
    """

    # ________________________________________RESOLUCION EJERCICIO 11_______________________________________

    lenght1 = len(lista1)
    lenght2 = len(lista2)

    if lenght1 < 4:
        return False
    elif lenght2 < 4:
        return False
    elif lista1[2] == lista2[2]:
        return True
    else:
        return False