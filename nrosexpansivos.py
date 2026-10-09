import unittest
import pytest

def expandir(arr):
    resultado = []
    i = 0

    while i < len(arr):
        cifra = arr[i]
        contador = 1

        while i + 1 < len(arr) and arr[i + 1] == cifra:
            contador += 1
            i += 1

        resultado.append(str(contador))
        resultado.append(str(cifra))
        i += 1

    return int(''.join(resultado))

# PRUEBA CON UNITTEST

class ExpanTest(unittest.TestCase):

    def test_caso_1(self):
        self.assertEqual(11, expandir([1]))

    def test_caso_2(self):
        self.assertEqual(21, expandir([1, 1]))

    def test_caso_3(self):
        self.assertEqual(1211, expandir([2, 1]))

# PRUEBA CON PYTEST

@pytest.mark.parametrize("valor, esperado", [
    ([1], 11),
    ([1, 1], 21),
    ([2, 1], 1211)
])
def test_expandir_pytest(valor, esperado):
    assert expandir(valor) == esperado


if __name__ == '__main__':
    unittest.main(verbosity=2)