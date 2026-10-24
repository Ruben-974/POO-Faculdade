import unittest
from Pessoa import Pessoa

class TestePessoa(unittest.TestCase):

    def test_fronteiras_f(self):

        self.assertEqual(Pessoa('F', 19.0, 1.0).calcularImc(), 'abaixo do peso')
        self.assertEqual(Pessoa('F', 19.1, 1.0).calcularImc(), 'no peso normal')
        self.assertEqual(Pessoa('F', 25.7, 1.0).calcularImc(), 'no peso normal')
        self.assertEqual(Pessoa('F', 25.8, 1.0).calcularImc(), 'marginalmente acima do peso')
        self.assertEqual(Pessoa('F', 27.2, 1.0).calcularImc(), 'marginalmente acima do peso')
        self.assertEqual(Pessoa('F', 27.3, 1.0).calcularImc(), 'acima do peso ideal')
        self.assertEqual(Pessoa('F', 32.2, 1.0).calcularImc(), 'acima do peso ideal')
        self.assertEqual(Pessoa('F', 32.3, 1.0).calcularImc(), 'obeso')
        self.assertEqual(Pessoa('F', 32.4, 1.0).calcularImc(), 'obeso')


    def test_fronteiras_m(self):

        self.assertEqual(Pessoa('M', 20.6, 1.0).calcularImc(), 'abaixo do peso')
        self.assertEqual(Pessoa('M', 20.7, 1.0).calcularImc(), 'no peso normal')
        self.assertEqual(Pessoa('M', 26.3, 1.0).calcularImc(), 'no peso normal')
        self.assertEqual(Pessoa('M', 26.4, 1.0).calcularImc(), 'marginalmente acima do peso')
        self.assertEqual(Pessoa('M', 27.7, 1.0).calcularImc(), 'marginalmente acima do peso')
        self.assertEqual(Pessoa('M', 27.8, 1.0).calcularImc(), 'acima do peso ideal')
        self.assertEqual(Pessoa('M', 31.0, 1.0).calcularImc(), 'acima do peso ideal')
        self.assertEqual(Pessoa('M', 31.1, 1.0).calcularImc(), 'obeso')
        self.assertEqual(Pessoa('M', 31.2, 1.0).calcularImc(), 'obeso')


    def test_exemplos_enunciano(self):

        self.assertEqual(Pessoa('F', 60.0, 1.65).calcularImc(), 'no peso normal')
        self.assertEqual(Pessoa('M', 100.0, 1.80).calcularImc(), 'acima do peso ideal')


if __name__ == '__main__':
    unittest.main()