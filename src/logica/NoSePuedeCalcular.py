class NoSePuedeCalcular(Exception):
    """Excepción lanzada cuando no se puede calcular la media."""
    pass


def calcular_media(elementos):
    """Calcula la media de una lista de elementos."""
    if not elementos:  # Verifica si la lista está vacía
        raise NoSePuedeCalcular("No se puede calcular la media de una lista vacía.")

    return sum(elementos) / len(elementos)