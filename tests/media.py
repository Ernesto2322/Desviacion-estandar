import unittest
from media import calcular_media, NoSePuedeCalcular

class TestCalcularMedia(unittest.TestCase):

    def test_lista_vacia(self):
        """Debe lanzar NoSePuedeCalcular para lista vacía. """
        with self.assertRaises(NoSePuedeCalcular):
            calcular_media([])  # Intento de calcular media en lista vacía

    def test_un_elemento(self):
        """Debe devolver el valor del único elemento."""
        self.assertEqual(calcular_media([5]), 5)  # La media de [5] es 5

    def test_dos_elementos(self):
        """Debe devolver el promedio de dos elementos."""
        self.assertEqual(calcular_media([4, 6]), 5)  # (4 + 6) / 2 = 5

    def test_n_elementos_positivos(self):
        """Debe devolver el promedio de n elementos positivos."""
        self.assertEqual(calcular_media([2, 4, 6, 8, 10]), 6)  # (2 + 4 + 6 + 8 + 10) / 5 = 6

if __name__ == '__main__':
    unittest.main()
