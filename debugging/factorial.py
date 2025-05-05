#!/usr/bin/python3
import sys

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("L'entrée doit être un entier non négatif")
    if n == 0:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <entier>")
        sys.exit(1)
    try:
        num = int(sys.argv[1])
        fact = factorial(num)
        print(fact)
    except ValueError as e:
        print(f"Erreur: {e}")
        sys.exit(1)
