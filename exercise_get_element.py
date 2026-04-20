def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """

    # ________________________________________RESOLUCION EJERCICIO 2_______________________________________

    length = len(lista)

    if -1 <= indice < length:
        return lista[indice]
    else:
        return None

