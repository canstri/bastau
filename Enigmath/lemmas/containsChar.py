from sympy import *
import mpmath
def ContainsChar(input):
    set = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    for c in set:
        if c in input:
            b = input.replace(c, '10')
            return b
    return input
