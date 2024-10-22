import unittest
from media import calcular_media, NoSePuedeCalcular

class TestCalcularMedia(unittest.TestCase):

    def test_lista_vacia(self):
        """Debe lanzar NoSePuedeCalcular para lista vacía."""
        with self.assertRaises(NoSePuedeCalcular):
            calcular_media([])  # Intento de calcular media en lista vacía

if __name__ == '__main__':
    unittest.main()
