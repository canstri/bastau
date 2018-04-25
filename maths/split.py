from sympy import *
from mpmath import *

def splitting(string):
    sign = ""
    lhs = ""
    rhs = ""
    met = False
    skip = False
    for i in range (0, len(string)):
        if skip == True:
            skip = False
            continue
        if (string[i] == ">" and string[i+1] == "=") or (string[i] == "<" and string[i+1] == "="):
            met = True
            sign = string[i] + string[i+1]
            skip = True
            continue
        elif string[i] == ">" or string[i] == "<" or string[i] == "=" or string[i] == "#" or string[i] == "~":
            met = True
            sign = string[i]
            skip = False
            continue
        if met == False:
            lhs += string[i]
        else:
            rhs += string[i]

    if lhs == '' or rhs == '':
        return "Wrong"
    lhs = sympify(lhs)
    rhs = sympify(rhs)
    return(lhs, rhs, sign)
