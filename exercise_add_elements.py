def add_elements(lista):
    """
    Agrega 'Pink' al principio y 'Yellow' al final de la lista.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista modificada con los elementos agregados
    """

    # ________________________________________RESOLUCION EJERCICIO 3_______________________________________

    lista.append("Yellow")
    lista.insert(0, "Pink")
    return lista
