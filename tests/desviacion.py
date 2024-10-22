import unittest
from desviacion import calcular_desviacion_estandar, NoSePuedeCalcularDesviacion

class TestCalcularDesviacionEstandar(unittest.TestCase):

    def test_lista_vacia(self):
        """Debe lanzar NoSePuedeCalcularDesviacion para lista vacía."""
        with self.assertRaises(NoSePuedeCalcularDesviacion):
            calcular_desviacion_estandar([])  # Intento de calcular desviación estándar en lista vacía

    def test_un_elemento(self):
        """Debe devolver 0.0 para una lista con un solo elemento."""
        self.assertEqual(calcular_desviacion_estandar([5]), 0.0)  # La desviación de [5] es 0.0

if __name__ == '__main__':
    unittest.main()
