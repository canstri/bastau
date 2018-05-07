from sympy import *
from mpmath import *

def splitFinal(string): 
    lhs = ""
    rhs = ""
    met = False
    for i in range (0, len(string)):
        if len(string) >= i + 6:
            if (string[i] == "C" and string[i+1] == 'o' and string[i+2] == 'r' and string[i+3] == 'r' and string[i+4] == 'e'and string[i+5] == 'c' and string[i+6] == 't'):
                rhs += string[i]
                print("zawel")
                met= True
                continue
        if len(string) >= i + 4:
            if (string[i] == "W" and string[i+1] == 'r' and string[i+2] == 'o' and string[i+3] == 'n' and string[i+4] == 'g'):
                rhs += string[i]
                met= True
                continue
        if len(string) >= i + 4:
            if (string[i] == "N" and string[i+1] == 'e' and string[i+2] == 'e' and string[i+3] == 'd' and string[i+4] == ' '):
                rhs += string[i]
                met= True
                continue

        if met == False:
            lhs += string[i]
        else:
           rhs += string[i]
    print('de', lhs, rhs)
    return(lhs,rhs)
#print(splitFinal('n**3-n =(n-1)*n*(n + 1) Correct'))