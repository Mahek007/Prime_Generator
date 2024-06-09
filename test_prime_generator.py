import unittest
from prime_generator import PrimeGenerator

class TestPrimeGenerator(unittest.TestCase):
    def setUp(self):
        self.prime_gen = PrimeGenerator()

    def test_sieve_of_eratosthenes(self):
        self.assertEqual(self.prime_gen.sieve_of_eratosthenes(1, 10), [2, 3, 5, 7])
        self.assertEqual(self.prime_gen.sieve_of_eratosthenes(10, 20), [11, 13, 17, 19])
        self.assertEqual(self.prime_gen.sieve_of_eratosthenes(20, 30), [23, 29])

    def test_trial_division(self):
        self.assertEqual(self.prime_gen.trial_division(1, 10), [2, 3, 5, 7])
        self.assertEqual(self.prime_gen.trial_division(10, 20), [11, 13, 17, 19])
        self.assertEqual(self.prime_gen.trial_division(20, 30), [23, 29])

if __name__ == '__main__':
    unittest.main()
