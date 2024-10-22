class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular la media."""
    pass


def calcular_media(elementos):
    """Calcula la media de una lista de elementos."""
    if not elementos:  # Verifica si la lista está vacía
        raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía.")

    for elem in elementos:
        if not isinstance(elem, (int, float)):
            raise TypeError(f"Elemento no numérico encontrado: {elem}")

    if len(elementos) == 1:  # Caso con un solo elemento
        return elementos[0]

    return sum(elementos) / len(elementos)