from __future__ import division
from sympy import *
from mpmath import *

def findPower(string):
    power = []
    base  = []
    for i in range (0, len(string)):
        if (string[i] == "*" and string[i+1] == "*"):
            power.append(sympify(string[i+2]))
            base.append(sympify(string[i-1]))
            continue
    return(base,power)
#print(findPower('n**3-n =n*(n**1)*(n+1)'))