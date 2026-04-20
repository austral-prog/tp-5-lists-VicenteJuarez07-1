def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """

    # ________________________________________RESOLUCION EJERCICIO 4_______________________________________

    lenght = len(lista)

    if lenght > 5:
        lista.pop(5)
    if lenght > 4:
        lista.pop(4)
    if lenght > 0:
        lista.pop(0)
    return lista