import math


class NoSePuedeCalcularDesviacion(Exception):
    """Excepción lanzada cuando no se puede calcular la desviación estándar."""
    pass


def calcular_desviacion_estandar(elementos):
    """Calcula la desviación estándar de una lista de elementos."""
    if not elementos:  # Verifica si la lista está vacía
        raise NoSePuedeCalcularDesviacion("No se puede calcular la desviación estándar de una lista vacía.")

    # Verifica que todos los elementos sean numéricos
    for elem in elementos:
        if not isinstance(elem, (int, float)):
            raise TypeError(f"Elemento no numérico encontrado: {elem}")

    if len(elementos) == 1:  # Caso con un solo elemento
        return 0.0

    media = sum(elementos) / len(elementos)
    varianza = sum((x - media) ** 2 for x in elementos) / len(elementos)
    return math.sqrt(varianza)
