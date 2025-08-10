import math as m
import statistics as stat
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from typing import Any
def Slope_Finder():
    print(f"Sure! Let's find the slope! Please provide 2 points x and y")
    try:
        x1: float = float(input("Enter x1: "))
        y1: float = float(input("Enter y1: "))
        x2: float = float(input("Enter x2: "))
        y2: float = float(input("Enter y2: "))
        print(f'The Slope is {(y2 - y1) / (x2 - x1)}')
    except ZeroDivisionError:
        print(f"That's Division by zero")
    except ValueError:
        print(f"That doesn't seem to be a valid set of points.")

def Pythagorean_Theorem():
    print(f"Sure! Let's get c. Please provide a and b")
    try:
        a: float = float(input("Enter side a: "))
        b: float = float(input("Enter side b: "))
        print(f'C is equal to {m.sqrt(a ** 2 + b ** 2)}')
    except ValueError:
        print(f"That doesn't seem to be a valid number.")
    except ZeroDivisionError:
        print("That's division by zero")

def Compound_Interest():
    print(f"Sure! Let's do some Compound interest. Please provide some info")
    try:
        P: float = float(input("Enter Principal amount (P): "))
        R: float = float(input("Enter Annual Interest Rate (R) as a decimal: "))
        T: float = float(input("Enter Time in years (T): "))
        N: float = float(input("Enter Number of times interest is compounded per year (N): "))
        print(f'Compounded {N} times gives you {round(P * ((1 + R / N) ** (N * T)), 2)} dollars')
    except ValueError:
        print(f"That doesn't seem to be a valid number.")
    except ZeroDivisionError:
        print("That's division by zero")

def Simple_Interest():
    print(f"Sure! Let's do some Simple interest. Please provide some info")
    try:
        P: float = float(input("Enter Principal amount (P): "))
        R: float = float(input("Enter Annual Interest Rate (R) in %: "))
        T: float = float(input("Enter Time in years (T): "))
        print(f'If you add interest to your initial sum of money you get {round(P * (1 + ((R / 100) * T)), 2)} dollars')
    except ValueError:
        print(f"That doesn't seem to be a valid number.")
    except ZeroDivisionError:
        print("That's division by zero")

def Mean():
    print("Let's calculate the Mean. Please provide some numbers separated by spaces.")
    try:
        data = list(map(float, input("Enter numbers: ").split()))
        mean_value = stat.mean(data)
        print(f"Mean: {mean_value}")
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Median():
    print("Let's calculate the Median. Please provide some numbers separated by spaces.")
    try:
        data = list(map(float, input("Enter numbers: ").split()))
        data.sort()
        median_value = stat.median(data)
        print(f"Median: {median_value}")
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Mode():
    print("Let's calculate the Mode. Provide some numbers separated by spaces.")
    try:
        data = list(map(float, input("Enter numbers: ").split()))
        mode_value = stat.mode(data)
        print(f"Mode: {mode_value}")
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Range():
    print("Let's calculate the Range. Please provide some numbers separated by spaces.")
    try:
        data = list(map(float, input("Enter numbers: ").split()))
        smallest_number = min(data)
        biggest_number = max(data)
        Range_value = biggest_number - smallest_number
        print(f'Range: {Range_value}')
    except ValueError:
        print("That doesn't seem to be a valid number.")

def Rounding():
    print("Let's calculate the rounding of some numbers. Please provide a number and precision.")
    try:
        num: float = float(input("Enter number to round: "))
        Precision: int = int(input("Enter number of decimal places: "))
        print(round(num, Precision))
    except ValueError:
        print("There seems to be an error. Remember to enter valid numbers.")
def Greatest_Common_Divisor():
    print("Let's calculate the greatest common divisor. Please provide 2 numbers.")
try:
    num1: int = int(input("Enter number 1: "))
    num2: int = int(input("Enter number 2: "))
    print(m.gcd(num1,num2))
except ValueError:
    print("There seems to be an error. Remember to enter valid numbers.")
def Least_Common_Multiple():
    print("Let's calculate the least common multiple. Please provide 2 numbers.")
    try:
        num1: int = int(input("Enter number 1: "))
        num2: int = int(input("Enter number 2: "))
        print("The LCM is:", m.lcm(num1, num2))
    except ValueError:
        print("Please enter valid integers.")

def Geometry_Visualizer():
    print("Welcome to the Geometry Visualizer!")
    print("Choose a shape to draw: circle, rectangle, triangle")
    shape = input("Enter shape name: ").strip().lower()

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    try:
        if shape == "circle":
            radius = float(input("Enter radius: "))
            circle = patches.Circle((0, 0), radius, edgecolor='blue', facecolor='lightblue')
            ax.add_patch(circle)
            plt.title(f"Circle with radius {radius}")

        elif shape == "rectangle":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            rect = patches.Rectangle((-width/2, -height/2), width, height, edgecolor='green', facecolor='lightgreen')
            ax.add_patch(rect)
            plt.title(f"Rectangle {width}×{height}")

        elif shape == "triangle":
            print("Enter coordinates of the 3 vertices:")
            x1, y1 = map(float, input("Vertex 1 (x y): ").split())
            x2, y2 = map(float, input("Vertex 2 (x y): ").split())
            x3, y3 = map(float, input("Vertex 3 (x y): ").split())
            triangle = patches.Polygon([[x1, y1], [x2, y2], [x3, y3]], edgecolor='red', facecolor='salmon')
            ax.add_patch(triangle)
            plt.title("Triangle")

        else:
            print("Unsupported shape. Try circle, rectangle, or triangle.")
            return

        plt.grid(True)
        plt.show()

    except ValueError:
        print("Invalid input. Please enter numeric values.")


translator: dict[str | Any, int | Any] = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 0
}

translator2: dict[int | Any, str | Any] = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
    21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 0: ' '
}

def Cipher():
    print("Sure! Let's do some cipher encoding.")
    try:
        user_input = input("Enter message to encode (lowercase letters and spaces only): ")
        key = int(input("Enter numeric key: "))
        user_inputs = list(user_input)

        print("Encoded message:")
        for letter in user_inputs:
            if letter not in translator:
                print(f"[Invalid character: {letter}]")
                continue
            value = translator[letter] * key
            if value % 26 != 0:
                print(translator2[value % 26], end='')
            else:
                print(translator2[1], end='')
        print()
    except ValueError:
        print("That doesn't seem to be a valid number.")