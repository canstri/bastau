from sympy import *
from mpmath import *

def splitFinal(string):
    znak = ""
    lhs = ""
    rhs = ""
    met = False
    for i in range (0, len(string)):
        if (string[i] == "C"):
            rhs += string[i]
            met= True
            continue

        if met == False:
            lhs += string[i]
        else:
           rhs += string[i]
    result_array = [lhs, rhs]
    return lhs,rhs
#print(splitFinal('n**3-n =(n-1)*n*(n + 1) Correct'))