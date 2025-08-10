import math as m

def Log2():
    print("Sure! Let's do some base 2 logs. Please provide a number.")
    try:
        num: float = float(input("Enter number: "))
        print(f'The answer is {m.log(num, 2)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Log10():
    print("Sure! Let's do some base 10 logs. Please provide a number.")
    try:
        num: float = float(input("Enter number: "))
        print(f'The answer is {m.log(num, 10)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Log3():
    print("Sure! Let's do some base 3 logs. Please provide a number.")
    try:
        num: float = float(input("Enter number: "))
        print(f'The answer is {m.log(num, 3)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Log4():
    print("Sure! Let's do some base 4 logs. Please provide a number.")
    try:
        num: float = float(input("Enter number: "))
        print(f'The answer is {m.log(num, 4)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Log23():
    print("Sure! Let's do some base 23 logs. Please provide a number.")
    try:
        num: float = float(input("Enter number: "))
        print(f'The answer is {m.log(num, 23)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Log5():
    print("Sure! Let's do some base 5 logs. Please provide a number.")
    try:
        num: float = float(input("Enter number: "))
        print(f'The answer is {m.log(num, 5)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Logn():
    print("Sure! Let's do some base n logs. Please provide a number and a base.")
    try:
        num: float = float(input("Enter number: "))
        base: int = int(input("Enter base: "))
        print(f'The answer is {m.log(num, base)}')
    except ValueError:
        print("That doesn't seem to be a valid number.")