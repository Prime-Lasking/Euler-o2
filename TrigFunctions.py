import math as m

def tan():
    print("Sure! Let's do some tangents. Please provide a number.")
    try:
        num: float = float(input("Enter angle in radians: "))
        print(f'The answer is {m.tan(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def sin():
    print("Sure! Let's do some sines. Please provide a number.")
    try:
        num: float = float(input("Enter angle in radians: "))
        print(f'The answer is {m.sin(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def cos():
    print("Sure! Let's do some cosines. Please provide a number.")
    try:
        num: float = float(input("Enter angle in radians: "))
        print(f'The answer is {m.cos(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def arctan():
    print("Sure! Let's do some arctangents. Please provide a number.")
    try:
        num: float = float(input("Enter value: "))
        print(f'The answer is {m.atan(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def arcsin():
    print("Sure! Let's do some arcsines. Please provide a number.")
    try:
        num: float = float(input("Enter value between -1 and 1: "))
        print(f'The answer is {m.asin(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def arccos():
    print("Sure! Let's do some arccosines. Please provide a number.")
    try:
        num: float = float(input("Enter value between -1 and 1: "))
        print(f'The answer is {m.acos(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def cotangent():
    print("Sure! Let's do some cotangents. Please provide a number.")
    try:
        num: float = float(input("Enter angle in radians: "))
        print(f'The answer is {1 / m.tan(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def secant():
    print("Sure! Let's do some secants. Please provide a number.")
    try:
        num: float = float(input("Enter angle in radians: "))
        print(f'The answer is {1 / m.cos(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def cosecant():
    print("Sure! Let's do some cosecants. Please provide a number.")
    try:
        num: float = float(input("Enter angle in radians: "))
        print(f'The answer is {1 / m.sin(num)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")