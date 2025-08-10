import math as m
import sympy as sy
def is_prime(n):
    return sy.isprime(n)

def normal_primes():
    print("Let's find some normal primes. Provide a limit.")
    try:
        limit = int(input("Enter upper limit: "))
        primes = [i for i in range(2, limit + 1) if is_prime(i)]
        print(f'Primes up to {limit}: {primes}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def mersenne_primes():
    print("Let's find some Mersenne primes. Provide a max exponent.")
    try:
        max_exp = int(input("Enter maximum exponent: "))
        primes = []
        for p in range(2, max_exp + 1):
            candidate = 2**p - 1
            if is_prime(candidate):
                primes.append(candidate)
        print(f'Mersenne primes up to exponent {max_exp}: {primes}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def factorial_primes():
    print("Let's check factorial primes. Provide a number.")
    try:
        n = int(input("Enter number for factorial: "))
        f = m.factorial(n)
        results = []
        if is_prime(f + 1):
            results.append(f + 1)
        if is_prime(f - 1):
            results.append(f - 1)
        print(f'Factorial primes around {n}!: {results}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def additive_primes():
    print("Let's find additive primes. Provide a limit.")
    try:
        limit = int(input("Enter upper limit: "))
        primes = []
        for i in range(2, limit + 1):
            if is_prime(i) and is_prime(sum(map(int, str(i)))):
                primes.append(i)
        print(f'Additive primes up to {limit}: {primes}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def twin_primes():
    print("Let's find twin primes. Provide a limit.")
    try:
        limit = int(input("Enter upper limit: "))
        twins = []
        for i in range(2, limit):
            if is_prime(i) and is_prime(i + 2):
                twins.append((i, i + 2))
        print(f'Twin primes up to {limit}: {twins}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def fermat_primes():
    print("Let's find Fermat primes. Provide how many you want.")
    try:
        count = int(input("Enter number of Fermat primes to find: "))
        primes = []
        for i in range(count):
            f = 2**(2**i) + 1
            if is_prime(f):
                primes.append(f)
        print(f'First {count} Fermat primes: {primes}')
    except ValueError:
        print("That doesn't seem to be a valid number.")
def prime_factors():
    print("Let's find the Prime factors. Provide a number.")
    try:
        num = int(input("Enter the number here: "))
        primefactors = list(sy.primefactors(num))
        for factor in primefactors:
            print(factor)
    except ValueError:
        print("That looks like an invalid number")