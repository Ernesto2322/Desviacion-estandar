import unittest
from desviacion import calcular_desviacion_estandar, NoSePuedeCalcularDesviacion

class TestCalcularDesviacionEstandar(unittest.TestCase):

    def test_lista_vacia(self):
        """Debe lanzar NoSePuedeCalcularDesviacion para lista vacía."""
        with self.assertRaises(NoSePuedeCalcularDesviacion):
            calcular_desviacion_estandar([])  # Intento de calcular desviación estándar en lista vacía

if __name__ == '__main__':
    unittest.main()
