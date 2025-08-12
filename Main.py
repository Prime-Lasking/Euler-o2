import LogFunctions as l
import SimpleFunctions as si
import TrigFunctions as t
import ComplexFunctions as c
import ShapesFunctions as sh
import PrimeFunctions as pr

def listen():
    return input("Type your command: ").lower().strip()

bot_name: str = 'Euler'
print(f'Hello! I\'m {bot_name}!')

command_map = {
    'hi': lambda: print('Hi there! How can I help you?'),
    'hello': lambda: print('Hi there! How can I help you?'),
    'hello euler': lambda: print('Hi there! How can I help you?'),
    'hi euler': lambda: print('Hi there! How can I help you?'),

    'bye': lambda: exit_message(),
    'goodbye': lambda: exit_message(),
    'see you later': lambda: exit_message(),
    'see you': lambda: exit_message(),
    'bye euler': lambda: exit_message(),
    'goodbye euler': lambda: exit_message(),
    'exit': lambda: exit_message(),

    'add': si.addition, '+': si.addition, 'addition': si.addition,
    'minus': si.subtraction, '-': si.subtraction, 'subtraction': si.subtraction,
    'division': si.division, '/': si.division, 'div': si.division,
    'multiplication': si.multiplication, 'x': si.multiplication,
    'exponents': si.exponents, '^': si.exponents,
    'square root': si.square_roots, 'sqrt': si.square_roots,
    '!': si.factorial, 'factorial': si.factorial,
    'mod': si.modulus,

    'tan': t.tan, 'cos': t.cos, 'sin': t.sin,
    'arcsin': t.arcsin, 'arctan': t.arctan, 'arccos': t.arccos,
    'cosecant': t.cosecant, 'csc': t.cosecant,
    'secant': t.secant, 'sec': t.secant,
    'cotangent': t.cotangent, 'cot': t.cotangent,

    'log10': l.Log10, 'log2': l.Log2, 'log3': l.Log3,
    'log4': l.Log4, 'log5': l.Log5, 'log': l.Logn,
    'log23': l.Log23,

    'slope': c.Slope_Finder,
    'pythagorean': c.Pythagorean_Theorem,
    'a^2+b^2=c^2': c.Pythagorean_Theorem,
    'pythagoras': c.Pythagorean_Theorem,
    'compound interest': c.Compound_Interest,
    'compound': c.Compound_Interest,
    'simple interest': c.Simple_Interest,
    'simple': c.Simple_Interest,
    'mean': c.Mean,'mode': c.Mode,
    'median': c.Median,'range': c.Range,
    'round': c.Rounding,'rounding': c.Rounding,
    'gcd': c.Greatest_Common_Divisor(),'lcm': c.Least_Common_Multiple(),
    'geometry': c.Geometry_Visualizer(),'cipher':c.Cipher,

    'circle': sh.Circle, 'triangle': sh.Triangle, 'square': sh.Square,
    'rectangle': sh.Rectangle, 'parallelogram': sh.Parallelogram,
    'ellipse': sh.Ellipse, 'rhombus': sh.Rhombus,
    'trapezoid': sh.Trapezoid, 'kite': sh.Kite,
    'polygon': sh.Regular_Polygon, 'regular polygon': sh.Regular_Polygon,

    'normal': pr.normal_primes,
    'mersenne': pr.mersenne_primes,
    'factorial': pr.factorial_primes,
    'additive': pr.additive_primes,
    'twin': pr.twin_primes,
    'fermat': pr.fermat_primes,
    'prime factors': pr.prime_factors,

    'help': lambda: print_help(),
    'trig': lambda: print_trig(),
    'log': lambda: print_log(),
    'complex': lambda: print_complex(),
    'shapes': lambda: print_shapes(),
    'primes': lambda: print_primes(),
}

def exit_message():
    print('Goodbye, see you next time!')
    global flag
    flag = False

def print_help():
    print('Which functions do you need? simple, complex, trig, log, primes or shapes?')

def print_trig():
    print('Trig functions: tan, cos, sin, arcsin, arctan, arccos, cosecant, secant, cotangent')

def print_log():
    print('Log functions: log2, log3, log4, log5, log10, log, log23')

def print_complex():
    print('Complex functions: slope, pythagoras, compound, simple, mean, median, mode, range, rounding, gcd, lcm, geometry, cipher')

def print_shapes():
    print('Shapes: circle, triangle, square, rectangle, parallelogram, ellipse, rhombus, trapezoid, kite, polygon')

def print_primes():
    print("Primes: normal, mersenne, factorial, additive, prue, twin, fermat, prime factors")

flag = True
if __name__ == "__main__":
 while flag:
    user_input = listen()
    action = command_map.get(user_input)
    if action:
        action()
    else:
        print("Sorry, I didn't understand that. Type '?' or 'help' for options.")

