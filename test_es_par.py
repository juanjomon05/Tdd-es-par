import unittest
from math_utils import es_par 

class TestEsPar(unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))

class TestNoEsPar(unittest.TestCase):
    def test_no_es_par(self):
        self.assertFalse(es_par(3))

class TestEsCero(unittest.TestCase):
    def test_0_es_par(self):
        self.assertTrue(es_par(0))


if __name__ == "__main__":
    unittest.main()