import unittest
from math_utils import es_par 
from test_es_multiplo_de import es_multiplo_de 

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))

class TestNoEsPar(unittest.TestCase):
    def test_no_es_par(self):
        self.assertFalse(es_par(3))

class TestEsCero(unittest.TestCase):
    def test_0_es_par(self):
        self.assertTrue(es_par(0))

class TestEsNegativo(unittest.TestCase):
    def test_es_negativo(self):
        self.assertTrue(es_par(-2))
        
class TestEsNegativo(unittest.TestCase):
    def test_es_negativo(self):
        self.assertFalse(es_par(-1))

class TestEsMultiplo(unittest.TestCase):
    def test_6_es_multiplo_de_6(self):
        self.assertTrue(es_multiplo_de(6,2))

if __name__ == "__main__":
    unittest.main()