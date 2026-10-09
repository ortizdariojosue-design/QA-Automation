import unittest

def es_divisible(numero, divisor):
    return numero % divisor == 0

def fizzbuzz(numero):
    if es_divisible(numero, 3) and es_divisible(numero, 5):
        return 'FizzBuzz'
    if es_divisible(numero, 3):
        return 'Fizz'
    if es_divisible(numero, 5):
        return 'Buzz'
    return numero

def get_lista(numero):
    lista = []
    for i in range(1, numero + 1):
        lista.append(fizzbuzz(i))  
    return lista


class FizzBuzzTest(unittest.TestCase):

    def test_fizz(self):
        self.assertEqual('Fizz', fizzbuzz(6))

    def test_buzz(self):
        self.assertEqual('Buzz', fizzbuzz(10))

    def test_fizzbuzz(self):
        self.assertEqual('FizzBuzz', fizzbuzz(15))

    def test_numero(self):
        self.assertEqual(7, fizzbuzz(7))

    def test_lista_hasta_5(self):
        esperado = [1, 2, 'Fizz', 4, 'Buzz']
        self.assertEqual(esperado, get_lista(5))


if __name__ == '__main__':
    unittest.main(defaultTest='FizzBuzzTest', argv=[''], verbosity=2, exit=False)