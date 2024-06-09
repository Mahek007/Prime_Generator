import argparse
import time
from prime_generator import PrimeGenerator

def main():
    parser = argparse.ArgumentParser(description="Generate prime numbers in a range.")
    parser.add_argument("start", type=int, help="Start:")
    parser.add_argument("end", type=int, help="End:")
    parser.add_argument("strategy", choices=["sieve", "trial"], help="Prime generation strategy")

    args = parser.parse_args()
    prime_gen = PrimeGenerator()

    start_time = time.time()

    if args.strategy == "sieve":
        primes = prime_gen.sieve_of_eratosthenes(args.start, args.end)
    elif args.strategy == "trial":
        primes = prime_gen.trial_division(args.start, args.end)

    end_time = time.time()
    print(f"Primes: {primes}")
    print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == '__main__':
    main()
