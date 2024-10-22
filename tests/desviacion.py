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

    def test_dos_elementos(self):
        """Debe devolver la desviación estándar para dos elementos."""
        resultado = calcular_desviacion_estandar([4, 10])  # Media = 7, Varianza = 9
        self.assertAlmostEqual(resultado, 3.0)  # sqrt(9) = 3.0

    def test_n_elementos_positivos(self):
        """Debe devolver la desviación estándar para n elementos positivos."""
        resultado = calcular_desviacion_estandar([2, 4, 6, 8, 10])  # Media = 6
        # Varianza = (16 + 4 + 0 + 4 + 16) / 5 = 8.0
        self.assertAlmostEqual(resultado, math.sqrt(8.0))  # sqrt(8) = 2.8284

    def test_n_elementos_ceros(self):
        """Debe devolver 0.0 para una lista con n ceros."""
        self.assertEqual(calcular_desviacion_estandar([0, 0, 0, 0, 0]), 0.0)

    def test_n_elementos_positivos_y_negativos(self):
        """Debe devolver la desviación estándar para n elementos positivos y negativos."""
        resultado = calcular_desviacion_estandar([-10, -5, 0, 5, 10])  # Media = 0
        # Varianza = (100 + 25 + 0 + 25 + 100) / 5 = 50
        self.assertAlmostEqual(resultado, math.sqrt(50))  # sqrt(50) ≈ 7.071

if __name__ == '__main__':
    unittest.main()
