from sympy import *
from maths.split import splitting
from maths.splitFinal import splitFinal
from maths.containsChar import ContainsChar
from sympy.parsing.sympy_parser import parse_expr
class TheoremCode(object):
    def zamena(input_exp):
        print(input_exp)
        status = False
        try:
             input_exp1, input_exp2  = input_exp.split(';')
        except Exception as e:
            return('Exception1')  # later need to change
        try:
            expressionFirst, statusFirst = splitFinal(input_exp1)
        except Exception as e:
            return('Exception2')  # later need to change

        try:
            part1,part2,sign = splitting(input_exp2)
        except Exception as e:
            return('Exception3')

        expressionFirst = str(expressionFirst)
        part1 = str(part1)
        part2 = str(part2)
       
        expressionFirst = expressionFirst.replace(part1, part2)
        return(expressionFirst)