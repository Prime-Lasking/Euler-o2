import math as m

def cot(n):
    return 1/m.tan(n)
pi = m.pi

def Circle():
    print("Sure! Let's do some Circles!")
    try:
        Radius: float = float(input("Enter radius: "))
        print(f'The Circumference is {2 * pi * Radius} The Area is {(pi ** 2) * Radius}')
    except ValueError:
        print("That doesn't seem to be a valid Radius.")

def Triangle():
    print("Sure! Let's do some Triangles!")
    try:
        a: float = float(input("Enter side a: "))
        b: float = float(input("Enter side b: "))
        c: float = float(input("Enter side c: "))
        base: float = float(input("Enter base: "))
        height: float = float(input("Enter height: "))
        print(f'The Perimeter is {a + b + c} The Area is {0.5 * base * height}')
    except ValueError:
        print("That doesn't seem valid.")

def Square():
    print("Sure! Let's do some Squares")
    try:
        a: float = float(input("Enter side length: "))
        print(f'The Perimeter is {a * 4} The Area is {a ** 2}')
    except ValueError:
        print("That doesn't seem valid.")

def Rectangle():
    print("Sure! Let's do some Rectangles!")
    try:
        length: float = float(input("Enter length: "))
        width: float = float(input("Enter width: "))
        print(f'The Perimeter is {(length * 2) + (width * 2)} The Area is {length * width}')
    except ValueError:
        print("That doesn't seem valid.")

def Parallelogram():
    print("Sure! Let's do some Parallelograms!")
    try:
        base: float = float(input("Enter base: "))
        height: float = float(input("Enter height: "))
        a: float = float(input("Enter side a: "))
        b: float = float(input("Enter side b: "))
        print(f'The Perimeter is {2 * (a + b)} The Area is {height * base}')
    except ValueError:
        print("That doesn't seem valid.")

def Ellipse():
    print("Sure! Let's do some Ellipses!")
    try:
        a: float = float(input("Enter semi-major axis (a): "))
        b: float = float(input("Enter semi-minor axis (b): "))
        print(f'The Perimeter is around {pi * (((3 * a) + b) - ((3 * a) + b) * (a + (3 * b)))} there isn\'t a formula for it  The Area is {pi * a * b}')
    except ValueError:
        print("That doesn't seem valid.")

def Rhombus():
    print("Sure! Let's do some Rhombuses!")
    try:
        d1: float = float(input("Enter diagonal 1: "))
        d2: float = float(input("Enter diagonal 2: "))
        a: float = float(input("Enter side length: "))
        print(f'The Perimeter is {4 * a} The Area is {0.5 * d1 * d2}')
    except ValueError:
        print("That doesn't seem valid.")

def Trapezoid():
    print("Sure! Let's do some Trapezoids!")
    try:
        a: float = float(input("Enter side a: "))
        b: float = float(input("Enter side b: "))
        c: float = float(input("Enter side c: "))
        d: float = float(input("Enter side d: "))
        Height: float = float(input("Enter height: "))
        print(f'The Perimeter is {a + b + c + d} The Area is {0.5 * (a + b) * Height}')
    except ValueError:
        print("That doesn't seem valid.")

def Kite():
    print("Sure! Let's do some Kites!")
    try:
        a: float = float(input("Enter side a: "))
        b: float = float(input("Enter side b: "))
        d1: float = float(input("Enter diagonal 1: "))
        d2: float = float(input("Enter diagonal 2: "))
        print(f'The Perimeter is {2 * (a + b)} The Area is {0.5 * d1 * d2}')
    except ValueError:
        print("That doesn't seem valid.")

def Regular_Polygon():
    print("Sure! Let's do some Regular Polygons!")
    try:
        n: int = int(input("Enter number of sides: "))
        a: float = float(input("Enter side length: "))
        print(f'The Perimeter is {n * a} The Area is {n * (a ** 2) * 0.25 * cot(pi / n)}')
    except ValueError:
        print("That doesn't seem valid.")