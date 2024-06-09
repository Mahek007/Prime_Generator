import math

class PrimeGenerator:
    def __init__(self):
        pass

    def sieve_of_eratosthenes(self, start, end):
        if end < 2:
            return []
        sieve = [True] * (end + 1)
        sieve[0] = sieve[1] = False
        for n in range(2, int(math.sqrt(end)) + 1):
            if sieve[n]:
                for multiple in range(n * n, end + 1, n):
                    sieve[multiple] = False
        return [n for n in range(start, end + 1) if sieve[n]]

    def trial_division(self, start, end):
        if end < 2:
            return []
        primes = []
        for n in range(max(start, 2), end + 1):
            is_prime = True
            for divisor in range(2, int(math.sqrt(n)) + 1):
                if n % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(n)
        return primes
