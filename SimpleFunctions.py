import math as m

def addition():
    print("Sure! Let's do some addition! Please provide 2 numbers for me to add.")
    try:
        num1: float = float(input("Enter first number: "))
        num2: float = float(input("Enter second number: "))
        print(f'The sum is {num1 + num2}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def subtraction():
    print("Sure! Let's do some subtraction. Please provide 2 different numbers.")
    try:
        num1: float = float(input("Enter first number: "))
        num2: float = float(input("Enter second number: "))
        print(f'The answer is {num1 - num2}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def division():
    print("Sure! Let's do some division. Please provide 2 different numbers.")
    try:
        num1: float = float(input("Enter numerator: "))
        num2: float = float(input("Enter denominator: "))
        print(f'The answer is {num1 / num2}')
    except ValueError:
        print("That doesn't seem to be a valid number.")
    except ZeroDivisionError:
        print("That's division by zero.")

def multiplication():
    print("Sure! Let's do some multiplication. Please provide 2 different numbers.")
    try:
        num1: float = float(input("Enter first number: "))
        num2: float = float(input("Enter second number: "))
        print(f'The product is {num1 * num2}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def exponents():
    print("Sure! Let's do some Exponents. Please provide a base and an exponent.")
    try:
        base: float = float(input("Enter base: "))
        exponent: float = float(input("Enter exponent: "))
        print(f'The answer is {base ** exponent}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def square_roots():
    print("Sure! Let's do some Square roots. Please provide a number.")
    try:
        num: float = float(input("Enter number: "))
        print(f'The answer is {num ** 0.5}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def factorial():
    print("Sure! Let's do some Factorials. Please provide a number (factorials only use integers).")
    try:
        num: int = int(input("Enter integer: "))
        print(f'The answer is {m.factorial(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def modulus():
    print("Sure! Let's do a Modulus. Please provide 2 different numbers.")
    try:
        num1: float = float(input("Enter dividend: "))
        num2: float = float(input("Enter divisor: "))
        print(f'The answer is {num1 % num2}')
    except ValueError:
        print("That doesn't seem to be a valid number.")